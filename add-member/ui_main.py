# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainRLFnXT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
"color: rgb(50, 141, 189, 255);")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.sidebar)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(200, 0))
        self.logo.setMaximumSize(QSize(300, 200))
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo_label = QLabel(self.logo)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(200, 0))
        self.logo_label.setMaximumSize(QSize(16666, 16666))
        self.logo_label.setPixmap(QPixmap(u":/images/logo2.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.logo_label.setIndent(0)

        self.verticalLayout_2.addWidget(self.logo_label)


        self.verticalLayout.addWidget(self.logo)

        self.menu = QFrame(self.sidebar)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(25, 0, 10, 100)
        self.accounts_button = QPushButton(self.menu)
        self.accounts_button.setObjectName(u"accounts_button")
        self.accounts_button.setMaximumSize(QSize(250, 50))
        font = QFont()
        font.setPointSize(11)
        self.accounts_button.setFont(font)
        self.accounts_button.setStyleSheet(u"border-radius:20px;\n"
"border-color:rgb(39,39,39,255);\n"
"border-style:outset;\n"
"border-width:4px;")
        self.accounts_button.setIconSize(QSize(100, 100))
        self.accounts_button.setAutoRepeatDelay(300)

        self.verticalLayout_3.addWidget(self.accounts_button)

        self.scrape_button = QPushButton(self.menu)
        self.scrape_button.setObjectName(u"scrape_button")
        self.scrape_button.setMaximumSize(QSize(250, 50))
        self.scrape_button.setFont(font)
        self.scrape_button.setStyleSheet(u"border-radius:20px;\n"
"border-color:rgb(39,39,39,255);\n"
"border-style:outset;\n"
"border-width:4px;")

        self.verticalLayout_3.addWidget(self.scrape_button)

        self.add_members_button = QPushButton(self.menu)
        self.add_members_button.setObjectName(u"add_members_button")
        self.add_members_button.setMaximumSize(QSize(250, 50))
        self.add_members_button.setFont(font)
        self.add_members_button.setStyleSheet(u"border-radius:20px;\n"
"border-color:rgb(39,39,39,255);\n"
"border-style:outset;\n"
"border-width:4px;")

        self.verticalLayout_3.addWidget(self.add_members_button)


        self.verticalLayout.addWidget(self.menu)


        self.horizontalLayout.addWidget(self.sidebar, 0, Qt.AlignLeft)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.body)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName(u"accounts_page")
        self.verticalLayout_5 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.accounts_label_frame = QFrame(self.accounts_page)
        self.accounts_label_frame.setObjectName(u"accounts_label_frame")
        self.accounts_label_frame.setFrameShape(QFrame.StyledPanel)
        self.accounts_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.accounts_label_frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.accounts_label_frame_2 = QFrame(self.accounts_label_frame)
        self.accounts_label_frame_2.setObjectName(u"accounts_label_frame_2")
        sizePolicy.setHeightForWidth(self.accounts_label_frame_2.sizePolicy().hasHeightForWidth())
        self.accounts_label_frame_2.setSizePolicy(sizePolicy)
        self.accounts_label_frame_2.setFrameShape(QFrame.StyledPanel)
        self.accounts_label_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.accounts_label_frame_2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, 0, 0, 0)
        self.accounts_label = QLabel(self.accounts_label_frame_2)
        self.accounts_label.setObjectName(u"accounts_label")
        self.accounts_label.setMaximumSize(QSize(200, 75))
        font1 = QFont()
        font1.setPointSize(29)
        self.accounts_label.setFont(font1)
        self.accounts_label.setStyleSheet(u"color: rgb(50, 141, 189, 255);")

        self.horizontalLayout_12.addWidget(self.accounts_label)


        self.horizontalLayout_11.addWidget(self.accounts_label_frame_2)

        self.accounts_settings_frame = QFrame(self.accounts_label_frame)
        self.accounts_settings_frame.setObjectName(u"accounts_settings_frame")
        self.accounts_settings_frame.setMaximumSize(QSize(60, 60))
        self.accounts_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.accounts_settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.accounts_settings_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.settings_button_3 = QPushButton(self.accounts_settings_frame)
        self.settings_button_3.setObjectName(u"settings_button_3")
        icon = QIcon()
        icon.addFile(u":/icons/4954068.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button_3.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.settings_button_3)


        self.horizontalLayout_11.addWidget(self.accounts_settings_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.accounts_label_frame)

        self.account_body = QFrame(self.accounts_page)
        self.account_body.setObjectName(u"account_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.account_body.sizePolicy().hasHeightForWidth())
        self.account_body.setSizePolicy(sizePolicy1)
        self.account_body.setFrameShape(QFrame.StyledPanel)
        self.account_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.account_body)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_account = QFrame(self.account_body)
        self.input_account.setObjectName(u"input_account")
        self.input_account.setMaximumSize(QSize(250, 16777215))
        self.input_account.setFrameShape(QFrame.StyledPanel)
        self.input_account.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.input_account)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.input_frame = QFrame(self.input_account)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setMinimumSize(QSize(100, 0))
        self.input_frame.setMaximumSize(QSize(250, 16777215))
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.input_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.phone_input = QLineEdit(self.input_frame)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setMaximumSize(QSize(250, 25))

        self.verticalLayout_8.addWidget(self.phone_input)

        self.api_id_input = QLineEdit(self.input_frame)
        self.api_id_input.setObjectName(u"api_id_input")
        self.api_id_input.setMaximumSize(QSize(250, 25))

        self.verticalLayout_8.addWidget(self.api_id_input)

        self.api_hash_input = QLineEdit(self.input_frame)
        self.api_hash_input.setObjectName(u"api_hash_input")
        self.api_hash_input.setMaximumSize(QSize(250, 25))

        self.verticalLayout_8.addWidget(self.api_hash_input)

        self.accounts_danger_text = QLabel(self.input_frame)
        self.accounts_danger_text.setObjectName(u"accounts_danger_text")
        self.accounts_danger_text.setMaximumSize(QSize(200, 15))
        self.accounts_danger_text.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_8.addWidget(self.accounts_danger_text)


        self.verticalLayout_7.addWidget(self.input_frame)

        self.button_frame = QFrame(self.input_account)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.button_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 170)
        self.add_account_button = QPushButton(self.button_frame)
        self.add_account_button.setObjectName(u"add_account_button")
        self.add_account_button.setMaximumSize(QSize(250, 50))
        self.add_account_button.setFont(font)
        self.add_account_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
"color: rgb(50, 141, 189, 255);\n"
"border-radius:20px;\n"
"border-color:rgb(39,39,39,255);\n"
"border-style:outset;\n"
"border-width:4px;")

        self.verticalLayout_9.addWidget(self.add_account_button)


        self.verticalLayout_7.addWidget(self.button_frame)


        self.horizontalLayout_2.addWidget(self.input_account)

        self.accounts_list_frame = QFrame(self.account_body)
        self.accounts_list_frame.setObjectName(u"accounts_list_frame")
        self.accounts_list_frame.setFrameShape(QFrame.StyledPanel)
        self.accounts_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.accounts_list_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.accounts_list_label = QLabel(self.accounts_list_frame)
        self.accounts_list_label.setObjectName(u"accounts_list_label")
        font2 = QFont()
        font2.setPointSize(12)
        self.accounts_list_label.setFont(font2)
        self.accounts_list_label.setStyleSheet(u"color: rgb(50, 141, 189, 255);")
        self.accounts_list_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.accounts_list_label)

        self.accounts_list = QScrollArea(self.accounts_list_frame)
        self.accounts_list.setObjectName(u"accounts_list")
        self.accounts_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 348, 448))
        self.accounts_list.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.accounts_list)


        self.horizontalLayout_2.addWidget(self.accounts_list_frame)


        self.verticalLayout_5.addWidget(self.account_body)

        self.stackedWidget.addWidget(self.accounts_page)
        self.scrape_page = QWidget()
        self.scrape_page.setObjectName(u"scrape_page")
        self.verticalLayout_11 = QVBoxLayout(self.scrape_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrape_label_frame = QFrame(self.scrape_page)
        self.scrape_label_frame.setObjectName(u"scrape_label_frame")
        self.scrape_label_frame.setMaximumSize(QSize(16777215, 75))
        self.scrape_label_frame.setFrameShape(QFrame.StyledPanel)
        self.scrape_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.scrape_label_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrape_label_frame_2 = QFrame(self.scrape_label_frame)
        self.scrape_label_frame_2.setObjectName(u"scrape_label_frame_2")
        sizePolicy.setHeightForWidth(self.scrape_label_frame_2.sizePolicy().hasHeightForWidth())
        self.scrape_label_frame_2.setSizePolicy(sizePolicy)
        self.scrape_label_frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrape_label_frame_2.setFrameShape(QFrame.StyledPanel)
        self.scrape_label_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.scrape_label_frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(30, 0, 0, 0)
        self.scrape_label = QLabel(self.scrape_label_frame_2)
        self.scrape_label.setObjectName(u"scrape_label")
        self.scrape_label.setMaximumSize(QSize(150, 50))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(29)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.scrape_label.setFont(font3)
        self.scrape_label.setStyleSheet(u"font: 29pt \"MS Shell Dlg 2\";\n"
"color: rgb(50, 141, 189, 255);")

        self.horizontalLayout_10.addWidget(self.scrape_label)


        self.horizontalLayout_9.addWidget(self.scrape_label_frame_2, 0, Qt.AlignTop)

        self.scrape_settings_frame = QFrame(self.scrape_label_frame)
        self.scrape_settings_frame.setObjectName(u"scrape_settings_frame")
        self.scrape_settings_frame.setMaximumSize(QSize(60, 30))
        self.scrape_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.scrape_settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.scrape_settings_frame)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.scrape_settings_button_2 = QPushButton(self.scrape_settings_frame)
        self.scrape_settings_button_2.setObjectName(u"scrape_settings_button_2")
        self.scrape_settings_button_2.setIcon(icon)

        self.verticalLayout_27.addWidget(self.scrape_settings_button_2, 0, Qt.AlignTop)


        self.horizontalLayout_9.addWidget(self.scrape_settings_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.scrape_label_frame, 0, Qt.AlignTop)

        self.scrape_body = QFrame(self.scrape_page)
        self.scrape_body.setObjectName(u"scrape_body")
        sizePolicy1.setHeightForWidth(self.scrape_body.sizePolicy().hasHeightForWidth())
        self.scrape_body.setSizePolicy(sizePolicy1)
        self.scrape_body.setFrameShape(QFrame.StyledPanel)
        self.scrape_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.scrape_body)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scraped_members_frame = QFrame(self.scrape_body)
        self.scraped_members_frame.setObjectName(u"scraped_members_frame")
        self.scraped_members_frame.setMaximumSize(QSize(16777215, 500))
        self.scraped_members_frame.setFrameShape(QFrame.StyledPanel)
        self.scraped_members_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.scraped_members_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scraped_members_label = QLabel(self.scraped_members_frame)
        self.scraped_members_label.setObjectName(u"scraped_members_label")
        self.scraped_members_label.setFont(font2)
        self.scraped_members_label.setStyleSheet(u"color: rgb(50, 141, 189, 255);")

        self.verticalLayout_14.addWidget(self.scraped_members_label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.scraped_members_table = QTableWidget(self.scraped_members_frame)
        if (self.scraped_members_table.columnCount() < 2):
            self.scraped_members_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.scraped_members_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.scraped_members_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.scraped_members_table.setObjectName(u"scraped_members_table")
        self.scraped_members_table.setMaximumSize(QSize(16777215, 500))
        self.scraped_members_table.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.scraped_members_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.scraped_members_table.horizontalHeader().setStretchLastSection(True)
        self.scraped_members_table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_14.addWidget(self.scraped_members_table, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.scraped_members_frame)

        self.scraped_input_frame = QFrame(self.scrape_body)
        self.scraped_input_frame.setObjectName(u"scraped_input_frame")
        self.scraped_input_frame.setFrameShape(QFrame.StyledPanel)
        self.scraped_input_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.scraped_input_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scraped_groups_frame = QFrame(self.scraped_input_frame)
        self.scraped_groups_frame.setObjectName(u"scraped_groups_frame")
        self.scraped_groups_frame.setMaximumSize(QSize(300, 16777215))
        self.scraped_groups_frame.setFrameShape(QFrame.StyledPanel)
        self.scraped_groups_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.scraped_groups_frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrape_groups_label_frame = QFrame(self.scraped_groups_frame)
        self.scrape_groups_label_frame.setObjectName(u"scrape_groups_label_frame")
        self.scrape_groups_label_frame.setFrameShape(QFrame.StyledPanel)
        self.scrape_groups_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.scrape_groups_label_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scraped_groups_label = QLabel(self.scrape_groups_label_frame)
        self.scraped_groups_label.setObjectName(u"scraped_groups_label")
        self.scraped_groups_label.setFont(font2)
        self.scraped_groups_label.setStyleSheet(u"color: rgb(50, 141, 189, 255);")

        self.horizontalLayout_4.addWidget(self.scraped_groups_label)

        self.scraped_groups_refresh_button = QPushButton(self.scrape_groups_label_frame)
        self.scraped_groups_refresh_button.setObjectName(u"scraped_groups_refresh_button")
        self.scraped_groups_refresh_button.setMaximumSize(QSize(30, 20))
        self.scraped_groups_refresh_button.setStyleSheet(u"color: rgb(50, 141, 189, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.scraped_groups_refresh_button.setIcon(icon1)
        self.scraped_groups_refresh_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.scraped_groups_refresh_button)


        self.verticalLayout_15.addWidget(self.scrape_groups_label_frame, 0, Qt.AlignTop)

        self.scrape_group_list_frame = QFrame(self.scraped_groups_frame)
        self.scrape_group_list_frame.setObjectName(u"scrape_group_list_frame")
        sizePolicy1.setHeightForWidth(self.scrape_group_list_frame.sizePolicy().hasHeightForWidth())
        self.scrape_group_list_frame.setSizePolicy(sizePolicy1)
        self.scrape_group_list_frame.setMaximumSize(QSize(300, 16777215))
        self.scrape_group_list_frame.setFrameShape(QFrame.StyledPanel)
        self.scrape_group_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.scrape_group_list_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scaped_groups_list = QScrollArea(self.scrape_group_list_frame)
        self.scaped_groups_list.setObjectName(u"scaped_groups_list")
        self.scaped_groups_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 294, 216))
        self.scaped_groups_list.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_16.addWidget(self.scaped_groups_list)

        self.scraped_groups_from_label = QLabel(self.scrape_group_list_frame)
        self.scraped_groups_from_label.setObjectName(u"scraped_groups_from_label")
        self.scraped_groups_from_label.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout_16.addWidget(self.scraped_groups_from_label)


        self.verticalLayout_15.addWidget(self.scrape_group_list_frame)


        self.horizontalLayout_3.addWidget(self.scraped_groups_frame)

        self.scraped_choose_input_frame = QFrame(self.scraped_input_frame)
        self.scraped_choose_input_frame.setObjectName(u"scraped_choose_input_frame")
        self.scraped_choose_input_frame.setFrameShape(QFrame.StyledPanel)
        self.scraped_choose_input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.scraped_choose_input_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.choose_group_frame = QFrame(self.scraped_choose_input_frame)
        self.choose_group_frame.setObjectName(u"choose_group_frame")
        self.choose_group_frame.setFrameShape(QFrame.StyledPanel)
        self.choose_group_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.choose_group_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.choose_group_label = QLabel(self.choose_group_frame)
        self.choose_group_label.setObjectName(u"choose_group_label")
        self.choose_group_label.setMaximumSize(QSize(260, 16777215))
        self.choose_group_label.setFont(font)
        self.choose_group_label.setStyleSheet(u"color: rgb(50, 141, 189, 255);")
        self.choose_group_label.setTextFormat(Qt.PlainText)
        self.choose_group_label.setScaledContents(False)
        self.choose_group_label.setAlignment(Qt.AlignCenter)
        self.choose_group_label.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.choose_group_label, 0, Qt.AlignHCenter)

        self.choose_group_input = QLineEdit(self.choose_group_frame)
        self.choose_group_input.setObjectName(u"choose_group_input")
        self.choose_group_input.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_18.addWidget(self.choose_group_input, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.choose_group_frame)

        self.line = QFrame(self.scraped_choose_input_frame)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 10))
        self.line.setStyleSheet(u"color: rgb(50, 141, 189, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line)

        self.choose_csv_frame = QFrame(self.scraped_choose_input_frame)
        self.choose_csv_frame.setObjectName(u"choose_csv_frame")
        sizePolicy1.setHeightForWidth(self.choose_csv_frame.sizePolicy().hasHeightForWidth())
        self.choose_csv_frame.setSizePolicy(sizePolicy1)
        self.choose_csv_frame.setFrameShape(QFrame.StyledPanel)
        self.choose_csv_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.choose_csv_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.choose_csv_button = QPushButton(self.choose_csv_frame)
        self.choose_csv_button.setObjectName(u"choose_csv_button")
        self.choose_csv_button.setMaximumSize(QSize(130, 40))
        self.choose_csv_button.setFont(font)
        self.choose_csv_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
"color: rgb(50, 141, 189, 255);\n"
"border-radius:20px;\n"
"border-color:rgb(39,39,39,255);\n"
"border-style:outset;\n"
"border-width:4px;")

        self.horizontalLayout_5.addWidget(self.choose_csv_button)


        self.verticalLayout_17.addWidget(self.choose_csv_frame)


        self.horizontalLayout_3.addWidget(self.scraped_choose_input_frame)


        self.verticalLayout_13.addWidget(self.scraped_input_frame)


        self.verticalLayout_11.addWidget(self.scrape_body)

        self.stackedWidget.addWidget(self.scrape_page)
        self.add_members_page = QWidget()
        self.add_members_page.setObjectName(u"add_members_page")
        self.verticalLayout_19 = QVBoxLayout(self.add_members_page)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, -1)
        self.add_members_label_frame = QFrame(self.add_members_page)
        self.add_members_label_frame.setObjectName(u"add_members_label_frame")
        self.add_members_label_frame.setMaximumSize(QSize(16777215, 75))
        self.add_members_label_frame.setFrameShape(QFrame.StyledPanel)
        self.add_members_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.add_members_label_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_members_label_frame_2 = QFrame(self.add_members_label_frame)
        self.add_members_label_frame_2.setObjectName(u"add_members_label_frame_2")
        sizePolicy.setHeightForWidth(self.add_members_label_frame_2.sizePolicy().hasHeightForWidth())
        self.add_members_label_frame_2.setSizePolicy(sizePolicy)
        self.add_members_label_frame_2.setFrameShape(QFrame.StyledPanel)
        self.add_members_label_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.add_members_label_frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(30, 0, 0, 0)
        self.add_members_labe = QLabel(self.add_members_label_frame_2)
        self.add_members_labe.setObjectName(u"add_members_labe")
        self.add_members_labe.setMaximumSize(QSize(300, 75))
        self.add_members_labe.setStyleSheet(u"font: 29pt \"MS Shell Dlg 2\";\n"
"color: rgb(50, 141, 189, 255);")

        self.horizontalLayout_7.addWidget(self.add_members_labe)


        self.horizontalLayout_6.addWidget(self.add_members_label_frame_2, 0, Qt.AlignTop)

        self.settings_frame = QFrame(self.add_members_label_frame)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setMaximumSize(QSize(60, 60))
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.settings_frame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.settings_button = QPushButton(self.settings_frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setIcon(icon)

        self.verticalLayout_20.addWidget(self.settings_button)


        self.horizontalLayout_6.addWidget(self.settings_frame, 0, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.add_members_label_frame)

        self.add_members_body_frame = QFrame(self.add_members_page)
        self.add_members_body_frame.setObjectName(u"add_members_body_frame")
        self.add_members_body_frame.setFrameShape(QFrame.StyledPanel)
        self.add_members_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.add_members_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.add_members_input_frame = QFrame(self.add_members_body_frame)
        self.add_members_input_frame.setObjectName(u"add_members_input_frame")
        self.add_members_input_frame.setMaximumSize(QSize(250, 16777215))
        self.add_members_input_frame.setFrameShape(QFrame.StyledPanel)
        self.add_members_input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.add_members_input_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.add_members_groups_frame = QFrame(self.add_members_input_frame)
        self.add_members_groups_frame.setObjectName(u"add_members_groups_frame")
        self.add_members_groups_frame.setMaximumSize(QSize(250, 250))
        self.add_members_groups_frame.setFrameShape(QFrame.StyledPanel)
        self.add_members_groups_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.add_members_groups_frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.groups_label = QLabel(self.add_members_groups_frame)
        self.groups_label.setObjectName(u"groups_label")
        self.groups_label.setStyleSheet(u"color: rgb(50, 141, 189, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.groups_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.groups_label)

        self.add_members_groups_list = QScrollArea(self.add_members_groups_frame)
        self.add_members_groups_list.setObjectName(u"add_members_groups_list")
        self.add_members_groups_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 244, 206))
        self.add_members_groups_list.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_22.addWidget(self.add_members_groups_list)

        self.groups_from_label = QLabel(self.add_members_groups_frame)
        self.groups_from_label.setObjectName(u"groups_from_label")
        self.groups_from_label.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout_22.addWidget(self.groups_from_label)


        self.verticalLayout_21.addWidget(self.add_members_groups_frame)

        self.add_members_input_frame_2 = QFrame(self.add_members_input_frame)
        self.add_members_input_frame_2.setObjectName(u"add_members_input_frame_2")
        self.add_members_input_frame_2.setMaximumSize(QSize(250, 220))
        self.add_members_input_frame_2.setFrameShape(QFrame.StyledPanel)
        self.add_members_input_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.add_members_input_frame_2)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.add_members_choose_group_input_frame = QFrame(self.add_members_input_frame_2)
        self.add_members_choose_group_input_frame.setObjectName(u"add_members_choose_group_input_frame")
        self.add_members_choose_group_input_frame.setFrameShape(QFrame.StyledPanel)
        self.add_members_choose_group_input_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.add_members_choose_group_input_frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.choose_group_input_label = QLabel(self.add_members_choose_group_input_frame)
        self.choose_group_input_label.setObjectName(u"choose_group_input_label")
        self.choose_group_input_label.setMaximumSize(QSize(250, 50))
        self.choose_group_input_label.setFont(font)
        self.choose_group_input_label.setAutoFillBackground(False)
        self.choose_group_input_label.setStyleSheet(u"color: rgb(50, 141, 189, 255)")
        self.choose_group_input_label.setAlignment(Qt.AlignCenter)
        self.choose_group_input_label.setWordWrap(True)

        self.horizontalLayout_14.addWidget(self.choose_group_input_label)

        self.choose_group_input_2 = QLineEdit(self.add_members_choose_group_input_frame)
        self.choose_group_input_2.setObjectName(u"choose_group_input_2")
        self.choose_group_input_2.setMaximumSize(QSize(50, 16777215))
        self.choose_group_input_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.choose_group_input_2)


        self.verticalLayout_23.addWidget(self.add_members_choose_group_input_frame, 0, Qt.AlignTop)

        self.must_choose_group_frame = QFrame(self.add_members_input_frame_2)
        self.must_choose_group_frame.setObjectName(u"must_choose_group_frame")
        sizePolicy1.setHeightForWidth(self.must_choose_group_frame.sizePolicy().hasHeightForWidth())
        self.must_choose_group_frame.setSizePolicy(sizePolicy1)
        self.must_choose_group_frame.setFrameShape(QFrame.StyledPanel)
        self.must_choose_group_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.must_choose_group_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.choose_group_label_2 = QLabel(self.must_choose_group_frame)
        self.choose_group_label_2.setObjectName(u"choose_group_label_2")
        self.choose_group_label_2.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout_12.addWidget(self.choose_group_label_2, 0, Qt.AlignTop)


        self.verticalLayout_23.addWidget(self.must_choose_group_frame, 0, Qt.AlignRight)

        self.add_members_start_frame = QFrame(self.add_members_input_frame_2)
        self.add_members_start_frame.setObjectName(u"add_members_start_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add_members_start_frame.sizePolicy().hasHeightForWidth())
        self.add_members_start_frame.setSizePolicy(sizePolicy2)
        self.add_members_start_frame.setMaximumSize(QSize(16777215, 50))
        self.add_members_start_frame.setFrameShape(QFrame.StyledPanel)
        self.add_members_start_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.add_members_start_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, 0, 0, 0)
        self.choose_csv_button_2 = QPushButton(self.add_members_start_frame)
        self.choose_csv_button_2.setObjectName(u"choose_csv_button_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.choose_csv_button_2.sizePolicy().hasHeightForWidth())
        self.choose_csv_button_2.setSizePolicy(sizePolicy3)
        self.choose_csv_button_2.setMaximumSize(QSize(150, 40))
        self.choose_csv_button_2.setFont(font)
        self.choose_csv_button_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
"color: rgb(50, 141, 189, 255);\n"
"border-radius:20px;\n"
"border-color:rgb(39,39,39,255);\n"
"border-style:outset;\n"
"border-width:4px;")

        self.verticalLayout_6.addWidget(self.choose_csv_button_2)


        self.verticalLayout_23.addWidget(self.add_members_start_frame)


        self.verticalLayout_21.addWidget(self.add_members_input_frame_2)


        self.horizontalLayout_8.addWidget(self.add_members_input_frame)

        self.add_members_list_frame = QFrame(self.add_members_body_frame)
        self.add_members_list_frame.setObjectName(u"add_members_list_frame")
        self.add_members_list_frame.setFrameShape(QFrame.StyledPanel)
        self.add_members_list_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.add_members_list_frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.add_members_list = QTableWidget(self.add_members_list_frame)
        if (self.add_members_list.columnCount() < 2):
            self.add_members_list.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.add_members_list.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.add_members_list.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.add_members_list.setObjectName(u"add_members_list")
        self.add_members_list.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_26.addWidget(self.add_members_list)


        self.horizontalLayout_8.addWidget(self.add_members_list_frame)


        self.verticalLayout_19.addWidget(self.add_members_body_frame)

        self.stackedWidget.addWidget(self.add_members_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label.setText("")
        self.accounts_button.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.scrape_button.setText(QCoreApplication.translate("MainWindow", u"Scrape", None))
        self.add_members_button.setText(QCoreApplication.translate("MainWindow", u"Add Members", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.accounts_label.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.settings_button_3.setText("")
        self.phone_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone (e.g. +3598877548960)", None))
        self.api_id_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Api Id", None))
        self.api_hash_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Api Hash", None))
        self.accounts_danger_text.setText("")
        self.add_account_button.setText(QCoreApplication.translate("MainWindow", u"Add Account", None))
        self.accounts_list_label.setText(QCoreApplication.translate("MainWindow", u"Added Accounts", None))
        self.scrape_label.setText(QCoreApplication.translate("MainWindow", u"Scrape", None))
        self.scrape_settings_button_2.setText("")
        self.scraped_members_label.setText(QCoreApplication.translate("MainWindow", u"Scraped Members", None))
        ___qtablewidgetitem = self.scraped_members_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem1 = self.scraped_members_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.scraped_groups_label.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.scraped_groups_refresh_button.setText("")
        self.scraped_groups_from_label.setText(QCoreApplication.translate("MainWindow", u"*Groups are from first added account!", None))
        self.choose_group_label.setText(QCoreApplication.translate("MainWindow", u"Choose group to scrape members from.", None))
        self.choose_csv_button.setText(QCoreApplication.translate("MainWindow", u"Choose csv", None))
        self.add_members_labe.setText(QCoreApplication.translate("MainWindow", u"Add Memebrs", None))
        self.settings_button.setText("")
        self.groups_label.setText(QCoreApplication.translate("MainWindow", u"Groups", None))
        self.groups_from_label.setText(QCoreApplication.translate("MainWindow", u"*Groups are from first added account!", None))
        self.choose_group_input_label.setText(QCoreApplication.translate("MainWindow", u"Choose group to add members to", None))
        self.choose_group_label_2.setText("")
        self.choose_csv_button_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        ___qtablewidgetitem2 = self.add_members_list.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem3 = self.add_members_list.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Process", None));
    # retranslateUi

