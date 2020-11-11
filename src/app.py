from PySide2 import QtGui, QtWidgets
from zipfile import ZipFile

from MainWindow import Ui_flywrench_main_window
from logic import randomize, settings
from gamemaker import convert, write

import os
import platform
import random
import string
import sys

operating_system = platform.platform()


class Ui(QtWidgets.QMainWindow, Ui_flywrench_main_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.settings = settings.Settings()

        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        self.initialize_textboxes()
        self.initialize_buttons()
        self.initialize_checkboxes()

    def initialize_buttons(self):
        # Randomize Seed Button
        seed_random_button = self.findChild(QtWidgets.QPushButton, 'randomize_seed_button')
        seed_random_button.setToolTip('Generate a random string to be used for the seed')
        seed_random_button.clicked.connect(self.randomize_seed)

        # Backup Files Button
        backup_files_button = self.findChild(QtWidgets.QPushButton, 'backup_files_button')
        backup_files_button.setToolTip('Backups up your Flywrench directory based on the "Flywrench Directory" textbox')
        backup_files_button.clicked.connect(lambda: self.compress_files(self.settings.directory))

        # Restore Files Button
        restore_files_button = self.findChild(QtWidgets.QPushButton, 'restore_files_button')
        restore_files_button.setToolTip('Restore Flywrench files from an archive\nOpens a file browser')
        restore_files_button.clicked.connect(lambda: self.restore_files())

        # Browse for directory
        browse_files_button = self.findChild(QtWidgets.QPushButton, 'explore_system_button')
        browse_files_button.setToolTip('Open a file browser to search for your Flywrench installation directory')
        browse_files_button.clicked.connect(self.file_window)

        # Quit Button
        quit_button = self.findChild(QtWidgets.QPushButton, 'quit_button')
        quit_button.setToolTip('Quits the program, duh!')
        quit_button.clicked.connect(QtWidgets.QApplication.instance().quit)

        # Randomize Button
        randomize_button = self.findChild(QtWidgets.QPushButton, 'randomize_button')
        randomize_button.setToolTip('Randomize the levels')
        randomize_button.clicked.connect(self.randomize_levels)

    def initialize_textboxes(self):
        # Randomize Seed Button
        self.seed_textbox = self.findChild(QtWidgets.QLineEdit, 'seed_textbox')
        self.seed_textbox.setText(get_random_string(16))
        self.settings.seed = self.seed_textbox.text()
        self.seed_textbox.textChanged.connect(self.set_settings)

        # Populate Flywrench Directory
        self.directory_textbox = self.findChild(QtWidgets.QLineEdit, 'directory_textbox')
        self.discover_directory()

    def initialize_checkboxes(self):
        self.randomize_checkbox = self.findChild(QtWidgets.QCheckBox, 'walls_checkbox')
        self.randomize_checkbox.setToolTip('Randomize the color of the walls of the levels')
        self.randomize_checkbox.stateChanged.connect(self.set_settings)

    # Events
    def randomize_seed(self):
        self.seed_textbox.setText(get_random_string(16))

    def discover_directory(self):
        if 'Windows' in operating_system:
            path = 'C:/Program Files (x86)/Steam/steamapps/common/Flywrench/'
            placeholder = 'C:/path/to/flywrench/directory'
        elif 'Darwin' in operating_system:
            path = os.path.expanduser('~/Library/Application Support/Steam/steamapps/common/Flywrench/')
            placeholder = '/path/to/flywrench/directory'
        else:
            path = os.path.expanduser('~/.steam/steam/SteamApps/common/Flywrench/')
            placeholder = '/path/to/flywrench/directory'
        self.directory_textbox.setPlaceholderText(placeholder)
        app_name = check_for_application(path)
        if app_name:
            self.directory_textbox.setText(path)
            self.settings.directory = path
        else:
            msg = """Flywrench default directory not found!\nPlease select your directory before randomizing."""
            QtWidgets.QMessageBox.about(self, "Not Found!", msg)

    def file_window(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Flywrench Install Folder"))
        if not directory:
            return
        self.settings.directory = directory
        self.statusBar.showMessage("Selected Directory: " + self.settings.directory)
        sender = self.sender()
        if sender.objectName() == 'explore_system_button':
            self.directory_textbox.setText(self.settings.directory)

    def manual_ops(self):
        sender = self.sender()
        if sender.objectName() == 'backup_files_button':
            self.statusBar.showMessage('Pressed the Backup Files... button')
        elif sender.objectName() == 'restore_files_button':
            self.statusBar.showMessage('Pressed the Restore Files... button')
        else:
            self.statusBar.showMessage('What happened?')

    def set_settings(self):
        sender = self.sender()
        if sender.objectName() == 'walls_checkbox':
            self.settings.walls = self.randomize_checkbox.isChecked()
        elif sender.objectName() == 'seed_textbox':
            if not self.seed_textbox.text():
                self.settings.seed = None
                self.seed_textbox.setStyleSheet("QLineEdit"
                                                "{"
                                                "background : red;"
                                                "font-family: MS Shell Dlg 2;"
                                                "font-size: 12pt;"
                                                "}")
            else:
                self.settings.seed = self.seed_textbox.text()
                self.seed_textbox.setStyleSheet("QLineEdit"
                                                "{"
                                                "background : white;"
                                                "font-family: MS Shell Dlg 2;"
                                                "font-size: 12pt;"
                                                "}")

    def compress_files(self, directory):
        if not check_for_application(directory):
            msg = """Flywrench default directory not found!\nPlease select your directory before randomizing."""
            QtWidgets.QMessageBox.warning(self, "Not Found!", msg)
            return
        os.chdir(directory)
        with ZipFile('FlywrenchFileBackup.zip', 'w') as backup:
            for root, directories, files in os.walk('ReadOnlyFiles/'):
                for file in files:
                    absolute_path = os.path.join(root, file)
                    relative_path = absolute_path.replace(self.settings.directory + '\\', '')
                    backup.write(absolute_path, relative_path)
        QtWidgets.QMessageBox.information(self, "Backup Complete", "Backup archive has been created.")
        self.statusBar.showMessage('Backup finished!')

    def restore_files(self):
        QtWidgets.QMessageBox.information(self, "Select archive", "Select the archive to restore your files from.")
        source = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select the Archive",
            self.settings.directory,
            "Zip Files (*.zip)"
        )
        if not source[0]:
            QtWidgets.QMessageBox.information(self, "Canceled", "Canceling operation.")
            self.statusBar.showMessage('Restore operation canceled!')
            return
        if not check_for_application(self.settings.directory):
            QtWidgets.QMessageBox.warning(
                self,
                "Invalid Directory",
                "The directory selected does not contain the Flywrench executable."
            )
            self.statusBar.showMessage('Flywrench directory is incorrect.')
        try:
            with ZipFile(source[0], 'r') as ref:
                ref.extractall(self.settings.directory)
        except Exception as err:
            msg = f"""
            A problem occured restoring files from the archive:
            
            { err }
            """
            QtWidgets.QMessageBox.warning(self, "An Error has Occurred", msg)
        QtWidgets.QMessageBox.information(self, "Completed Restoring", "Files have been restored from the archive.")
        self.statusBar.showMessage('Restoring files has completed.')

    def randomize_levels(self):
        confirm = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Question,
            "Randomize?",
            "Are you ready to randomize?"
        )
        confirm.addButton(QtWidgets.QMessageBox.Yes)
        confirm.addButton(QtWidgets.QMessageBox.No)
        confirm.setDefaultButton(QtWidgets.QMessageBox.No)

        reply = confirm.exec()
        if reply == QtWidgets.QMessageBox.No:
            return
        else:
            if self.settings.seed is None:
                QtWidgets.QMessageBox.warning(
                    self,
                    "No seed set!",
                    "Please set a seed to start randomizing!"
                )
                return
            elif self.settings.am_i_randomizing() is False:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Nothing selected!",
                    "None of the randomizing options have been selected! Will not randomize."
                )
                return
            game_planets = randomize.level_setup(settings=self.settings)
            randomize.set_seed(seed=self.settings.seed)
            if self.settings.walls:
                randomize.randomize_walls(game_levels=game_planets)
            # TODO: Randomize the Obstacles
            # TODO: Randomize the Turrets
            # TODO: Randomize the Pinwheels
            # TODO: Randomize the Moving Lines
            # TODO: Write levels to files
            write.tofile(game_planets, self.settings)
            print("Finished!")


# Other Functions
def get_random_string(length):
    chars = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(chars) for i in range(length)))
    return result_str


def check_for_application(directory):
    app_names = ["FlywrenchStudio.exe", "FlywrenchStudio.app", "FlywrenchStudio"]
    for app_name in app_names:
        if os.path.exists(os.path.join(directory, app_name)):
            return app_name
    return False


############
# Main App #
############
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()
