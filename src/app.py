from PySide2 import QtGui
from PySide2.QtWidgets import *
from zipfile import ZipFile

from MainWindow import Ui_flywrench_main_window

import os
import platform
import random
import string
import sys

operating_system = platform.platform()


class Settings:
    def __init__(self):
        self.seed = None
        self.walls = False
        self.internal = False
        self.names = False
        self.intros = False
        self.theme = "none"
        self.random_theme = False
        self.directory = ""


class MainWindow(QMainWindow, Ui_flywrench_main_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.settings = Settings()

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        self.initialize_textboxes()
        self.initialize_buttons()
        self.initialize_checkboxes()

    def initialize_buttons(self):
        # Randomize Seed Button
        seed_random_button = self.findChild(QPushButton, 'randomize_seed_button')

        seed_random_button.setToolTip('Generate a random string to be used for the seed')
        seed_random_button.clicked.connect(self.randomize_seed)

        # Backup Files Button
        backup_files_button = self.findChild(QPushButton, 'backup_files_button')
        backup_files_button.setToolTip('Backups up your Flywrench directory based on the "Flywrench Directory" textbox')
        backup_files_button.clicked.connect(lambda: self.compress_files(self.settings.directory))

        # Restore Files Button
        restore_files_button = self.findChild(QPushButton, 'restore_files_button')
        restore_files_button.setToolTip('Restore Flywrench files from an archive\nOpens a file browser')
        restore_files_button.clicked.connect(lambda: self.restore_files())

        # Browse for directory
        browse_files_button = self.findChild(QPushButton, 'explore_system_button')
        browse_files_button.setToolTip('Open a file browser to search for your Flywrench installation directory')
        browse_files_button.clicked.connect(self.file_window)

        # Quit Button
        quit_button = self.findChild(QPushButton, 'quit_button')
        quit_button.setToolTip('Quits the program, duh!')
        quit_button.clicked.connect(QApplication.instance().quit)

    def initialize_textboxes(self):
        # Randomize Seed Button
        self.seed_textbox = self.findChild(QLineEdit, 'seed_textbox')
        self.seed_textbox.setText(get_random_string(16))
        self.seed_textbox.textChanged.connect(self.set_settings)

        # Populate Flywrench Directory
        self.directory_textbox = self.findChild(QLineEdit, 'directory_textbox')
        self.discover_directory()

    def initialize_checkboxes(self):
        self.randomize_checkbox = self.findChild(QCheckBox, 'walls_checkbox')
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
            QMessageBox.about(self, "Not Found!", msg)

    def file_window(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Flywrench Install Folder"))
        if not directory:
            return
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
            QMessageBox.warning(self, "Not Found!", msg)
            return
        os.chdir(directory)
        with ZipFile('FlywrenchFileBackup.zip', 'w') as backup:
            for root, directories, files in os.walk('ReadOnlyFiles/'):
                for file in files:
                    absolute_path = os.path.join(root, file)
                    relative_path = absolute_path.replace(self.settings.directory + '\\', '')
                    backup.write(absolute_path, relative_path)
        QMessageBox.information(self, "Backup Complete", "Backup archive has been created.")
        self.statusBar.showMessage('Backup finished!')

    def restore_files(self):
        QMessageBox.information(self, "Select archive", "Select the archive to restore your files from.")
        source = QFileDialog.getOpenFileName(
            self,
            "Select the Archive",
            self.settings.directory,
            "Zip Files (*.zip)"
        )
        if not source[0]:
            QMessageBox.information(self, "Canceled", "Canceling operation.")
            self.statusBar.showMessage('Restore operation canceled!')
            return
        if not check_for_application(self.settings.directory):
            QMessageBox.warning(
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
        QMessageBox.information(self, "Completed Restoring", "Files have been restored from the archive.")
        self.statusBar.showMessage('Restoring files has completed.')


# Other Functions
def get_random_string(length):
    chars = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(chars) for i in range(length)))
    return result_str


def check_for_application(directory):
    app_names = ["FlywrenchStudio.exe", "FlywrenchStudio.app", "FlywrenchStudio"]
    for app_name in app_names:
        if os.path.exists(directory + app_name):
            return app_name
    else:
        return False


############
# Main App #
############
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()