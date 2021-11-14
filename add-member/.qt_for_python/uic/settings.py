# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Settings_2(object):
    def setupUi(self, Settings_2):
        if not Settings_2.objectName():
            Settings_2.setObjectName(u"Settings_2")
        Settings_2.resize(318, 278)
        self.verticalLayout = QVBoxLayout(Settings_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.settings_body_frame = QFrame(Settings_2)
        self.settings_body_frame.setObjectName(u"settings_body_frame")
        self.settings_body_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.settings_body_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settings_menu = QTabWidget(self.settings_body_frame)
        self.settings_menu.setObjectName(u"settings_menu")
        font = QFont()
        font.setPointSize(9)
        self.settings_menu.setFont(font)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.verticalLayout_3 = QVBoxLayout(self.Settings)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.Settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_5.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_5.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_5.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_5.addWidget(self.checkBox_4)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        font1 = QFont()
        font1.setPointSize(3)
        self.frame_6.setFont(font1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(30, 16777215))
        font2 = QFont()
        font2.setPointSize(8)
        self.lineEdit.setFont(font2)

        self.verticalLayout_9.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_2.setFont(font2)

        self.verticalLayout_9.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_3.setFont(font2)

        self.verticalLayout_9.addWidget(self.lineEdit_3)


        self.horizontalLayout.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.settings_menu.addTab(self.Settings, "")
        self.Info = QWidget()
        self.Info.setObjectName(u"Info")
        self.verticalLayout_6 = QVBoxLayout(self.Info)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.Info)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_5)
        self.textEdit.setObjectName(u"textEdit")
        font3 = QFont()
        font3.setPointSize(5)
        self.textEdit.setFont(font3)

        self.verticalLayout_7.addWidget(self.textEdit)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.settings_menu.addTab(self.Info, "")

        self.verticalLayout_2.addWidget(self.settings_menu)


        self.verticalLayout.addWidget(self.settings_body_frame)


        self.retranslateUi(Settings_2)

        self.settings_menu.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Settings_2)
    # setupUi

    def retranslateUi(self, Settings_2):
        Settings_2.setWindowTitle(QCoreApplication.translate("Settings_2", u"Form", None))
        self.checkBox.setText(QCoreApplication.translate("Settings_2", u"Add members by Id", None))
        self.checkBox_2.setText(QCoreApplication.translate("Settings_2", u"Add members by username", None))
        self.checkBox_3.setText(QCoreApplication.translate("Settings_2", u"Skip already added users", None))
        self.checkBox_4.setText(QCoreApplication.translate("Settings_2", u"Automatic settings for multiple accounts", None))
        self.label.setText(QCoreApplication.translate("Settings_2", u"Interval between member add(secs)", None))
        self.label_2.setText(QCoreApplication.translate("Settings_2", u"Interval between memeber batches(secs)", None))
        self.label_3.setText(QCoreApplication.translate("Settings_2", u"Memebrs per batch", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Settings_2", u"10", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Settings_2", u"60", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Settings_2", u"20", None))
        self.settings_menu.setTabText(self.settings_menu.indexOf(self.Settings), QCoreApplication.translate("Settings_2", u"Settings", None))
        self.textEdit.setHtml(QCoreApplication.translate("Settings_2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt; font-weight:600;\">BOT FOR ADDING MEMBERS TO GROUP</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">The bot can scrape members from certain group and to add them to certain group. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">Telegram"
                        " Api have got restrictions so you can add certain amoun of members per day in one group. If you use more than one account you will be able to add more people faster. I sugest you to set 10 secs time intervla between adding members if you use only one account, 20 people batches and 60 secs betweem batchest. in my experience it works the best in that way if you use one account. If you use more than one account you can set 2 secs time interval between adding members.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">You can get your Api Id and Api Hash from here: https://my.telegram.org/auth</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">For more information text me on: easytelegrambots@gmail.com</span></p></body></html>", None))
        self.settings_menu.setTabText(self.settings_menu.indexOf(self.Info), QCoreApplication.translate("Settings_2", u"Info", None))
    # retranslateUi

