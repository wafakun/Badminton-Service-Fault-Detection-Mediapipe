# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacebaru.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

import resources_rc

class Ui_Mainwindow2(object):
    def setupUi(self, Mainwindow2):
        if not Mainwindow2.objectName():
            Mainwindow2.setObjectName(u"Mainwindow2")
        Mainwindow2.resize(1024, 600)
        Mainwindow2.setMinimumSize(QSize(1024, 600))
        Mainwindow2.setMaximumSize(QSize(1024, 600))
        Mainwindow2.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"#frame_4, #frame_8, #frame_11, #frame_13, #frame_14, #frame_15, #popupNotificationSubContainer, #rightMenuSubContainer,  #mainContensContainer, #midContentcontainer{\n"
"	background-color: #16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer, #footerContainer, #frame_8, #frame_11, #frame_15{\n"
"	background-color: #2c313c;\n"
"}\n"
"#pushButton_2{\n"
"	background-color: rgb(85, 170, 0);\n"
"}")
        self.centralwidget = QWidget(Mainwindow2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(78, 78))
        self.label_5.setLineWidth(1)
        self.label_5.setPixmap(QPixmap(u":/images/badminton no bg.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame = QFrame(self.headerContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame)

        self.pushButton_2 = QPushButton(self.headerContainer)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton:enabled {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(167, 167, 167);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon)
        self.closeBtn.setIconSize(QSize(31, 31))

        self.horizontalLayout_5.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContensContainer = QWidget(self.mainBodyContent)
        self.mainContensContainer.setObjectName(u"mainContensContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContensContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mainContensSubContainer = QWidget(self.mainContensContainer)
        self.mainContensSubContainer.setObjectName(u"mainContensSubContainer")
        self.horizontalLayout_14 = QHBoxLayout(self.mainContensSubContainer)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.widget_7 = QWidget(self.mainContensSubContainer)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_14 = QVBoxLayout(self.widget_7)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setSpacing(60)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(60, 60, 60, 60)
        self.frame_15 = QFrame(self.widget_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_15)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_15)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(43, 43))

        self.verticalLayout.addWidget(self.pushButton_11)

        self.pushButton = QPushButton(self.frame_15)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton:enabled {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(167, 167, 167);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame_15)


        self.verticalLayout_14.addWidget(self.widget_5)


        self.horizontalLayout_14.addWidget(self.widget_7)


        self.verticalLayout_15.addWidget(self.mainContensSubContainer)


        self.horizontalLayout_8.addWidget(self.mainContensContainer)

        self.midContentcontainer = QWidget(self.mainBodyContent)
        self.midContentcontainer.setObjectName(u"midContentcontainer")
        self.verticalLayout_16 = QVBoxLayout(self.midContentcontainer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.midContentcontainer)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.widget_4 = QWidget(self.widget_6)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setSpacing(60)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(60, 60, 60, 60)
        self.frame_11 = QFrame(self.widget_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(43, 43))

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_16 = QPushButton(self.frame_11)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setStyleSheet(u"QPushButton:enabled {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(167, 167, 167);\n"
"}")
        self.pushButton_16.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_16)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.verticalLayout_16.addWidget(self.widget_6)


        self.horizontalLayout_8.addWidget(self.midContentcontainer)

        self.rightMenuContainer = QWidget(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.rightMenuContainer)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setEnabled(True)
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuSubContainer.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_13 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.widget_8 = QWidget(self.rightMenuSubContainer)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_17 = QVBoxLayout(self.widget_8)
        self.verticalLayout_17.setSpacing(60)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(60, 60, 60, 60)
        self.frame_8 = QFrame(self.widget_8)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.frame_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u"C:/multi-pose-landmark-mediapipe-main/GUI TA/icons/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(43, 43))

        self.verticalLayout_5.addWidget(self.pushButton_12)

        self.captureBtn = QPushButton(self.frame_8)
        self.captureBtn.setObjectName(u"captureBtn")
        self.captureBtn.setFont(font2)
        self.captureBtn.setStyleSheet(u"QPushButton:enabled {\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	color: rgb(167, 167, 167);\n"
"}")
        self.captureBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_5.addWidget(self.captureBtn)


        self.verticalLayout_17.addWidget(self.frame_8)


        self.verticalLayout_13.addWidget(self.widget_8)


        self.horizontalLayout_13.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 0))
        self.label_16.setMaximumSize(QSize(57, 57))
        self.label_16.setFrameShape(QFrame.StyledPanel)
        self.label_16.setFrameShadow(QFrame.Plain)
        self.label_16.setPixmap(QPixmap(u":/images/poltek.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_16)


        self.horizontalLayout_11.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        Mainwindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainwindow2)
        self.pushButton_2.clicked.connect(Mainwindow2.close)
        self.closeBtn.clicked.connect(Mainwindow2.close)
        self.captureBtn.clicked.connect(self.rightMenuContainer.show)

        QMetaObject.connectSlotsByName(Mainwindow2)
    # setupUi

    def retranslateUi(self, Mainwindow2):
        Mainwindow2.setWindowTitle(QCoreApplication.translate("Mainwindow2", u"Mainwindow2", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Mainwindow2", u"SERVICE FAULT BADMINTON DETECTION", None))
        self.pushButton_2.setText(QCoreApplication.translate("Mainwindow2", u"NORMAL", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("Mainwindow2", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.pushButton_11.setText("")
        self.pushButton.setText(QCoreApplication.translate("Mainwindow2", u"CAM 1", None))
        self.pushButton_9.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("Mainwindow2", u"CAM 2", None))
        self.pushButton_12.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_12.setShortcut(QCoreApplication.translate("Mainwindow2", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.captureBtn.setToolTip(QCoreApplication.translate("Mainwindow2", u"Capture", None))
#endif // QT_CONFIG(tooltip)
        self.captureBtn.setText(QCoreApplication.translate("Mainwindow2", u"Replay", None))
        self.label_15.setText(QCoreApplication.translate("Mainwindow2", u"Copyright Politeknik Negeri Madiun @2023", None))
        self.label_16.setText("")
    # retranslateUi

        self.captureBtn.clicked.connect(self.openvideo)
        self.pushButton_12.clicked.connect(self.openvideo)
        self.pushButton.clicked.connect(self.btn1)
        self.pushButton_11.clicked.connect(self.btn1)
        self.pushButton_16.clicked.connect(self.btn2)
        self.pushButton_9.clicked.connect(self.btn2)
        self.pushButton_2.clicked.connect(self.kidal)


    def btn1(self):
        os.system('python -u "C:/Yolo/multi-pose-landmark-mediapipe-main/coba1.py"')

    def btn2(self):
        os.system('python -u "C:/Yolo/multi-pose-landmark-mediapipe-main/coba2.py"')  

    def openvideo(self):
        os.system('python -u "C:/Yolo/multi-pose-landmark-mediapipe-main/GUI TA/openvidiofolder"')

    def kidal(self):
        os.system('python -u "C:/Yolo/multi-pose-landmark-mediapipe-main/GUI TA/main.py"')