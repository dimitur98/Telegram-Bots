from asyncio.windows_events import NULL
from logging import addLevelName, error
from sqlite3.dbapi2 import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCheckBox, QLabel, QLineEdit, QMainWindow, QWidget, QMessageBox
from telethon.errors.rpcerrorlist import PasswordHashInvalidError, PhoneCodeInvalidError, SessionPasswordNeededError
from telethon.tl.types import TypeUrlAuthResult
from add_to_group import *
from scraper import *
from db import *
from qtwidgets import AnimatedToggle
from py_toggle import *

RUNNING_ADDING_ERROR = "Add members is started. First stop it!"
OPEN_SETTINGS_ERROR = "Should wait until the process finish."
scraper = Scraper()
db = Db()
add_to_group = Add_To_Group()
class Ui_MainWindow(QMainWindow):
    self_main_window = None
    members_to_add = []
    selected_group = None
    stop_adding = False
    add_members_thread = None
    settings = None
    user_index_of_adding = None
    add_index = 0
    get_already_added_users = True
    selected_group_index_to_add = None
    reset_progresbar = False
    running_adding = False
    client_flood_errors = {}
    running_scraping = False
    MainWindow = None
    settings_open = False
    should_wait_seconds = 0
    codes = []
    passwords = []
    group_name = None
    threads = []
    scrape_users_for_every_account = False
    scraped_group_index = None
    users_from_csv = None

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi()
    def setupUi(self):   
        self.setObjectName("MainWindow")
        self.resize(940, 600)
        self.setMinimumSize(940,570)
        self.setMaximumSize(1024,700)
        icon = QtGui.QIcon()
        icon.addFile(u":/images/logo2.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
        "color: rgb(50, 141, 189, 255);")
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QFrame(self.sidebar)
        self.logo.setMinimumSize(QtCore.QSize(200, 0))
        self.logo.setMaximumSize(QtCore.QSize(300, 200))
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.logo)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo_label = QtWidgets.QLabel(self.logo)
        self.logo_label.setMinimumSize(QtCore.QSize(200, 0))
        self.logo_label.setMaximumSize(QtCore.QSize(16666, 16666))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/images/logo2.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.logo_label.setIndent(0)
        self.logo_label.setObjectName("logo_label")
        self.verticalLayout_2.addWidget(self.logo_label)
        self.verticalLayout.addWidget(self.logo)
        self.menu = QtWidgets.QFrame(self.sidebar)
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_3.setContentsMargins(25, 0, 10, 100)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.accounts_button = QtWidgets.QPushButton(self.menu)
        self.accounts_button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.accounts_button.setFont(font)
        self.accounts_button.setStyleSheet("border-radius:20px;\n"
                                           "border-color:rgb(39,39,39,255);\n"
                                           "border-style:outset;\n"
                                           "border-width:4px;")
        self.accounts_button.setIconSize(QtCore.QSize(100, 100))
        self.accounts_button.setAutoRepeatDelay(300)
        self.accounts_button.setObjectName("accounts_button")
        self.verticalLayout_3.addWidget(self.accounts_button)
        self.scrape_button = QtWidgets.QPushButton(self.menu)
        self.scrape_button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scrape_button.setFont(font)
        self.scrape_button.setStyleSheet("border-radius:20px;\n"
                                         "border-color:rgb(39,39,39,255);\n"
                                         "border-style:outset;\n"
                                         "border-width:4px;")
        self.scrape_button.setObjectName("scrape_button")
        self.verticalLayout_3.addWidget(self.scrape_button)
        self.add_members_button = QtWidgets.QPushButton(self.menu)
        self.add_members_button.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_members_button.setFont(font)
        self.add_members_button.setStyleSheet("border-radius:20px;\n"
                                              "border-color:rgb(39,39,39,255);\n"
                                              "border-style:outset;\n"
                                              "border-width:4px;")
        self.add_members_button.setObjectName("add_members_button")
        self.verticalLayout_3.addWidget(self.add_members_button)
        self.verticalLayout.addWidget(self.menu)
        self.horizontalLayout.addWidget(self.sidebar, 0, QtCore.Qt.AlignLeft)
        self.body = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.body)
        self.stackedWidget.setToolTip("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.accounts_page = QtWidgets.QWidget()
        self.accounts_page.setObjectName("accounts_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.accounts_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.accounts_label_frame = QtWidgets.QFrame(self.accounts_page)
        self.accounts_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accounts_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accounts_label_frame.setObjectName("accounts_label_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.accounts_label_frame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.accounts_label_frame_2 = QtWidgets.QFrame(self.accounts_label_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accounts_label_frame_2.sizePolicy().hasHeightForWidth())
        self.accounts_label_frame_2.setSizePolicy(sizePolicy)
        self.accounts_label_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accounts_label_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accounts_label_frame_2.setObjectName("accounts_label_frame_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.accounts_label_frame_2)
        self.horizontalLayout_12.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.accounts_label = QtWidgets.QLabel(self.accounts_label_frame_2)
        self.accounts_label.setMaximumSize(QtCore.QSize(200, 75))
        font = QtGui.QFont()
        font.setPointSize(29)
        self.accounts_label.setFont(font)
        self.accounts_label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.accounts_label.setObjectName("accounts_label")
        self.horizontalLayout_12.addWidget(self.accounts_label)
        self.horizontalLayout_11.addWidget(self.accounts_label_frame_2)
        self.accounts_settings_frame = QtWidgets.QFrame(self.accounts_label_frame)
        self.accounts_settings_frame.setMaximumSize(QtCore.QSize(60, 60))
        self.accounts_settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accounts_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accounts_settings_frame.setObjectName("accounts_settings_frame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.accounts_settings_frame)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.settings_button_3 = QtWidgets.QPushButton(self.accounts_settings_frame)
        self.settings_button_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/4954068.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button_3.setIcon(icon)
        self.settings_button_3.setObjectName("settings_button_3")
        self.settings_button_3.clicked.connect(self.settings_page_show)
        self.horizontalLayout_13.addWidget(self.settings_button_3)
        self.horizontalLayout_11.addWidget(self.accounts_settings_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.accounts_label_frame)
        self.account_body = QtWidgets.QFrame(self.accounts_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_body.sizePolicy().hasHeightForWidth())
        self.account_body.setSizePolicy(sizePolicy)
        self.account_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.account_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.account_body.setObjectName("account_body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.account_body)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.input_account = QtWidgets.QFrame(self.account_body)
        self.input_account.setMaximumSize(QtCore.QSize(400, 16777215))
        self.input_account.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_account.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_account.setObjectName("input_account")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.input_account)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.input_frame = QtWidgets.QFrame(self.input_account)
        self.input_frame.setMinimumSize(QtCore.QSize(100, 0))
        self.input_frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.input_frame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.input_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.phone_input = QtWidgets.QLineEdit(self.input_frame)
        self.phone_input.setMaximumSize(QtCore.QSize(300, 30))
        self.phone_input.setObjectName("phone_input")
        self.verticalLayout_8.addWidget(self.phone_input)
        self.api_id_input = QtWidgets.QLineEdit(self.input_frame)
        self.api_id_input.setMaximumSize(QtCore.QSize(300, 30))
        self.api_id_input.setObjectName("api_id_input")
        self.verticalLayout_8.addWidget(self.api_id_input)
        self.api_hash_input = QtWidgets.QLineEdit(self.input_frame)
        self.api_hash_input.setMaximumSize(QtCore.QSize(300, 30))
        self.api_hash_input.setObjectName("api_hash_input")
        self.verticalLayout_8.addWidget(self.api_hash_input)
        self.verticalLayout_7.addWidget(self.input_frame)
        self.accounts_danger_text = QtWidgets.QLabel(self.input_frame)
        self.accounts_danger_text.setObjectName(u"accounts_danger_text")
        self.accounts_danger_text.setMaximumSize(QtCore.QSize(200, 25))
        self.accounts_danger_text.setStyleSheet(u"color: rgb(255, 0, 0);font: 9pt \"MS Shell Dlg 2\";")
        self.accounts_danger_text.setWordWrap(True)
        self.verticalLayout_8.addWidget(self.accounts_danger_text)
        self.button_frame = QtWidgets.QFrame(self.input_account)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.button_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 185)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.add_account_button = QtWidgets.QPushButton(self.button_frame)
        self.add_account_button.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_account_button.setFont(font)
        self.add_account_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
                                              "color: rgb(50, 141, 189, 255);\n"
                                              "border-radius:20px;\n"
                                              "border-color:rgb(39,39,39,255);\n"
                                              "border-style:outset;\n"
                                              "border-width:4px;")
        self.add_account_button.setObjectName("add_account_button")
        self.verticalLayout_9.addWidget(self.add_account_button)
        self.verticalLayout_7.addWidget(self.button_frame)
        self.horizontalLayout_2.addWidget(self.input_account)
        self.accounts_list_frame = QtWidgets.QFrame(self.account_body)
        self.accounts_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accounts_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accounts_list_frame.setObjectName("accounts_list_frame")
        self.accounts_list_frame.setMaximumSize(QtCore.QSize(320, 16777215))
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.accounts_list_frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.accounts_list_label = QtWidgets.QLabel(self.accounts_list_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accounts_list_label.setFont(font)
        self.accounts_list_label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.accounts_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.accounts_list_label.setObjectName("accounts_list_label")
        self.verticalLayout_10.addWidget(self.accounts_list_label)
        self.accounts_list = QtWidgets.QListWidget(self.accounts_list_frame)
        self.accounts_list.setMaximumSize(QtCore.QSize(350, 16777215))
        self.accounts_list.setObjectName("accounts_list")
        self.e = RemoveAccountsEventFilter()
        self.accounts_list.installEventFilter(self.e)
        self.verticalLayout_10.addWidget(self.accounts_list)
        self.horizontalLayout_2.addWidget(self.accounts_list_frame)
        self.verticalLayout_5.addWidget(self.account_body)
        self.stackedWidget.addWidget(self.accounts_page)
        self.scrape_page = QtWidgets.QWidget()
        self.scrape_page.setObjectName("scrape_page")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrape_page)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrape_label_frame = QtWidgets.QFrame(self.scrape_page)
        self.scrape_label_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.scrape_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrape_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrape_label_frame.setObjectName("scrape_label_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scrape_label_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.scrape_label_frame_2 = QtWidgets.QFrame(self.scrape_label_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrape_label_frame_2.sizePolicy().hasHeightForWidth())
        self.scrape_label_frame_2.setSizePolicy(sizePolicy)
        self.scrape_label_frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrape_label_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrape_label_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrape_label_frame_2.setObjectName("scrape_label_frame_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.scrape_label_frame_2)
        self.horizontalLayout_10.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.scrape_label = QtWidgets.QLabel(self.scrape_label_frame_2)
        self.scrape_label.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(29)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.scrape_label.setFont(font)
        self.scrape_label.setStyleSheet("font: 29pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(50, 141, 189, 255);")
        self.scrape_label.setObjectName("scrape_label")
        self.horizontalLayout_10.addWidget(self.scrape_label)
        self.horizontalLayout_9.addWidget(self.scrape_label_frame_2, 0, QtCore.Qt.AlignTop)
        self.scrape_settings_frame = QtWidgets.QFrame(self.scrape_label_frame)
        self.scrape_settings_frame.setMaximumSize(QtCore.QSize(60, 30))
        self.scrape_settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrape_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrape_settings_frame.setObjectName("scrape_settings_frame")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.scrape_settings_frame)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.scrape_settings_button_2 = QtWidgets.QPushButton(self.scrape_settings_frame)
        self.scrape_settings_button_2.setText("")
        self.scrape_settings_button_2.setIcon(icon)
        self.scrape_settings_button_2.setObjectName("scrape_settings_button_2")
        self.scrape_settings_button_2.clicked.connect(self.settings_page_show)
        self.verticalLayout_27.addWidget(self.scrape_settings_button_2, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_9.addWidget(self.scrape_settings_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_11.addWidget(self.scrape_label_frame, 0, QtCore.Qt.AlignTop)
        self.scrape_body = QtWidgets.QFrame(self.scrape_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrape_body.sizePolicy().hasHeightForWidth())
        self.scrape_body.setSizePolicy(sizePolicy)
        self.scrape_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrape_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrape_body.setObjectName("scrape_body")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.scrape_body)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.scraped_members_frame = QtWidgets.QFrame(self.scrape_body)
        self.scraped_members_frame.setMaximumSize(QtCore.QSize(16777215, 500))
        self.scraped_members_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scraped_members_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scraped_members_frame.setObjectName("scraped_members_frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.scraped_members_frame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.scraped_members_label = QtWidgets.QLabel(self.scraped_members_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scraped_members_label.setFont(font)
        self.scraped_members_label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.scraped_members_label.setObjectName("scraped_members_label")
        self.verticalLayout_14.addWidget(self.scraped_members_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scraped_members_table = QtWidgets.QTableWidget(self.scraped_members_frame)
        self.scraped_members_table.setMaximumSize(QtCore.QSize(16777215, 500))
        self.scraped_members_table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed)
        self.scraped_members_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.scraped_members_table.setObjectName("scraped_members_table")
        self.scraped_members_table.setColumnCount(2)
        self.scraped_members_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.scraped_members_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.scraped_members_table.setHorizontalHeaderItem(1, item)
        self.scraped_members_table.horizontalHeader().setStretchLastSection(True)
        self.scraped_members_table.verticalHeader().setStretchLastSection(True)
        self.scraped_members_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalLayout_14.addWidget(self.scraped_members_table, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_13.addWidget(self.scraped_members_frame)
        self.scraped_input_frame = QtWidgets.QFrame(self.scrape_body)
        self.scraped_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scraped_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scraped_input_frame.setObjectName("scraped_input_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scraped_input_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.scrape_spinner = QtWidgets.QLabel(self.scraped_input_frame)
        # self.scrape_spinner.setAlignment(QtCore.Qt.AlignCenter)
        self.movie = QtGui.QMovie(":/gifs/scrape_spinner.gif")
        self.scrape_spinner.setMovie(self.movie)
        self.scrape_spinner.setAlignment(QtCore.Qt.AlignCenter)
        self.scrape_spinner.setHidden(True)
        self.horizontalLayout_3.addWidget(self.scrape_spinner, 0, QtCore.Qt.AlignHCenter)

        self.scraped_groups_frame = QtWidgets.QFrame(self.scraped_input_frame)
        self.scraped_groups_frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scraped_groups_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scraped_groups_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scraped_groups_frame.setObjectName("scraped_groups_frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scraped_groups_frame)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.scrape_groups_label_frame = QtWidgets.QFrame(self.scraped_groups_frame)
        self.scrape_groups_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrape_groups_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrape_groups_label_frame.setObjectName("scrape_groups_label_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrape_groups_label_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scraped_groups_label = QtWidgets.QLabel(self.scrape_groups_label_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scraped_groups_label.setFont(font)
        self.scraped_groups_label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.scraped_groups_label.setObjectName("scraped_groups_label")
        self.horizontalLayout_4.addWidget(self.scraped_groups_label)
        self.scraped_groups_refresh_button = QtWidgets.QPushButton(self.scrape_groups_label_frame)
        self.scraped_groups_refresh_button.setMaximumSize(QtCore.QSize(30, 20))
        self.scraped_groups_refresh_button.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.scraped_groups_refresh_button.setText("")
        self.scraped_groups_refresh_button.clicked.connect(self.load_groups_scrape_button)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons8-refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scraped_groups_refresh_button.setIcon(icon1)
        self.scraped_groups_refresh_button.setIconSize(QtCore.QSize(20, 20))
        self.scraped_groups_refresh_button.setObjectName("scraped_groups_refresh_button")
        self.horizontalLayout_4.addWidget(self.scraped_groups_refresh_button)
        self.verticalLayout_15.addWidget(self.scrape_groups_label_frame, 0, QtCore.Qt.AlignTop)
        self.scrape_group_list_frame = QtWidgets.QFrame(self.scraped_groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrape_group_list_frame.sizePolicy().hasHeightForWidth())
        self.scrape_group_list_frame.setSizePolicy(sizePolicy)
        self.scrape_group_list_frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.scrape_group_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrape_group_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrape_group_list_frame.setObjectName("scrape_group_list_frame")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.scrape_group_list_frame)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.scraped_groups_list = QtWidgets.QListWidget(self.scrape_group_list_frame)
        self.scraped_groups_list.setObjectName("scraped_groups_list")
        self.scraped_groups_list.setGeometry(QtCore.QRect(0, 0, 294, 216))
        self.scraped_groups_list.itemDoubleClicked.connect(self.scrape_member_by_double_click)
        self.verticalLayout_16.addWidget(self.scraped_groups_list)
        self.scrape_danger_text = QtWidgets.QLabel(self.scrape_group_list_frame)
        self.scrape_danger_text.setStyleSheet("color: rgb(255, 0, 0); font: 9pt \"MS Shell Dlg 2\";")
        self.scrape_danger_text.setObjectName("scrape_danger_text")
        self.scrape_danger_text.setWordWrap(True)
        self.verticalLayout_16.addWidget(self.scrape_danger_text)
        self.verticalLayout_15.addWidget(self.scrape_group_list_frame)
        self.horizontalLayout_3.addWidget(self.scraped_groups_frame)
        self.scraped_choose_input_frame = QtWidgets.QFrame(self.scraped_input_frame)
        self.scraped_choose_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scraped_choose_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scraped_choose_input_frame.setObjectName("scraped_choose_input_frame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.scraped_choose_input_frame)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.choose_group_frame = QtWidgets.QFrame(self.scraped_choose_input_frame)
        self.choose_group_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_group_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_group_frame.setObjectName("choose_group_frame")
        self.choose_group_frame.setMaximumSize(QtCore.QSize(500,16777215))
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.choose_group_frame)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.choose_group_label = QtWidgets.QLabel(self.choose_group_frame)
        self.choose_group_label.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose_group_label.setFont(font)
        self.choose_group_label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.choose_group_label.setTextFormat(QtCore.Qt.PlainText)
        self.choose_group_label.setScaledContents(False)
        self.choose_group_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_group_label.setWordWrap(True)
        self.choose_group_label.setObjectName("choose_group_label")
        self.verticalLayout_18.addWidget(self.choose_group_label)
        self.choose_group_input = QtWidgets.QLineEdit(self.choose_group_frame)
        self.choose_group_input.setMaximumSize(QtCore.QSize(50, 16777215))
        self.choose_group_input.setObjectName("choose_group_input")
        self.choose_group_input.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.choose_group_input.setFont(font)
        self.choose_group_input.returnPressed.connect(self.scrape_members_by_input)
        self.verticalLayout_18.addWidget(self.choose_group_input, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_17.addWidget(self.choose_group_frame,0,QtCore.Qt.AlignTop)
        self.line = QtWidgets.QFrame(self.scraped_choose_input_frame)
        self.line.setMaximumSize(QtCore.QSize(16777215, 10))
        self.line.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_17.addWidget(self.line)
        self.choose_csv_frame = QtWidgets.QFrame(self.scraped_choose_input_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_csv_frame.sizePolicy().hasHeightForWidth())
        self.choose_csv_frame.setSizePolicy(sizePolicy)
        self.choose_csv_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_csv_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_csv_frame.setObjectName("choose_csv_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.choose_csv_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.choose_csv_button = QtWidgets.QPushButton(self.choose_csv_frame)
        self.choose_csv_button.setMaximumSize(QtCore.QSize(130, 40))
        self.choose_csv_button.clicked.connect(self.open_csv_file)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.choose_csv_button.setFont(font)
        self.choose_csv_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
                                             "color: rgb(50, 141, 189, 255);\n"
                                             "border-radius:20px;\n"
                                             "border-color:rgb(39,39,39,255);\n"
                                             "border-style:outset;\n"
                                             "border-width:4px;")
        self.choose_csv_button.setObjectName("choose_csv_button")
        self.horizontalLayout_5.addWidget(self.choose_csv_button)
        self.verticalLayout_17.addWidget(self.choose_csv_frame)
        self.horizontalLayout_3.addWidget(self.scraped_choose_input_frame)
        self.verticalLayout_13.addWidget(self.scraped_input_frame)
        self.verticalLayout_11.addWidget(self.scrape_body)
        self.stackedWidget.addWidget(self.scrape_page)
        self.add_members_page = QtWidgets.QWidget()
        self.add_members_page.setObjectName("add_members_page")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.add_members_page)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.add_members_label_frame = QtWidgets.QFrame(self.add_members_page)
        self.add_members_label_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.add_members_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_label_frame.setObjectName("add_members_label_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.add_members_label_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_members_label_frame_2 = QtWidgets.QFrame(self.add_members_label_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_members_label_frame_2.sizePolicy().hasHeightForWidth())
        self.add_members_label_frame_2.setSizePolicy(sizePolicy)
        self.add_members_label_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_label_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_label_frame_2.setObjectName("add_members_label_frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.add_members_label_frame_2)
        self.horizontalLayout_7.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.add_members_labe = QtWidgets.QLabel(self.add_members_label_frame_2)
        self.add_members_labe.setMaximumSize(QtCore.QSize(300, 75))
        self.add_members_labe.setStyleSheet("font: 29pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(50, 141, 189, 255);")
        self.add_members_labe.setObjectName("add_members_labe")
        self.horizontalLayout_7.addWidget(self.add_members_labe)
        self.horizontalLayout_6.addWidget(self.add_members_label_frame_2, 0, QtCore.Qt.AlignTop)
        self.settings_frame = QtWidgets.QFrame(self.add_members_label_frame)
        self.settings_frame.setMaximumSize(QtCore.QSize(60, 60))
        self.settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_frame.setObjectName("settings_frame")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.settings_frame)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.settings_button = QtWidgets.QPushButton(self.settings_frame)
        self.settings_button.setText("")
        self.settings_button.setIcon(icon)
        self.settings_button.setObjectName("settings_button")
        self.settings_button.clicked.connect(self.settings_page_show)
        self.verticalLayout_20.addWidget(self.settings_button)
        self.horizontalLayout_6.addWidget(self.settings_frame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_19.addWidget(self.add_members_label_frame)
        self.add_members_body_frame = QtWidgets.QFrame(self.add_members_page)
        self.add_members_body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_body_frame.setObjectName("add_members_body_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.add_members_body_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.add_members_input_frame = QtWidgets.QFrame(self.add_members_body_frame)
        self.add_members_input_frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.add_members_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_input_frame.setObjectName("add_members_input_frame")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.add_members_input_frame)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.add_members_groups_frame = QtWidgets.QFrame(self.add_members_input_frame)
        self.add_members_groups_frame.setMaximumSize(QtCore.QSize(250, 250))
        self.add_members_groups_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_groups_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_groups_frame.setObjectName("add_members_groups_frame")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.add_members_groups_frame)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.add_members_input_label_frame = QtWidgets.QFrame(self.add_members_groups_frame)
        self.add_members_input_label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_input_label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_input_label_frame.setObjectName("add_members_input_label_frame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.add_members_input_label_frame)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.add_members_groups_label = QtWidgets.QLabel(self.add_members_input_label_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_members_groups_label.setFont(font)
        self.add_members_groups_label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.add_members_groups_label.setObjectName("add_members_groups_label")
        self.horizontalLayout_15.addWidget(self.add_members_groups_label)
        self.add_members_groups_refresh_button_2 = QtWidgets.QPushButton(self.add_members_input_label_frame)
        self.add_members_groups_refresh_button_2.setMaximumSize(QtCore.QSize(30, 20))
        self.add_members_groups_refresh_button_2.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.add_members_groups_refresh_button_2.setText("")
        self.add_members_groups_refresh_button_2.setIcon(icon1)
        self.add_members_groups_refresh_button_2.setIconSize(QtCore.QSize(20, 20))
        self.add_members_groups_refresh_button_2.setObjectName("add_members_groups_refresh_button_2")
        self.add_members_groups_refresh_button_2.clicked.connect(self.load_groups_add_members_button)
        self.horizontalLayout_15.addWidget(self.add_members_groups_refresh_button_2)
        self.verticalLayout_22.addWidget(self.add_members_input_label_frame, 0, QtCore.Qt.AlignTop)
        self.add_members_groups_rfame = QtWidgets.QFrame(self.add_members_groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_members_groups_rfame.sizePolicy().hasHeightForWidth())
        self.add_members_groups_rfame.setSizePolicy(sizePolicy)
        self.add_members_groups_rfame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_groups_rfame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_groups_rfame.setObjectName("add_members_groups_rfame")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.add_members_groups_rfame)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.add_members_groups_list = QtWidgets.QListWidget(self.add_members_groups_rfame)
        self.add_members_groups_list.setObjectName("add_members_groups_list")
        self.add_members_groups_list.itemDoubleClicked.connect(self.get_index_group_to_add_members_on_dclick)
        self.verticalLayout_24.addWidget(self.add_members_groups_list)
        self.add_members_danger_text = QtWidgets.QLabel(self.add_members_groups_rfame)
        self.add_members_danger_text.setStyleSheet("color: rgb(255, 0, 0);font: 9pt \"MS Shell Dlg 2\";")
        self.add_members_danger_text.setWordWrap(True)
        self.add_members_danger_text.setObjectName("add_members_danger_text")
        self.verticalLayout_24.addWidget(self.add_members_danger_text)
        self.verticalLayout_22.addWidget(self.add_members_groups_rfame)
        self.verticalLayout_21.addWidget(self.add_members_groups_frame)
        self.add_members_input_frame_2 = QtWidgets.QFrame(self.add_members_input_frame)
        self.add_members_input_frame_2.setMaximumSize(QtCore.QSize(250, 220))
        self.add_members_input_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_input_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_input_frame_2.setObjectName("add_members_input_frame_2")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.add_members_input_frame_2)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.add_members_choose_group_input_frame = QtWidgets.QFrame(self.add_members_input_frame_2)
        self.add_members_choose_group_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_choose_group_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_choose_group_input_frame.setObjectName("add_members_choose_group_input_frame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.add_members_choose_group_input_frame)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.choose_group_input_label = QtWidgets.QLabel(self.add_members_choose_group_input_frame)
        self.choose_group_input_label.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choose_group_input_label.setFont(font)
        self.choose_group_input_label.setAutoFillBackground(False)
        self.choose_group_input_label.setStyleSheet("color: rgb(50, 141, 189, 255)")
        self.choose_group_input_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_group_input_label.setWordWrap(True)
        self.choose_group_input_label.setObjectName("choose_group_input_label")
        self.horizontalLayout_14.addWidget(self.choose_group_input_label)
        self.choose_group_input_2 = QtWidgets.QLineEdit(self.add_members_choose_group_input_frame)
        self.choose_group_input_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.choose_group_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_group_input_2.setObjectName("choose_group_input_2")
        self.choose_group_input_2.setFont(font)
        self.horizontalLayout_14.addWidget(self.choose_group_input_2)
        self.verticalLayout_23.addWidget(self.add_members_choose_group_input_frame, 0, QtCore.Qt.AlignTop)
        self.adding_progressbar_frame = QtWidgets.QFrame(self.add_members_input_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adding_progressbar_frame.sizePolicy().hasHeightForWidth())
        self.adding_progressbar_frame.setSizePolicy(sizePolicy)
        self.adding_progressbar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adding_progressbar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adding_progressbar_frame.setObjectName("adding_progressbar_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.adding_progressbar_frame)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 50)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.progressbar_frame = QtWidgets.QFrame(self.adding_progressbar_frame)
        self.progressbar_frame.setObjectName("progressbar_frame")
        self.progressbar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progressbar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.progressbar_frame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.adding_progressbar = QtWidgets.QProgressBar(self.progressbar_frame)
        self.adding_progressbar.setObjectName("adding_progressbar")
        self.adding_progressbar.setStyleSheet("QProgressBar:horizontal {\n"
                                              "border: 1px solid gray;\n"
                                              "border-radius: 3px;\n"
                                              "background: white;\n"
                                              "padding: 1px;\n"
                                              "text-align: center;\n"
                                              "}\n"
                                              "QProgressBar::chunk:horizontal {\n"
                                              "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgb(50, 141, 189, 255), stop: 1 white);\n"
                                              "margin-right: 2px; /* space */\n"
                                              "width: 20px;\n"
                                              "})")
        self.adding_progressbar.setTextVisible(True)
        self.adding_progressbar.setHidden(True)
        self.verticalLayout_24.addWidget(self.adding_progressbar)
        self.verticalLayout_12.addWidget(self.progressbar_frame)
        self.counter_frame = QtWidgets.QFrame(self.adding_progressbar_frame)
        self.counter_frame.setObjectName("counter_frame")
        self.counter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.counter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.counter_frame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, -1, 0)
        self.counter_label = QtWidgets.QLabel(self.counter_frame)
        self.counter_label.setObjectName("counter_label")
        self.counter_label.setMaximumSize(QtCore.QSize(85,20))
        self.counter_label.setStyleSheet("color: rgb(50,141,189,255); font: 9pt\"MS Shell Dig 2\"")
        self.counter_label.setHidden(True)
        self.horizontalLayout_15.addWidget(self.counter_label)
        self.counter = QtWidgets.QLabel(self.counter_frame)
        self.counter.setObjectName("counter")
        self.counter.setMaximumSize(QtCore.QSize(16777215,20))
        self.counter.setStyleSheet("color: rgb(50,141,189,255); font: 9pt\"MS Shell Dig 2\"")
        self.counter.setHidden(True)
        self.horizontalLayout_15.addWidget(self.counter)
        self.verticalLayout_12.addWidget(self.counter_frame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_23.addWidget(self.adding_progressbar_frame)
        self.add_members_start_frame = QtWidgets.QFrame(self.add_members_input_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_members_start_frame.sizePolicy().hasHeightForWidth())
        self.add_members_start_frame.setSizePolicy(sizePolicy)
        self.add_members_start_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.add_members_start_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_start_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_start_frame.setObjectName("add_members_start_frame")
        self.verticalLayout_6 = QtWidgets.QHBoxLayout(self.add_members_start_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.start_button = QtWidgets.QPushButton(self.add_members_start_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
                                        "color: rgb(50, 141, 189, 255);\n"
                                        "border-radius:20px;\n"
                                        "border-color:rgb(39,39,39,255);\n"
                                        "border-style:outset;\n"
                                        "border-width:4px;")
        self.start_button.setObjectName("star_button")
        self.start_button.clicked.connect(self.get_index_group_to_add_members)
        self.verticalLayout_6.addWidget(self.start_button)

        self.pause_button = QtWidgets.QPushButton(self.add_members_start_frame)
        self.pause_button.setSizePolicy(sizePolicy)
        self.pause_button.setMaximumSize(QtCore.QSize(150, 40))
        self.pause_button.setFont(font)
        self.pause_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
                                        "color: rgb(50, 141, 189, 255);\n"
                                        "border-radius:20px;\n"
                                        "border-color:rgb(39,39,39,255);\n"
                                        "border-style:outset;\n"
                                        "border-width:4px;")
        self.pause_button.setObjectName("pause_button")
        self.pause_button.clicked.connect(self.pause_adding)
        self.verticalLayout_6.addWidget(self.pause_button)
        self.pause_button.setHidden(True)

        self.continue_button = QtWidgets.QPushButton(self.add_members_start_frame)
        self.continue_button.setSizePolicy(sizePolicy)
        self.continue_button.setMaximumSize(QtCore.QSize(150, 40))
        self.continue_button.setFont(font)
        self.continue_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
                                        "color: rgb(50, 141, 189, 255);\n"
                                        "border-radius:20px;\n"
                                        "border-color:rgb(39,39,39,255);\n"
                                        "border-style:outset;\n"
                                        "border-width:4px;")
        self.continue_button.setObjectName("continue_button")
        self.continue_button.clicked.connect(self.continue_adding)
        self.verticalLayout_6.addWidget(self.continue_button)
        self.continue_button.setHidden(True)

        self.stop_adding_button = QtWidgets.QPushButton(self.add_members_start_frame)
        self.stop_adding_button.setMaximumSize(QtCore.QSize(150, 40))
        self.stop_adding_button.setFont(font)
        self.stop_adding_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.039801, y1:0.023, x2:1, y2:1, stop:0 rgba(47, 47, 47, 255), stop:1 rgba(57, 57, 57, 255));\n"
                                              "color: rgb(50, 141, 189, 255);\n"
                                              "border-radius:20px;\n"
                                              "border-color:rgb(39,39,39,255);\n"
                                              "border-style:outset;\n"
                                              "border-width:4px;")
        self.stop_adding_button.setObjectName("stop_adding_button")
        self.stop_adding_button.clicked.connect(lambda x: self.stop_adding_members(show_text=True))
        self.verticalLayout_6.addWidget(self.stop_adding_button)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_23.addWidget(self.add_members_start_frame)
        self.verticalLayout_21.addWidget(self.add_members_input_frame_2)
        self.horizontalLayout_8.addWidget(self.add_members_input_frame)
        self.add_members_list_frame = QtWidgets.QFrame(self.add_members_body_frame)
        self.add_members_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_members_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_members_list_frame.setObjectName("add_members_list_frame")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.add_members_list_frame.setSizePolicy(sizePolicy)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.add_members_list_frame)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.add_members_table = QtWidgets.QTableWidget(self.add_members_list_frame)
        self.add_members_table.setObjectName("add_members_table")
        self.add_members_table.setMaximumSize(QtCore.QSize(500,16777215))
        self.add_members_table.setColumnCount(3)
        self.add_members_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.add_members_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.add_members_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.add_members_table.setHorizontalHeaderItem(2, item)
        self.add_members_table.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_26.addWidget(self.add_members_table)
        self.horizontalLayout_8.addWidget(self.add_members_list_frame)
        self.verticalLayout_19.addWidget(self.add_members_body_frame)
        self.stackedWidget.addWidget(self.add_members_page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.body)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        self.settings = Ui_Settings()
        Ui_MainWindow.self_main_window = self

        self.settings.setupUi()
        self.settings.setMaximumSize(QtCore.QSize(400, 300))
        self.stackedWidget.setCurrentIndex(0)
        self.add_account_button.clicked.connect(self.add_account)
        self.load_accounts_from_db()
        
        # self.load_settings()
        
        QtCore.QMetaObject.connectSlotsByName(self)
    def load_accounts_from_db(self):
        client_groups = db.get_all_accounts()

        if client_groups == None:
            return

        for account in client_groups:
            self.add_account(account["phone"], account["api_id"], account["api_hash"])

    def add_account_to_list(self,client,phone):
        add_to_group.set_client(client,phone)
        # check if db has main client
        settings = db.get_all_settings()

        if settings != []:
            settings = settings[0]
            if settings["main_account"] == "":
                db.update_settings(settings["id"],main_account=phone)

        db.insert_account(phone, client.api_id, client.api_hash)
        self.accounts_list_show()
    def accounts_list_show(self):
        index = 1
        self.accounts_list.clear()

        for account in add_to_group.client_groups.keys():
                new_item = QtWidgets.QListWidgetItem()
                font = QtGui.QFont()

                new_item.setText(f"{index}. {add_to_group.client_phone[account]}")
                new_item.setFont(font)
                new_item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.accounts_list.addItem(new_item)

                index += 1
        self.phone_input.setText("")
        self.api_id_input.setText("")
        self.api_hash_input.setText("")
        self.accounts_list.setStyleSheet('font: 12pt "MS Shell Dlg 2";')
        # self.accounts_list.setLayout(formLayout)
    def add_account(self, phone = None, api_id = None, api_hash = None):
        self.reset_danger_text(add_accounts=True)
        from_input = False
        if phone == None or api_id == None or api_hash == None:
            phone = self.phone_input.text().strip()
            api_id = self.api_id_input.text().strip()
            api_hash = self.api_hash_input.text().strip()
            from_input = True

        if phone == "" or api_id == "" or api_hash == "":
                self.accounts_danger_text.setText("*All fields are required.")
                return

        if db.if_account_exist(phone) and from_input:
            self.accounts_danger_text.setText("Account already added.")
            return

        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        client = loop.run_until_complete(add_to_group.client_initializer(api_id, api_hash, phone))
        if isinstance(client,tuple):
            # db.delete_account(api_id=api_id)

            self.setEnabled(False)
            code = Ui_Code(phone,client[0],client[1])
            code.show()
            self.codes.append(code)
        elif isinstance(client,str):
            self.accounts_danger_text.setText(client)
        else:
            self.add_account_to_list(client,phone)

    def settings_page_show(self):
        if self.running_scraping:
            self.scrape_danger_text.setText(OPEN_SETTINGS_ERROR)
            return
        if self.running_adding:
            self.add_members_danger_text.setText(OPEN_SETTINGS_ERROR)
            return
        self.settings.load_account_dropdown()
        self.settings.show()
        self.setEnabled(False)
        self.settings_open = True

    def load_groups_add_members_button(self):
        self.load_groups(add_members= True)
    def load_groups_scrape_button(self):
        self.load_groups(scrape = True)
    
    def load_groups(self,add_members = False, scrape = False):
        if add_members:
            self.add_members_groups_list.clear()
        if scrape:
            self.scraped_groups_list.clear()

        if add_to_group.client_groups == {}:
            return
        print("load groups main accoubnt:",add_to_group.client_phone[add_to_group.main_client])
        group_names = add_to_group.load_group_names(add_to_group.get_account_groups(main_client=True))

        if group_names == []:
            return
        for index, group_name in group_names.items():
            new_item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            new_item.setText(f"{index+1}. {group_name}")
            new_item.setFont(font)

            if add_members:
                self.add_members_groups_list.addItem(new_item)
            if scrape:
                self.scraped_groups_list.addItem(new_item)

    def scrape_members(self,group_index):
        try:
            settings = db.get_all_settings()[0]

            if group_index != self.scraped_group_index and bool(settings["mode"]):
                self.scrape_users_for_every_account = True
            else:
                self.scrape_users_for_every_account = False

            self.users_from_csv = False
            self.scraped_group_index = group_index
            self.thread = QtCore.QThread()
            self.worker = ScrapeMembersThread(group_index)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.start_scrape_spinner)
            self.thread.started.connect(self.worker.scrape_by_group_index)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.stop_scrape_spinner)
            self.worker.finished.connect(self.show_scraped_memebers)
            self.thread.start()
        except Exception as ex:
            print("scrape members error: ",ex)
    def scrape_members_by_input(self):
        if self.running_adding:
            self.scrape_danger_text.setText(RUNNING_ADDING_ERROR)
            return

        group_index = self.choose_group_input.text()
        if group_index == "":
            return
        self.scrape_members(group_index)
    def scrape_member_by_double_click(self,item):
        if self.running_adding:
            self.scrape_danger_text.setText(RUNNING_ADDING_ERROR)
            return

        group_name = item.text()
        group = group_name.split(".")
        group_index = group[0]
        self.group_name = group[1]
        self.scrape_members(group_index)
    def show_scraped_memebers(self):
        if self.members_to_add == []:
            return

        self.stop_adding_members(show_text=False,reset_progressbar=False)
        self.scraped_members_table.setRowCount(len(self.members_to_add))
        i = 0

        for user in self.members_to_add:
            self.scraped_members_table.setItem(i,0,QtWidgets.QTableWidgetItem(user["username"]))
            self.scraped_members_table.setItem(i,1,QtWidgets.QTableWidgetItem(user["name"]))
            i += 1
    def scrape_users_for_every_account_func(self, is_continue):
        try:
            if self.group_name == None:
                return
            self.running_scraping = True
            self.thread = QtCore.QThread()
            self.worker = ScrapeMembersThread(group_name=self.group_name, is_continue = is_continue)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.scrape_by_group_name)
            self.worker.finished_2.connect(self.thread.terminate)
            self.worker.finished_2.connect(self.scrape_by_group_name_finished)
            self.thread.start()
            self.threads.append(self.thread)
            self.add_members_danger_text.setText("Should wait some time until users are scrapped for every account!")
        except Exception as ex:
            print("every account scrape error: ",ex)

    def start_scrape_spinner(self):
        self.running_scraping = True
        self.scraped_choose_input_frame.hide()
        self.scraped_groups_frame.hide()
        self.scrape_spinner.setHidden(False)
        self.movie.start()
    def stop_scrape_spinner(self):
        self.running_scraping = False
        self.reset_danger_text(add_members=True)
        self.scraped_choose_input_frame.show()
        self.scraped_groups_frame.show()
        self.scrape_spinner.setHidden(True)
        self.movie.stop()
    def scrape_by_group_name_finished(self, is_continue):
        print("in finished scrape:",is_continue)
        self.running_scraping = False
        self.reset_danger_text(add_members=True)
        self.scrape_users_for_every_account = False
        self.add_members(skip_scrape=True,is_continue=is_continue)

    def open_csv_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(
            caption="Choose .csv file to get people from.",
            filter = "Data file (*.csv)"
        )
        file_root = file[0]
        if file_root == "":
            return
            
        self.users_from_csv = True
        Ui_MainWindow.members_to_add = add_to_group.read_file(file_root)
        self.show_scraped_memebers()

    def get_index_group_to_add_members(self):
        if self.running_adding:
            self.add_members_danger_text.setText(RUNNING_ADDING_ERROR)
            return

        self.stop_adding = False
        group_index = self.choose_group_input_2.text()
        if group_index == '':
            self.add_members_danger_text.setText("Choose group!")
            return
        self.reset_danger_text(add_members=True)
        self.add_members(group_index)
    def get_index_group_to_add_members_on_dclick(self, item):
        if self.running_adding:
            self.add_members_danger_text.setText(RUNNING_ADDING_ERROR)
            return

        self.stop_adding = False
        group_name = item.text()
        group_index = group_name.split(".")[0]
        self.reset_danger_text(add_members=True)
        self.add_members(group_index)
    def add_members(self, group_index = None, is_continue = False, skip_scrape = False):
        settings = db.get_all_settings()[0]

        if self.running_scraping:
            self.add_members_danger_text.setText("Users are scraping now. Please wait!")
            return

        if self.members_to_add == []:
            self.add_members_danger_text.setText("There are no uesers for adding.")
            return

        if self.users_from_csv and bool(settings["mode"]):
            self.add_members_danger_text.setText("You can't add users by id when they are from .csv file.")
            return

        if group_index == None:
            group_index = self.selected_group_index_to_add
        else:
            if self.selected_group != group_index:
                self.set_reset_progresbar()

            self.selected_group_index_to_add = group_index

        print("mode in start thread: ",bool(settings["mode"]))
        if bool(settings["mode"]) and (self.scrape_users_for_every_account or not skip_scrape):
            print("in if for mode from start thread")
            self.scrape_users_for_every_account_func(is_continue)
            return

        if self.reset_progresbar:
            self.set_reset_progresbar()
        else:
            self.reset_progresbar = False

        try:
            self.selected_group = add_to_group.get_account_groups(main_client=True,group_index = int(group_index)-1)

            if self.get_already_added_users:
                print("get already")
                add_to_group.get_already_added_users(self.selected_group)

            # Set up thread
            self.thread = QtCore.QThread()
            self.worker = AddMembersThread(is_continue)
            self.add_members_thread = self.worker
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.update_progress.connect(self.update_progressbar)
            self.worker.update_counter.connect(self.update_counter)
            self.worker.reached_limit.connect(self.reached_limit)
            self.worker.no_accounts.connect(self.no_accounts_left)
            self.worker.finished.connect(self.thread.terminate)
            self.worker.finished.connect(self.on_thread_quit)
            self.thread.start()
            self.threads.append(self.thread)
            # Set up progressbar
            self.adding_progressbar.setMinimum(0)
            self.adding_progressbar.setMaximum(len(self.members_to_add))
            self.adding_progressbar.setHidden(False)
            self.counter_label.setHidden(False)
            self.counter.setHidden(False)

            # Buttons
            self.start_button.setHidden(True)
            self.pause_button.setHidden(False)
            self.continue_button.setHidden(True)
            self.add_members_choose_group_input_frame.setHidden(True)

            self.reset_danger_text(add_members=True)

        except Error as ex:
            print("add users in main error:",ex)
    def on_thread_quit(self):
        self.pause_button.setEnabled(True)
        self.start_button.setEnabled(True)
        self.continue_button.setEnabled(True)
        self.add_members_thread = None
        self.reset_danger_text(add_members=True)
    def reached_limit(self):
        self.add_members_danger_text.setText("Users add limit has been reached")
        self.continue_button.setHidden(True)
        self.start_button.setEnabled(False)
        self.start_button.setHidden(False)
        self.pause_button.setHidden(True)
        self.add_members_thread = None
    def no_accounts_left(self):
        self.continue_button.setHidden(True)
        self.start_button.setEnabled(False)
        self.start_button.setHidden(False)
        self.pause_button.setHidden(True)
        self.add_members_danger_text.setText("No client_groups left! All of them banned! Please wait some time!")
        self.add_members_thread = None
    
    def pause_adding(self):
        if self.add_members_thread == None:
            return
        self.add_members_thread.pause_adding_members()
        self.pause_button.setHidden(True)
        self.continue_button.setEnabled(False)
        self.continue_button.setHidden(False)
        self.get_already_added_users = False
        self.reset_danger_text(add_members= True,scrape= True)
        self.add_members_danger_text.setText(f"Paused! Should wait {self.should_wait_seconds} secs.")
    def continue_adding(self):
        self.reset_danger_text(add_members=True)
        self.add_members(is_continue=True, skip_scrape=True)
    def stop_adding_members(self, show_text = True, reset_progressbar = True):
        self.get_already_added_users = True
        self.continue_button.setHidden(True)
        self.start_button.setEnabled(False)
        self.start_button.setHidden(False)
        self.pause_button.setHidden(True)
        self.add_members_choose_group_input_frame.setHidden(False)

        if reset_progressbar:
            self.reset_progresbar = True

        self.reset_danger_text(add_members= True,scrape= True)

        if show_text:
            text = "Stopped!"

            if self.should_wait_seconds != 0 and self.running_adding:
                text += f"Should wait {self.should_wait_seconds} secs."

            self.add_members_danger_text.setText(text)

        if self.add_members_thread != None:
            self.add_members_thread.stop_adding_members()

    def update_progressbar(self):
        value = self.adding_progressbar.value() + 1
        self.adding_progressbar.setValue(value)
    def update_counter(self):
        self.counter.setText(str(int(self.counter.text()) + 1))
    def set_reset_progresbar(self):
        self.adding_progressbar.setValue(0)
        self.add_members_table.setRowCount(0)
        self.counter.setText("0")
        self.add_index = 0
    def reset_danger_text(self,add_members = False, scrape = False, add_accounts = False):
        if add_members:
            self.add_members_danger_text.setText("")
        if scrape:
            self.scrape_danger_text.setText("")
        if add_accounts:
            self.accounts_danger_text.setText("")
    def closeEvent(self,event):
        if self.settings_open:
            event.ignore()
            return 

        result = QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QMessageBox.Yes| QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Add Members Bot"))
        self.accounts_button.setText(_translate("self", "Accounts"))
        self.accounts_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.accounts_page))
        self.scrape_button.setText(_translate("self", "Scrape"))
        self.scrape_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.scrape_page))
        self.scrape_button.clicked.connect(self.load_groups_scrape_button, QtCore.Qt.QueuedConnection)
        self.add_members_button.setText(_translate("self", "Add Members"))
        self.add_members_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add_members_page))
        self.add_members_button.clicked.connect(self.load_groups_add_members_button)
        self.accounts_label.setText(_translate("self", "Accounts"))
        self.phone_input.setPlaceholderText(_translate("self", "Phone (e.g. +3598877548960)"))
        self.api_id_input.setPlaceholderText(_translate("self", "Api Id"))
        self.api_hash_input.setPlaceholderText(_translate("self", "Api Hash"))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.api_id_input.setFont(font)
        self.api_hash_input.setFont(font)
        self.phone_input.setFont(font)
        self.accounts_danger_text.setText("")
        self.add_account_button.setText(_translate("self", "Add Account"))
        self.accounts_list_label.setText(_translate("self", "Added Accounts"))
        self.scrape_label.setText(_translate("self", "Scrape"))
        self.scraped_members_label.setText(_translate("self", "Scraped Members"))
        item = self.scraped_members_table.horizontalHeaderItem(0)
        item.setText(_translate("self", "Username"))
        item = self.scraped_members_table.horizontalHeaderItem(1)
        item.setText(_translate("self", "Name"))
        self.scraped_groups_label.setText(_translate("self", "Groups"))
        self.choose_group_label.setText(_translate("self", "Choose group to scrape members from."))
        self.choose_csv_button.setText(_translate("self", "Choose csv"))
        self.add_members_labe.setText(_translate("self", "Add Memebrs"))
        self.add_members_groups_label.setText(_translate("self", "Groups"))
        self.choose_group_input_label.setText(_translate("self", "Choose group to add members to"))
        self.counter_label.setText(_translate("self", "Ädded users: "))
        self.start_button.setText(_translate("self", "Start"))
        self.pause_button.setText(_translate("self", "Pause"))
        self.continue_button.setText(_translate("self", "Continue"))
        self.stop_adding_button.setText(_translate("self", "Stop"))
        item = self.add_members_table.horizontalHeaderItem(0)
        item.setText(_translate("self", "Username"))
        item = self.add_members_table.horizontalHeaderItem(1)
        item.setText(_translate("self", "Account"))
        item = self.add_members_table.horizontalHeaderItem(2)
        item.setText(_translate("self", "Process"))
import resources_rc
class ScrapeMembersThread(QtCore.QThread):
    finished = QtCore.pyqtSignal()
    finished_2 = pyqtSignal(bool)
    loop = None

    def __init__(self,group_index = None, group_name = None,is_continue = None) -> None:
        super().__init__()
        self.loop = self.get_or_create_eventloop()
        self.group_index = group_index
        self.group_name = group_name
        self.is_continue = is_continue

    def get_or_create_eventloop(self):
        try:
            return asyncio.get_event_loop()
        except RuntimeError as ex:
            if "There is no current event loop in thread" in str(ex):
                loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

    def scrape_by_group_index(self):
        try:
            if self.group_index == "" or self.group_index == None:
                return

            asyncio.set_event_loop(self.loop)

            group = add_to_group.get_account_groups(main_client=True, group_index=int(self.group_index)-1)
            scraped_members = self.loop.run_until_complete(scraper.scrape_members(add_to_group.main_client, group))

            if isinstance(scraped_members, list):
                Ui_MainWindow.self_main_window.members_to_add  = scraped_members
            else:
                Ui_MainWindow.self_main_window.scrape_danger_text.setText(scraped_members)
        except Exception as e:
            print("scrape by group index error:",e)

        self.finished.emit()

    def scrape_by_group_name(self):
        try:
            print("start")
            if self.group_name == "" or self.group_name == None:
                return
            
            asyncio.set_event_loop(self.loop)

            for client,groups in add_to_group.client_groups.items():
                if client == add_to_group.main_client:
                    add_to_group.client_users[client] = Ui_MainWindow.self_main_window.members_to_add
                    continue
                print(f"groups from {add_to_group.client_phone[client]}: ",groups)
                # TO DO first or default doesnt work properly and set event loop too
                group = [x for x in groups if x.title == self.group_name.strip()]
                print("group: ",group)
                if group == []:
                    print("continue for:  ",add_to_group.client_phone[client])
                    continue

                scraped_members = self.loop.run_until_complete(scraper.scrape_members(client, group[0]))

                if isinstance(scraped_members, list):
                    add_to_group.client_users[client] = scraped_members
                else:
                    Ui_MainWindow.self_main_window.add_members_danger_text.setText(f"{add_to_group.client_phone[client]}: {scraped_members}")

        except Exception as e:
            print("scrape for client: ",e)

        self.finished_2.emit(self.is_continue)

class AddMembersThread(QtCore.QThread):
    update_progress = QtCore.pyqtSignal()
    update_counter = QtCore.pyqtSignal()
    reached_limit = QtCore.pyqtSignal()
    no_accounts = QtCore.pyqtSignal() 
    finished = QtCore.pyqtSignal()
    loop = None
    stop_adding = False

    def __init__(self,is_continue) -> None:
        super().__init__()
        self.loop = self.get_or_create_eventloop()
        self.is_continue = is_continue
    def get_or_create_eventloop(self):
        try:
            return asyncio.get_event_loop()
        except RuntimeError as ex:
            if "There is no current event loop in thread" in str(ex):
                loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return asyncio.get_event_loop()

    def run(self):
        Ui_MainWindow.self_main_window.running_adding = True
        Ui_MainWindow.self_main_window.adding_progressbar.setStyleSheet("QProgressBar:horizontal {\n"
                                                                        "border: 1px solid gray;\n"
                                                                        "border-radius: 3px;\n"
                                                                        "background: white;\n"
                                                                        "padding: 1px;\n"
                                                                        "text-align: center;\n"
                                                                        "font-size: 15px;\n"
                                                                        "}\n"
                                                                        "QProgressBar::chunk:horizontal {\n"
                                                                        "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgb(50, 141, 189, 255), stop: 1 white);\n"
                                                                        "margin-right: 2px; /* space */\n"
                                                                        "width: 10px;\n"
                                                                        "})")
        try:
            asyncio.set_event_loop(self.loop)
            self.loop.run_until_complete(self.add())
        except Exception as e:
            Ui_MainWindow.self_main_window.running_adding = False
            Ui_MainWindow.self_main_window.add_members_danger_text.setText("Error occured!")
            Ui_MainWindow.self_main_window.stop_adding_members()
            self.finished.emit()
            print("loop:",e)
    async def add(self):
        settings = db.get_all_settings()[0]
        print("is continue:",self.is_continue)

        clients = list(add_to_group.client_phone.keys())
        client_flood = {i : False for i in clients}

        if self.is_continue:
            index = Ui_MainWindow.self_main_window.add_index + settings["add_users_start_index"]-1
            i = Ui_MainWindow.self_main_window.add_index
            print("index in continue:",index)
            print("i in continue:",i)
        else:
            add_to_group.current_client = add_to_group.main_client
            index = settings["add_users_start_index"]-1
            i = 0
            print("index not continue:",index)
            print("i not continue:",i)

        table = Ui_MainWindow.self_main_window.add_members_table
        reqests_counter = 1
        added_counter = 0
        for user in Ui_MainWindow.self_main_window.members_to_add[index:]:
            if client_flood[add_to_group.current_client]:
                if not self.change_flooded_client(client_flood):
                    Ui_MainWindow.self_main_window.add_members_danger_text.setText("All accounts got flood error.")
                    break

            exclude = False
            add = True
            print("user from main: ",user)
            if reqests_counter % settings["users_per_batch"] == 0:
                Ui_MainWindow.self_main_window.should_wait_seconds = settings["users_batches_interval"]
                await asyncio.sleep(settings["users_batches_interval"])

            Ui_MainWindow.self_main_window.should_wait_seconds = settings["users_add_interval"]

            print("if stop adding: ",self.stop_adding)
            if self.stop_adding:
                Ui_MainWindow.self_main_window.running_adding = False
                break
            proccess = None
            print("mode in add thread before if:",bool(settings["mode"]))
            if bool(settings["mode"]):
                print("in if for mode")
                user_by_client = add_to_group.get_user_by_client(user["id"])
                print("user_by_client:",user_by_client)

                if user_by_client == None:
                    add = False
                    proccess = ACCOUNT_NOT_IN_GROUP
                else:
                    user = user_by_client
            
            if add:
                proccess = await add_to_group.add_members(user, Ui_MainWindow.self_main_window.selected_group.title)

            table.insertRow(i)
            table.setItem(i,0,QtWidgets.QTableWidgetItem(user["name"]))
            table.setItem(i,1, QtWidgets.QTableWidgetItem(add_to_group.client_phone[add_to_group.current_client]))
            table.setItem(i,2,QtWidgets.QTableWidgetItem(proccess))
            table.selectRow(i)
            i+=1

            if proccess == SUCCESSFULL_ADDED:
                self.update_counter.emit()
                added_counter += 1

            self.update_progress.emit()

            print("added counter: ",added_counter)
            print("users add limit: ",settings["users_limit"])
            print("limit exceeded:",added_counter == settings["users_limit"])
            if added_counter == settings["users_limit"]:
                Ui_MainWindow.self_main_window.running_adding = False
                self.reached_limit.emit()
                break

            await asyncio.sleep(settings["users_add_interval"])

            # add +1 to flood error of the current client
            # if current client has 3 flood errors in a row it is excluded from the client list for adding
            # if flood errors of the client are not in a row they don't count
            if proccess == FLOOD_ERROR:
                if add_to_group.current_client in Ui_MainWindow.self_main_window.client_flood_errors:
                   Ui_MainWindow.self_main_window.client_flood_errors[add_to_group.current_client] +=1
                else:
                   Ui_MainWindow.self_main_window.client_flood_errors[add_to_group.current_client] = 1

                if Ui_MainWindow.self_main_window.client_flood_errors[add_to_group.current_client] == 3:
                    exclude = True
            else:
                Ui_MainWindow.self_main_window.client_flood_errors[add_to_group.current_client] = 0

            if proccess != ALREADY_ADDED:
                add_to_group.change_client()
                reqests_counter += 1
            
            if exclude:
                client_flood[add_to_group.current_client] = True

            print("no groups if: ",add_to_group.client_groups == {})
            if add_to_group.client_groups == {}:
                Ui_MainWindow.self_main_window.running_adding = False
                self.no_accounts.emit()
                break
        Ui_MainWindow.self_main_window.add_index = i

        if Ui_MainWindow.self_main_window.add_index == len(Ui_MainWindow.members_to_add)-1:
            Ui_MainWindow.self_main_window.add_index = 0

        self.finished.emit()
    def change_flooded_client(self,client_flood):
        add_to_group.change_client()

        if client_flood[add_to_group.current_client]:
            floods = list(client_flood.values())
            if not any(False in x for x in floods):
                return False

            self.change_flooded_client(client_flood)
        else:
            return True
    def pause_adding_members(self):
        self.interrupt_adding()
    def stop_adding_members(self):
        Ui_MainWindow.self_main_window.add_index = 0
        self.interrupt_adding()
    def interrupt_adding(self):
        self.stop_adding = True
        Ui_MainWindow.self_main_window.adding_progressbar.setStyleSheet("QProgressBar:horizontal {\n"
                                                                        "border: 1px solid gray;\n"
                                                                        "border-radius: 3px;\n"
                                                                        "background: white;\n"
                                                                        "padding: 1px;\n"
                                                                        "text-align: center;\n"
                                                                        "font-size: 15px;\n"
                                                                        "}\n"
                                                                        "QProgressBar::chunk:horizontal {\n"
                                                                        "background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);\n"
                                                                        "margin-right: 2px; /* space */\n"
                                                                        "width: 10px;\n"
                                                                        "})")

class Ui_Code(QWidget):
    code = None
    ui_password = None
    def __init__(self,phone, client, phone_code_hash) -> None:
        super(QWidget,self).__init__()
        self.phone = phone
        self.client = client
        self.phone_code_hash = phone_code_hash
        self.setupUi()
    def setupUi(self):
        self.ui_password = Ui_Password(self.phone,self.client)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setObjectName("self")
        self.resize(300, 145)
        self.setMinimumSize(300,102)
        self.setMaximumSize(300,102)
        icon = QtGui.QIcon()
        icon.addFile(u":/images/logo2.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.code_input = QtWidgets.QLineEdit(self.frame)
        self.code_input.setObjectName("code_input")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.code_input.setFont(font)
        self.verticalLayout_2.addWidget(self.code_input)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignVCenter)
        self.code_input.returnPressed.connect(self.send_code)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    def enable_main(self):
        show_main = True
        for code in Ui_MainWindow.self_main_window.codes:
            if code.isVisible():
                show_main = False
        for password in Ui_MainWindow.self_main_window.passwords:
            if password.isVisible():
                show_main = False
            
            
        if show_main:
            Ui_MainWindow.self_main_window.setEnabled(show_main)
    def send_code(self):
        has_not_password = True
        self.code = self.code_input.text()
        if self.code == "":
            return
        try:
            self.client.sign_in(self.phone,self.code, phone_code_hash= self.phone_code_hash.phone_code_hash)
        except SessionPasswordNeededError:
            has_not_password= False
            Ui_MainWindow.self_main_window.passwords.append(self.ui_password)
            self.ui_password.show()
        except PhoneCodeInvalidError:
            Ui_MainWindow.self_main_window.accounts_danger_text.setText("Wrong code!")
            self.code_input.setText("")
            self.close()
            self.enable_main()
            return

        if has_not_password:
            if self.client.is_user_authorized():
                Ui_MainWindow.self_main_window.add_account_to_list(self.client,self.phone)
        self.close()
        self.enable_main()
    def closeEvent(self, event):
        self.enable_main()
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Code"))
        self.label.setText(_translate("self", f"Enter The Code For '{self.phone}': "))

class Ui_Password(QWidget):
    def __init__(self,phone,client, )-> None:
        super(QWidget,self).__init__()
        self.client = client
        self.phone = phone
        self.setupUi()
    def setupUi(self):
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setObjectName("self")
        self.resize(300, 102)
        self.setMinimumSize(300,102)
        self.setMaximumSize(300,102)
        icon = QtGui.QIcon()
        icon.addFile(u":/images/logo2.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(50, 141, 189, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.password_input = QtWidgets.QLineEdit(self.frame)
        self.password_input.setObjectName("password")
        self.password_input.setEchoMode(QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password_input.setFont(font)
        self.password_input.returnPressed.connect(self.get_password)
        self.verticalLayout_2.addWidget(self.password_input)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    def enable_main(self):
        show_main = True
        for password in Ui_MainWindow.self_main_window.passwords:
            if password.isVisible():
                show_main = False
            
        if show_main:
            Ui_MainWindow.self_main_window.setEnabled(show_main)

    def get_password(self):
        password = self.password_input.text()

        if password == "":
            return
            
        try:
            self.client.sign_in(password = str(password))
        except PasswordHashInvalidError:
            Ui_MainWindow.self_main_window.accounts_danger_text.setText("Wrong password!")
            self.password_input.setText("")
            self.close()
            self.enable_main()
            return

        Ui_MainWindow.self_main_window.add_account_to_list(self.client,self.phone)
        self.close()
        self.enable_main()
    def closeEvent(self, event):
       self.enable_main()
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Password"))
        self.label.setText(_translate("self", f"Enter Password For '{self.phone}': "))
class RemoveAccountsEventFilter(QtCore.QObject):
    def __init__(self):
         super(RemoveAccountsEventFilter, self).__init__()
    def eventFilter(self,source,event):
        if event.type() == QtCore.QEvent.ContextMenu and source is Ui_MainWindow.self_main_window.accounts_list:
            menu = QtWidgets.QMenu()
            menu.addAction("Remove")

            if menu.exec_(event.globalPos()):
                # Get client for remove
                try:
                    selected_client = source.itemAt(event.pos())
                    key_list = list(add_to_group.client_phone.keys())
                    val_list = list(add_to_group.client_phone.values())
                    client_phone = selected_client.text().split(" ")[1]
                    client_index = val_list.index(client_phone)
                    client = key_list[client_index]

                    # Disconnect client
                    client.log_out()
                    # client.disconnect()

                    # Remove from storage
                    del add_to_group.client_groups[client]
                    del add_to_group.client_phone[client]

                    # Delete from db
                    account = db.get_account_by_phone(client_phone)
                    if account != []:
                        db.delete_account(id= account[0]["id"])
                    # Remove from settings
                    settings = db.get_all_settings()
                    if settings != []:
                        db.update_settings(settings[0]["id"],main_account="")
                    # Check if is main
                    if add_to_group.is_client_main(client):
                        if add_to_group.client_phone != {}:
                            add_to_group.set_main_client(client = list(add_to_group.client_phone.keys())[0])
                        else:
                            add_to_group.set_main_client()

                    Ui_MainWindow.accounts_list_show(Ui_MainWindow.self_main_window)
                except:
                    Ui_MainWindow.self_main_window.accounts_danger_text.setText("Problem occured. Try again later.")
            return True
        
        return super().eventFilter(source,event)

class Ui_Settings(QtWidgets.QWidget):
    USERS_PER_BATCH = 20
    USERS_BATCHES_INTERVAL=60
    USERS_ADD_INTERVAL = 10
    USERS_LIMIT = None
    ADD_USERS_START_INDEX = 1
    id = None
    reload_groups = False
    detect_dropdown = True

    def __init__(self, ):
        super(QWidget,self).__init__()
    def setupUi(self):
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.setObjectName("Ui_Settings")
        self.resize(318, 300)
        icon = QtGui.QIcon()
        icon.addFile(u":/images/logo2.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings_body_frame = QtWidgets.QFrame(self)
        self.settings_body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_body_frame.setObjectName("settings_body_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.settings_body_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.settings_menu = QtWidgets.QTabWidget(self.settings_body_frame)
        self.settings_menu.setObjectName("settings_menu")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.settings_menu.setFont(font)
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Settings)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.Settings)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.only_megagroups_checkbox = QtWidgets.QCheckBox(self.frame)
        self.only_megagroups_checkbox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.only_megagroups_checkbox.setObjectName("only_megagroups_checkbox")
        self.only_megagroups_checkbox.setFont(font)
        self.only_megagroups_checkbox.setChecked(True)
        self.only_megagroups_checkbox.stateChanged.connect(self.set_only_megagroups)
        self.verticalLayout_5.addWidget(self.only_megagroups_checkbox)
        self.skip_added_users_checkbox = QtWidgets.QCheckBox(self.frame)
        self.skip_added_users_checkbox.setObjectName("skip_added_users_checkbox")
        self.skip_added_users_checkbox.setChecked(True)
        self.skip_added_users_checkbox.setFont(font)
        self.skip_added_users_checkbox.stateChanged.connect(self.set_skip_added_users)
        self.verticalLayout_5.addWidget(self.skip_added_users_checkbox)
        self.automatic_settings = QtWidgets.QCheckBox(self.frame)
        self.automatic_settings.setObjectName("automatic_settings")
        self.automatic_settings.stateChanged.connect(self.set_automatic_settings)
        self.automatic_settings.setFont(font)
        self.verticalLayout_5.addWidget(self.automatic_settings)
        self.recently_active_checkbox = QtWidgets.QCheckBox(self.frame)
        self.recently_active_checkbox.setObjectName("recently_active_checkbox")
        self.recently_active_checkbox.setChecked(True)
        self.recently_active_checkbox.stateChanged.connect(self.set_recently_active_users)
        self.recently_active_checkbox.setFont(font)
        self.verticalLayout_5.addWidget(self.recently_active_checkbox)
        self.frame_7 = QFrame(self.frame)
        self.setObjectName("frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0,0,0,0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName("frame_7")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0,0,0,0)
        self.label_6 =QLabel(self.frame_8)
        self.label_6.setObjectName("label_4")
        self.label_6.setMaximumSize(QSize(90, 16777215))
        self.verticalLayout_10.addWidget(self.label_6)
        self.horizontalLayout_2.addWidget(self.frame_8,0,QtCore.Qt.AlignLeft)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName("frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0,0,0,0)
        self.switch_mode = PyToggle(self.frame_9,width=85, onStateChange=self.set_mode)
        self.verticalLayout_11.addWidget(self.switch_mode)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_4.addWidget(self.frame,0,QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.verticalLayout_8.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setObjectName("label_5")
        self.label_5.setMaximumSize(QtCore.QSize(170,16777215))
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.label_7.setMaximumSize(QtCore.QSize(170,16777215))
        self.verticalLayout_8.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.main_accounts_dropdown = QtWidgets.QComboBox(self.frame_4)
        self.main_accounts_dropdown.setObjectName("main_accounts_dropdown")
        self.main_accounts_dropdown.setMaximumSize(QtCore.QSize(500,20))
        self.main_accounts_dropdown.currentTextChanged.connect(self.get_selected_account)
        self.verticalLayout_8.addWidget(self.main_accounts_dropdown)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(3)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 45)
        self.user_add_time_interval_input = QtWidgets.QLineEdit(self.frame_6)
        self.user_add_time_interval_input.setMaximumSize(QtCore.QSize(30, 16777215))
        self.user_add_time_interval_input.editingFinished.connect(self.set_user_add_time_interval)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.user_add_time_interval_input.setFont(font)
        self.user_add_time_interval_input.setObjectName("user_add_time_interval_input")
        self.verticalLayout_9.addWidget(self.user_add_time_interval_input)
        self.batches_interval_input = QtWidgets.QLineEdit(self.frame_6)
        self.batches_interval_input.setMaximumSize(QtCore.QSize(30, 16777215))
        self.batches_interval_input.editingFinished.connect(self.set_batches_interval)
        self.batches_interval_input.setFont(font)
        self.batches_interval_input.setObjectName("batches_interval_input")
        self.verticalLayout_9.addWidget(self.batches_interval_input)
        self.users_per_batch_input = QtWidgets.QLineEdit(self.frame_6)
        self.users_per_batch_input.setMaximumSize(QtCore.QSize(30, 16777215))
        self.users_per_batch_input.editingFinished.connect(self.set_users_per_batch)
        self.users_per_batch_input.setFont(font)
        self.users_per_batch_input.setText("")
        self.users_per_batch_input.setObjectName("users_per_batch_input")
        self.verticalLayout_9.addWidget(self.users_per_batch_input)
        self.add_users_limit_input = QtWidgets.QLineEdit(self.frame_6)
        self.add_users_limit_input.setObjectName("add_users_limit_input")
        self.add_users_limit_input.setMaximumSize(QtCore.QSize(30,16777215))
        self.add_users_limit_input.setFont(font)
        self.add_users_limit_input.editingFinished.connect(self.set_add_users_limit)
        self.verticalLayout_9.addWidget(self.add_users_limit_input)
        self.add_users_start_index_input = QLineEdit(self.frame_6)
        self.add_users_start_index_input.setObjectName("add_users_start_index_input")
        self.add_users_start_index_input.setMaximumSize(QtCore.QSize(30,16777215))
        self.add_users_start_index_input.setFont(font)
        self.add_users_start_index_input.editingFinished.connect(self.set_add_users_start_index)
        self.verticalLayout_9.addWidget(self.add_users_start_index_input)
        self.horizontalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.settings_menu.addTab(self.Settings, "")
        self.Info = QtWidgets.QWidget()
        self.Info.setObjectName("Info")
        self.Info.setContentsMargins(0, 0, 0, 0)
        self.Info.setMaximumSize(QtCore.QSize(16777215,500))
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Info)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.Info)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 500))
        self.verticalLayout_7.addWidget(self.textEdit)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.settings_menu.addTab(self.Info, "")
        self.verticalLayout_2.addWidget(self.settings_menu)
        self.verticalLayout.addWidget(self.settings_body_frame)
        self.retranslateUi()
        self.settings_menu.setCurrentIndex(0)
        # self.load_account_dropdown()
        self.load_settings_from_db()
        QtCore.QMetaObject.connectSlotsByName(self)
    def load_settings_from_db(self):
        settings = db.get_all_settings()

        if settings != []:
            settings = settings[0]
            self.id = settings["id"]

            self.only_megagroups_checkbox.setChecked(settings["only_megagroups"])
            self.recently_active_checkbox.setChecked(settings["scrape_active_users"])
            self.automatic_settings.setChecked(settings["automatic_settings"])
            self.skip_added_users_checkbox.setChecked(settings["skip_added_users"])
            self.switch_mode.setChecked(bool(settings["mode"]))
            self.user_add_time_interval_input.setText(str(settings["users_add_interval"]))
            self.users_per_batch_input.setText(str(settings["users_per_batch"]))
            self.batches_interval_input.setText(str(settings["users_batches_interval"]))

            if settings["users_limit"] == None:
                self.add_users_limit_input.setText("")
            else:
                self.add_users_limit_input.setText(str(settings["users_limit"]))

            self.add_users_start_index_input.setText(str(settings["add_users_start_index"]))
        else:
            id = db.insert_settings(self.only_megagroups_checkbox.isChecked(),
                                         self.skip_added_users_checkbox.isChecked(),
                                         self.automatic_settings.isChecked(),
                                         self.recently_active_checkbox.isChecked(),
                                         False,
                                         self.USERS_ADD_INTERVAL,
                                         self.USERS_BATCHES_INTERVAL,
                                         self.USERS_PER_BATCH,
                                         self.USERS_LIMIT,
                                         self.ADD_USERS_START_INDEX,
                                         self.main_accounts_dropdown.currentText()
                                         )
            self.id = id[0]
    def set_only_megagroups(self):
        self.reload_groups = True
        add_to_group.get_megagroups_only = self.only_megagroups_checkbox.isChecked()
        db.update_settings(self.id, only_megagroups=self.only_megagroups_checkbox.isChecked())
    def set_recently_active_users(self):
        scraper.scrape_only_recently_active = self.recently_active_checkbox.isChecked()
        db.update_settings(self.id, scrape_only_recently_active_users=self.recently_active_checkbox.isChecked())
    def set_automatic_settings(self):
        if self.automatic_settings.isChecked():
            if len(add_to_group.client_groups) >= 2:
                users_per_batch = len(add_to_group.client_groups)
                self.users_per_batch_input.setText(str(users_per_batch))
                user_add_time_interval = 4
                self.user_add_time_interval_input.setText(str(user_add_time_interval))
                users_limit = self.USERS_LIMIT
                self.add_users_limit_input.setText("")
                if len(add_to_group.client_groups )>12:
                    user_batches_interval = 15
                    self.batches_interval_input.setText(str(user_batches_interval))
                else:
                    user_batches_interval = 60 - (len(add_to_group.client_groups)*4)
                    self.batches_interval_input.setText(str(user_batches_interval))
            elif len(add_to_group.client_groups) == 1:
                users_per_batch = self.USERS_PER_BATCH
                self.users_per_batch_input.setText(str(self.USERS_PER_BATCH))
                user_batches_interval=self.USERS_BATCHES_INTERVAL
                self.batches_interval_input.setText(str(self.USERS_BATCHES_INTERVAL))
                user_add_time_interval = self.USERS_ADD_INTERVAL
                self.user_add_time_interval_input.setText(str(self.USERS_ADD_INTERVAL))
                users_limit = self.USERS_LIMIT
                self.add_users_limit_input.setText("")
            else:
                self.automatic_settings.setChecked(False)
                return
            db.update_settings(self.id,automatic_settings=self.automatic_settings.isChecked(), users_per_batch = users_per_batch, users_add_interval = user_add_time_interval,users_batches_interval = user_batches_interval,users_limit=users_limit)
    def set_skip_added_users(self):
        db.update_settings(self.id,skip_added_users=self.skip_added_users_checkbox.isChecked())
    def set_mode(self, mode):
        db.update_settings(self.id,mode=mode)
    def set_user_add_time_interval(self):
        try:
            time = int(self.user_add_time_interval_input.text())
            if time == "":
                self.user_add_time_interval_input.setText(str(self.USERS_ADD_INTERVAL))
                return
        except:
            time = self.USERS_ADD_INTERVAL
            self.user_add_time_interval_input.setText('10')

        self.automatic_settings.setChecked(False)
        db.update_settings(self.id,automatic_settings=self.automatic_settings.isChecked(), users_add_interval=time)
    def set_users_per_batch(self):
        try:
            users = int(self.users_per_batch_input.text())
            if users == "":
                self.users_per_batch_input.setText(str(self.USERS_PER_BATCH))
                return
        except:
            users = self.USERS_PER_BATCH
            self.users_per_batch_input.setText('20')
        self.users_per_batch = users
        self.automatic_settings.setChecked(False)
        db.update_settings(self.id,automatic_settings=self.automatic_settings.isChecked(), users_per_batch=users)
    def set_batches_interval(self):
        try:
            time = int(self.batches_interval_input.text())
            if time == "":
                self.batches_interval_input.setText(str(self.USERS_BATCHES_INTERVAL))
                return
        except:
            time = self.USERS_BATCHES_INTERVAL
            self.batches_interval_input.setText(str(time))

        self.automatic_settings.setChecked(False)
        db.update_settings(self.id,automatic_settings=self.automatic_settings.isChecked(), users_batches_interval=time)
    def set_add_users_limit(self):
        try:
            users = int(self.add_users_limit_input.text())
            if users == "":
                return
        except:
            users = self.USERS_LIMIT
            self.add_users_limit_input.setText('')

        db.update_settings(self.id, users_limit=users)
    def set_add_users_start_index(self):
        try:
            index = int(self.add_users_start_index_input.text())
            if index == "":
                return
        except:
            index = self.ADD_USERS_START_INDEX
            self.add_users_start_index_input.setText(str(self.ADD_USERS_START_INDEX))

        db.update_settings(self.id, add_users_start_index=index)
    def load_account_dropdown(self):
        if hasattr(self, "main_accounts_dropdown"):
            client_groups = list(add_to_group.client_phone.values())
            if client_groups == []:
                return

            self.detect_dropdown = False
            self.delete_accounts_from_dropdown()
            self.detect_dropdown = False

            self.main_accounts_dropdown.addItems(client_groups)
            settings = db.get_all_settings()
            if settings != []:
                self.main_accounts_dropdown.setCurrentText(settings[0]["main_account"])
            
    def delete_accounts_from_dropdown(self):
        self.main_accounts_dropdown.clear()
    def get_selected_account(self):
        if self.detect_dropdown:
                phone = self.main_accounts_dropdown.currentText()
                if phone == "":
                    return

                add_to_group.set_main_client(phone = phone)
                db.update_settings(self.id, main_account=phone)

                Ui_MainWindow.load_groups_scrape_button(Ui_MainWindow.self_main_window)
                Ui_MainWindow.load_groups_add_members_button(Ui_MainWindow.self_main_window)

        self.detect_dropdown = True
    def closeEvent(self,event):
        Ui_MainWindow.self_main_window.settings_open = False
        Ui_MainWindow.self_main_window.setEnabled(True)
        if self.reload_groups:
            Ui_MainWindow.self_main_window.load_groups(add_members=True)
            Ui_MainWindow.self_main_window.load_groups(scrape=True)
            Ui_MainWindow.self_main_window.stop_adding_members()
            self.reload_groups = False
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Settings"))
        self.only_megagroups_checkbox.setText(_translate("Ui_Settings", "Get only 'Megagroups'"))
        self.skip_added_users_checkbox.setText(_translate("Ui_Settings", "Skip already added users"))
        self.automatic_settings.setText(_translate("Ui_Settings", "Automatic settings"))
        self.recently_active_checkbox.setText(_translate("Ui_Settings", "Scrape only recently active users"))
        self.label.setText(_translate("self", "Interval between user add(secs)"))
        self.label_2.setText(_translate("self", "Interval between memeber batches(secs)"))
        self.label_3.setText(_translate("self", "Memebrs per batch"))
        self.label_4.setText(_translate("self", "Choose main account"))
        self.label_5.setText(_translate("self", "Add members limit"))
        self.label_7.setText(_translate("self", "Start adding users from"))
        self.label_6.setText(_translate("self", "Add users by: "))
        self.user_add_time_interval_input.setPlaceholderText(_translate("self", "10"))
        self.batches_interval_input.setPlaceholderText(_translate("self", "60"))
        self.users_per_batch_input.setPlaceholderText(_translate("self", "20"))
        self.add_users_start_index_input.setPlaceholderText(_translate("self", "1"))
        self.settings_menu.setTabText(self.settings_menu.indexOf(self.Settings), _translate("self", "Settings"))
        self.textEdit.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">BOT FOR ADDING MEMBERS TO GROUP</span></p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The bot can scrape members from certain group and to add them to certain group. </p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Telegram Api have got restrictions so you can add certain amoun of members per day in one group. If you use more than one account you will be able to add more people faster. I sugest you to set 10 secs time intervla between adding members if you use only one account, 20 people batches and 60 secs betweem batchest. in my experience it works the best in that way if you use one account. If you use more than one account you can set 2 secs time interval between adding members.</p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can get your Api Id and Api Hash from here: https://my.telegram.org/auth</p>\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For more information text me on: easytelegrambots@gmail.com</p></body></html>"))
        self.settings_menu.setTabText(self.settings_menu.indexOf(self.Info), _translate("self", "Info"))
