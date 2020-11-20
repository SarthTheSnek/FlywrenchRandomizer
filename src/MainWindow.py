# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flywrenchgui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_flywrench_main_window(object):
    def setupUi(self, flywrench_main_window):
        if not flywrench_main_window.objectName():
            flywrench_main_window.setObjectName(u"flywrench_main_window")
        flywrench_main_window.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(flywrench_main_window.sizePolicy().hasHeightForWidth())
        flywrench_main_window.setSizePolicy(sizePolicy)
        flywrench_main_window.setMinimumSize(QSize(800, 600))
        flywrench_main_window.setMaximumSize(QSize(800, 600))
        flywrench_main_window.setBaseSize(QSize(800, 600))
        font = QFont()
        font.setPointSize(12)
        flywrench_main_window.setFont(font)
        flywrench_main_window.setAnimated(False)
        self.centralwidget = QWidget(flywrench_main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.walls_checkbox = QCheckBox(self.centralwidget)
        self.walls_checkbox.setObjectName(u"walls_checkbox")
        self.walls_checkbox.setGeometry(QRect(10, 140, 399, 23))
        self.all_internals_checkbox = QCheckBox(self.centralwidget)
        self.all_internals_checkbox.setObjectName(u"all_internals_checkbox")
        self.all_internals_checkbox.setEnabled(True)
        self.all_internals_checkbox.setGeometry(QRect(10, 170, 399, 23))
        self.level_names_checkbox = QCheckBox(self.centralwidget)
        self.level_names_checkbox.setObjectName(u"level_names_checkbox")
        self.level_names_checkbox.setEnabled(True)
        self.level_names_checkbox.setGeometry(QRect(10, 390, 399, 23))
        self.dialog_checkbox = QCheckBox(self.centralwidget)
        self.dialog_checkbox.setObjectName(u"dialog_checkbox")
        self.dialog_checkbox.setEnabled(False)
        self.dialog_checkbox.setVisible(False)
        self.dialog_checkbox.setGeometry(QRect(10, 420, 399, 23))
        self.randomizer_options_line = QFrame(self.centralwidget)
        self.randomizer_options_line.setObjectName(u"randomizer_options_line")
        self.randomizer_options_line.setGeometry(QRect(10, 120, 801, 16))
        self.randomizer_options_line.setFrameShape(QFrame.HLine)
        self.randomizer_options_line.setFrameShadow(QFrame.Sunken)
        self.randomizer_label = QLabel(self.centralwidget)
        self.randomizer_label.setObjectName(u"randomizer_label")
        self.randomizer_label.setGeometry(QRect(10, 80, 391, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.randomizer_label.setFont(font1)
        self.randomizer_label.setAlignment(Qt.AlignCenter)
        self.middle_vertical_line = QFrame(self.centralwidget)
        self.middle_vertical_line.setObjectName(u"middle_vertical_line")
        self.middle_vertical_line.setGeometry(QRect(400, 80, 20, 411))
        self.middle_vertical_line.setFrameShape(QFrame.VLine)
        self.middle_vertical_line.setFrameShadow(QFrame.Sunken)
        self.bottom_horizontal_line = QFrame(self.centralwidget)
        self.bottom_horizontal_line.setObjectName(u"bottom_horizontal_line")
        self.bottom_horizontal_line.setGeometry(QRect(0, 490, 801, 16))
        self.bottom_horizontal_line.setFrameShape(QFrame.HLine)
        self.bottom_horizontal_line.setFrameShadow(QFrame.Sunken)
        self.randomize_button = QPushButton(self.centralwidget)
        self.randomize_button.setObjectName(u"randomize_button")
        self.randomize_button.setEnabled(True)
        self.randomize_button.setGeometry(QRect(670, 510, 121, 41))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(603, 80, 20, 411))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.theme_label = QLabel(self.centralwidget)
        self.theme_label.setObjectName(u"theme_label")
        self.theme_label.setEnabled(False)
        self.theme_label.setGeometry(QRect(410, 80, 191, 41))
        self.theme_label.setFont(font1)
        self.theme_label.setVisible(False)
        self.theme_label.setAlignment(Qt.AlignCenter)
        self.manual_ops_label = QLabel(self.centralwidget)
        self.manual_ops_label.setObjectName(u"manual_ops_label")
        self.manual_ops_label.setGeometry(QRect(620, 80, 171, 41))
        self.manual_ops_label.setFont(font1)
        self.manual_ops_label.setAlignment(Qt.AlignCenter)
        self.backup_files_button = QPushButton(self.centralwidget)
        self.backup_files_button.setObjectName(u"backup_files_button")
        self.backup_files_button.setGeometry(QRect(620, 140, 171, 61))
        self.quit_button = QPushButton(self.centralwidget)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setGeometry(QRect(540, 510, 121, 41))
        self.restore_files_button = QPushButton(self.centralwidget)
        self.restore_files_button.setObjectName(u"restore_files_button")
        self.restore_files_button.setGeometry(QRect(620, 210, 171, 61))
        self.theme_combobox = QComboBox(self.centralwidget)
        self.theme_combobox.setObjectName(u"theme_combobox")
        self.theme_combobox.setEnabled(False)
        self.theme_combobox.setVisible(False)
        self.theme_combobox.setGeometry(QRect(420, 140, 181, 22))
        self.theme_combobox.setFrame(True)
        self.random_theme_checkbox = QCheckBox(self.centralwidget)
        self.random_theme_checkbox.setObjectName(u"random_theme_checkbox")
        self.random_theme_checkbox.setEnabled(False)
        self.random_theme_checkbox.setVisible(False)
        self.random_theme_checkbox.setGeometry(QRect(420, 180, 181, 17))
        self.seed_textbox = QLineEdit(self.centralwidget)
        self.seed_textbox.setObjectName(u"seed_textbox")
        self.seed_textbox.setGeometry(QRect(110, 460, 181, 31))
        self.seed_textbox.setMaxLength(16)
        self.seed_label = QLabel(self.centralwidget)
        self.seed_label.setObjectName(u"seed_label")
        self.seed_label.setGeometry(QRect(10, 465, 91, 21))
        self.seed_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.randomize_seed_button = QPushButton(self.centralwidget)
        self.randomize_seed_button.setObjectName(u"randomize_seed_button")
        self.randomize_seed_button.setGeometry(QRect(300, 460, 101, 31))
        self.top_horizontal_line = QFrame(self.centralwidget)
        self.top_horizontal_line.setObjectName(u"top_horizontal_line")
        self.top_horizontal_line.setGeometry(QRect(0, 63, 801, 20))
        self.top_horizontal_line.setFrameShape(QFrame.HLine)
        self.top_horizontal_line.setFrameShadow(QFrame.Sunken)
        self.main_title_label = QLabel(self.centralwidget)
        self.main_title_label.setObjectName(u"main_title_label")
        self.main_title_label.setGeometry(QRect(10, 10, 781, 51))
        font2 = QFont()
        font2.setPointSize(36)
        self.main_title_label.setFont(font2)
        self.main_title_label.setAlignment(Qt.AlignCenter)
        self.directory_ = QLabel(self.centralwidget)
        self.directory_.setObjectName(u"directory_")
        self.directory_.setGeometry(QRect(10, 500, 71, 51))
        self.directory_.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.directory_textbox = QLineEdit(self.centralwidget)
        self.directory_textbox.setObjectName(u"directory_textbox")
        self.directory_textbox.setGeometry(QRect(90, 519, 391, 21))
        self.directory_textbox.setReadOnly(True)
        self.explore_system_button = QPushButton(self.centralwidget)
        self.explore_system_button.setObjectName(u"explore_system_button")
        self.explore_system_button.setGeometry(QRect(490, 520, 21, 21))
        self.explore_system_button.setToolTipDuration(3)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(520, 500, 3, 61))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.turrets_checkbox = QCheckBox(self.centralwidget)
        self.turrets_checkbox.setObjectName(u"turrets_checkbox")
        self.turrets_checkbox.setEnabled(True)
        self.turrets_checkbox.setGeometry(QRect(30, 230, 371, 23))
        self.pinwheels_checkbox = QCheckBox(self.centralwidget)
        self.pinwheels_checkbox.setObjectName(u"pinwheels_checkbox")
        self.pinwheels_checkbox.setGeometry(QRect(30, 260, 371, 23))
        self.movinglines_checkbox = QCheckBox(self.centralwidget)
        self.movinglines_checkbox.setObjectName(u"movinglines_checkbox")
        self.movinglines_checkbox.setEnabled(True)
        self.movinglines_checkbox.setGeometry(QRect(30, 290, 371, 23))
        self.obstacles_checkbox = QCheckBox(self.centralwidget)
        self.obstacles_checkbox.setObjectName(u"obstacles_checkbox")
        self.obstacles_checkbox.setEnabled(False)
        self.obstacles_checkbox.setVisible(False)
        self.obstacles_checkbox.setGeometry(QRect(30, 200, 371, 23))
        flywrench_main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(flywrench_main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        flywrench_main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(flywrench_main_window)
        self.statusbar.setObjectName(u"statusbar")
        flywrench_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(flywrench_main_window)

        QMetaObject.connectSlotsByName(flywrench_main_window)
    # setupUi

    def retranslateUi(self, flywrench_main_window):
        flywrench_main_window.setWindowTitle(QCoreApplication.translate("flywrench_main_window", u"Flywrench Randomizer", None))
        self.walls_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Walls", None))
        self.all_internals_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Internals", None))
        self.level_names_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Randomize Level Names", None))
        self.dialog_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Randomize Opening Cutscene Dialog", None))
        self.randomizer_label.setText(QCoreApplication.translate("flywrench_main_window", u"Randomizer Settings", None))
#if QT_CONFIG(tooltip)
        self.randomize_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.randomize_button.setText(QCoreApplication.translate("flywrench_main_window", u"Randomize", None))
        self.theme_label.setText(QCoreApplication.translate("flywrench_main_window", u"Theme", None))
        self.manual_ops_label.setText(QCoreApplication.translate("flywrench_main_window", u"Manual Ops", None))
#if QT_CONFIG(tooltip)
        self.backup_files_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.backup_files_button.setText(QCoreApplication.translate("flywrench_main_window", u"Backup Files", None))
#if QT_CONFIG(tooltip)
        self.quit_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.quit_button.setText(QCoreApplication.translate("flywrench_main_window", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.restore_files_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.restore_files_button.setText(QCoreApplication.translate("flywrench_main_window", u"Restore Files...", None))
#if QT_CONFIG(tooltip)
        self.theme_combobox.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.random_theme_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.random_theme_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Randomize Theme", None))
#if QT_CONFIG(tooltip)
        self.seed_textbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.seed_textbox.setPlaceholderText(QCoreApplication.translate("flywrench_main_window", u"I'm Random Woah!", None))
        self.seed_label.setText(QCoreApplication.translate("flywrench_main_window", u"Seed", None))
#if QT_CONFIG(tooltip)
        self.randomize_seed_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.randomize_seed_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.randomize_seed_button.setText(QCoreApplication.translate("flywrench_main_window", u"Randomize", None))
        self.main_title_label.setText(QCoreApplication.translate("flywrench_main_window", u"Flywrench Randomizer", None))
        self.directory_.setText(QCoreApplication.translate("flywrench_main_window", u"Flywrench\n"
"Directory:", None))
        self.directory_textbox.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.explore_system_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.explore_system_button.setText(QCoreApplication.translate("flywrench_main_window", u"...", None))
        self.turrets_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Turrets", None))
        self.pinwheels_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Pinwheels", None))
        self.movinglines_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Moving Lines", None))
        self.obstacles_checkbox.setText(QCoreApplication.translate("flywrench_main_window", u"Lines", None))
    # retranslateUi

