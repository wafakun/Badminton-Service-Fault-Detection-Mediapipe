/********************************************************************************
** Form generated from reading UI file 'interfacebaruVxsCEm.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef INTERFACEBARUVXSCEM_H
#define INTERFACEBARUVXSCEM_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout;
    QWidget *mainBodyContainer;
    QVBoxLayout *verticalLayout_10;
    QWidget *headerContainer;
    QHBoxLayout *horizontalLayout_4;
    QFrame *frame_5;
    QHBoxLayout *horizontalLayout_7;
    QLabel *label_5;
    QLabel *label_6;
    QFrame *frame;
    QPushButton *pushButton_2;
    QFrame *frame_7;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *closeBtn;
    QWidget *mainBodyContent;
    QHBoxLayout *horizontalLayout_8;
    QWidget *mainContensContainer;
    QVBoxLayout *verticalLayout_15;
    QWidget *mainContensSubContainer;
    QHBoxLayout *horizontalLayout_14;
    QWidget *widget_7;
    QVBoxLayout *verticalLayout_14;
    QWidget *widget_5;
    QHBoxLayout *horizontalLayout_2;
    QFrame *frame_15;
    QVBoxLayout *verticalLayout;
    QPushButton *pushButton_11;
    QPushButton *pushButton;
    QWidget *midContentcontainer;
    QVBoxLayout *verticalLayout_16;
    QWidget *widget_6;
    QVBoxLayout *verticalLayout_3;
    QWidget *widget_4;
    QVBoxLayout *verticalLayout_4;
    QFrame *frame_11;
    QVBoxLayout *verticalLayout_2;
    QPushButton *pushButton_9;
    QPushButton *pushButton_16;
    QWidget *rightMenuContainer;
    QHBoxLayout *horizontalLayout_13;
    QWidget *rightMenuSubContainer;
    QVBoxLayout *verticalLayout_13;
    QWidget *widget_8;
    QVBoxLayout *verticalLayout_17;
    QFrame *frame_8;
    QVBoxLayout *verticalLayout_5;
    QPushButton *pushButton_12;
    QPushButton *captureBtn;
    QWidget *footerContainer;
    QHBoxLayout *horizontalLayout_11;
    QFrame *frame_10;
    QHBoxLayout *horizontalLayout_12;
    QLabel *label_15;
    QLabel *label_16;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(1024, 600);
        MainWindow->setMinimumSize(QSize(1024, 600));
        MainWindow->setMaximumSize(QSize(1024, 600));
        MainWindow->setStyleSheet(QLatin1String("*{\n"
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
"}"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        horizontalLayout = new QHBoxLayout(centralwidget);
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        mainBodyContainer = new QWidget(centralwidget);
        mainBodyContainer->setObjectName(QStringLiteral("mainBodyContainer"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(mainBodyContainer->sizePolicy().hasHeightForWidth());
        mainBodyContainer->setSizePolicy(sizePolicy);
        mainBodyContainer->setStyleSheet(QStringLiteral(""));
        verticalLayout_10 = new QVBoxLayout(mainBodyContainer);
        verticalLayout_10->setSpacing(0);
        verticalLayout_10->setObjectName(QStringLiteral("verticalLayout_10"));
        verticalLayout_10->setContentsMargins(0, 0, 0, 0);
        headerContainer = new QWidget(mainBodyContainer);
        headerContainer->setObjectName(QStringLiteral("headerContainer"));
        horizontalLayout_4 = new QHBoxLayout(headerContainer);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        frame_5 = new QFrame(headerContainer);
        frame_5->setObjectName(QStringLiteral("frame_5"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        horizontalLayout_7 = new QHBoxLayout(frame_5);
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setObjectName(QStringLiteral("horizontalLayout_7"));
        horizontalLayout_7->setContentsMargins(0, 0, 0, 0);
        label_5 = new QLabel(frame_5);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setMaximumSize(QSize(78, 78));
        label_5->setLineWidth(1);
        label_5->setPixmap(QPixmap(QString::fromUtf8(":/images/badminton no bg.png")));
        label_5->setScaledContents(true);

        horizontalLayout_7->addWidget(label_5);

        label_6 = new QLabel(frame_5);
        label_6->setObjectName(QStringLiteral("label_6"));
        QFont font;
        font.setPointSize(19);
        font.setBold(true);
        font.setWeight(75);
        label_6->setFont(font);

        horizontalLayout_7->addWidget(label_6);


        horizontalLayout_4->addWidget(frame_5, 0, Qt::AlignLeft);

        frame = new QFrame(headerContainer);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);

        horizontalLayout_4->addWidget(frame);

        pushButton_2 = new QPushButton(headerContainer);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        QFont font1;
        font1.setPointSize(14);
        font1.setBold(true);
        font1.setWeight(75);
        pushButton_2->setFont(font1);
        pushButton_2->setStyleSheet(QLatin1String("QPushButton:enabled {\n"
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
"}"));

        horizontalLayout_4->addWidget(pushButton_2);

        frame_7 = new QFrame(headerContainer);
        frame_7->setObjectName(QStringLiteral("frame_7"));
        frame_7->setFrameShape(QFrame::StyledPanel);
        frame_7->setFrameShadow(QFrame::Raised);
        horizontalLayout_5 = new QHBoxLayout(frame_7);
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        closeBtn = new QPushButton(frame_7);
        closeBtn->setObjectName(QStringLiteral("closeBtn"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/icons/x-circle.svg"), QSize(), QIcon::Normal, QIcon::Off);
        closeBtn->setIcon(icon);
        closeBtn->setIconSize(QSize(31, 31));

        horizontalLayout_5->addWidget(closeBtn);


        horizontalLayout_4->addWidget(frame_7, 0, Qt::AlignRight);


        verticalLayout_10->addWidget(headerContainer, 0, Qt::AlignTop);

        mainBodyContent = new QWidget(mainBodyContainer);
        mainBodyContent->setObjectName(QStringLiteral("mainBodyContent"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(mainBodyContent->sizePolicy().hasHeightForWidth());
        mainBodyContent->setSizePolicy(sizePolicy1);
        horizontalLayout_8 = new QHBoxLayout(mainBodyContent);
        horizontalLayout_8->setObjectName(QStringLiteral("horizontalLayout_8"));
        mainContensContainer = new QWidget(mainBodyContent);
        mainContensContainer->setObjectName(QStringLiteral("mainContensContainer"));
        verticalLayout_15 = new QVBoxLayout(mainContensContainer);
        verticalLayout_15->setSpacing(0);
        verticalLayout_15->setObjectName(QStringLiteral("verticalLayout_15"));
        verticalLayout_15->setContentsMargins(0, 0, 0, 0);
        mainContensSubContainer = new QWidget(mainContensContainer);
        mainContensSubContainer->setObjectName(QStringLiteral("mainContensSubContainer"));
        horizontalLayout_14 = new QHBoxLayout(mainContensSubContainer);
        horizontalLayout_14->setObjectName(QStringLiteral("horizontalLayout_14"));
        horizontalLayout_14->setContentsMargins(5, 5, 5, 5);
        widget_7 = new QWidget(mainContensSubContainer);
        widget_7->setObjectName(QStringLiteral("widget_7"));
        verticalLayout_14 = new QVBoxLayout(widget_7);
        verticalLayout_14->setSpacing(0);
        verticalLayout_14->setObjectName(QStringLiteral("verticalLayout_14"));
        verticalLayout_14->setContentsMargins(0, 0, 0, 0);
        widget_5 = new QWidget(widget_7);
        widget_5->setObjectName(QStringLiteral("widget_5"));
        horizontalLayout_2 = new QHBoxLayout(widget_5);
        horizontalLayout_2->setSpacing(60);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(60, 60, 60, 60);
        frame_15 = new QFrame(widget_5);
        frame_15->setObjectName(QStringLiteral("frame_15"));
        frame_15->setFrameShape(QFrame::StyledPanel);
        frame_15->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frame_15);
        verticalLayout->setSpacing(0);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        pushButton_11 = new QPushButton(frame_15);
        pushButton_11->setObjectName(QStringLiteral("pushButton_11"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/icons/video.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_11->setIcon(icon1);
        pushButton_11->setIconSize(QSize(43, 43));

        verticalLayout->addWidget(pushButton_11);

        pushButton = new QPushButton(frame_15);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        QFont font2;
        font2.setPointSize(20);
        font2.setBold(true);
        font2.setWeight(75);
        pushButton->setFont(font2);
        pushButton->setStyleSheet(QLatin1String("QPushButton:enabled {\n"
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
"}"));

        verticalLayout->addWidget(pushButton);


        horizontalLayout_2->addWidget(frame_15);


        verticalLayout_14->addWidget(widget_5);


        horizontalLayout_14->addWidget(widget_7);


        verticalLayout_15->addWidget(mainContensSubContainer);


        horizontalLayout_8->addWidget(mainContensContainer);

        midContentcontainer = new QWidget(mainBodyContent);
        midContentcontainer->setObjectName(QStringLiteral("midContentcontainer"));
        verticalLayout_16 = new QVBoxLayout(midContentcontainer);
        verticalLayout_16->setSpacing(0);
        verticalLayout_16->setObjectName(QStringLiteral("verticalLayout_16"));
        verticalLayout_16->setContentsMargins(0, 0, 0, 0);
        widget_6 = new QWidget(midContentcontainer);
        widget_6->setObjectName(QStringLiteral("widget_6"));
        verticalLayout_3 = new QVBoxLayout(widget_6);
        verticalLayout_3->setSpacing(7);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(5, 5, 5, 5);
        widget_4 = new QWidget(widget_6);
        widget_4->setObjectName(QStringLiteral("widget_4"));
        verticalLayout_4 = new QVBoxLayout(widget_4);
        verticalLayout_4->setSpacing(60);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(60, 60, 60, 60);
        frame_11 = new QFrame(widget_4);
        frame_11->setObjectName(QStringLiteral("frame_11"));
        frame_11->setFrameShape(QFrame::StyledPanel);
        frame_11->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame_11);
        verticalLayout_2->setSpacing(0);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        pushButton_9 = new QPushButton(frame_11);
        pushButton_9->setObjectName(QStringLiteral("pushButton_9"));
        pushButton_9->setIcon(icon1);
        pushButton_9->setIconSize(QSize(43, 43));

        verticalLayout_2->addWidget(pushButton_9);

        pushButton_16 = new QPushButton(frame_11);
        pushButton_16->setObjectName(QStringLiteral("pushButton_16"));
        pushButton_16->setFont(font2);
        pushButton_16->setStyleSheet(QLatin1String("QPushButton:enabled {\n"
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
"}"));
        pushButton_16->setIconSize(QSize(40, 40));

        verticalLayout_2->addWidget(pushButton_16);


        verticalLayout_4->addWidget(frame_11);


        verticalLayout_3->addWidget(widget_4);


        verticalLayout_16->addWidget(widget_6);


        horizontalLayout_8->addWidget(midContentcontainer);

        rightMenuContainer = new QWidget(mainBodyContent);
        rightMenuContainer->setObjectName(QStringLiteral("rightMenuContainer"));
        rightMenuContainer->setMinimumSize(QSize(200, 0));
        rightMenuContainer->setSizeIncrement(QSize(0, 0));
        horizontalLayout_13 = new QHBoxLayout(rightMenuContainer);
        horizontalLayout_13->setSpacing(0);
        horizontalLayout_13->setObjectName(QStringLiteral("horizontalLayout_13"));
        horizontalLayout_13->setContentsMargins(0, 0, 0, 0);
        rightMenuSubContainer = new QWidget(rightMenuContainer);
        rightMenuSubContainer->setObjectName(QStringLiteral("rightMenuSubContainer"));
        rightMenuSubContainer->setEnabled(true);
        rightMenuSubContainer->setMinimumSize(QSize(200, 0));
        rightMenuSubContainer->setSizeIncrement(QSize(0, 0));
        verticalLayout_13 = new QVBoxLayout(rightMenuSubContainer);
        verticalLayout_13->setObjectName(QStringLiteral("verticalLayout_13"));
        verticalLayout_13->setContentsMargins(5, 5, 5, 5);
        widget_8 = new QWidget(rightMenuSubContainer);
        widget_8->setObjectName(QStringLiteral("widget_8"));
        verticalLayout_17 = new QVBoxLayout(widget_8);
        verticalLayout_17->setSpacing(60);
        verticalLayout_17->setObjectName(QStringLiteral("verticalLayout_17"));
        verticalLayout_17->setContentsMargins(60, 60, 60, 60);
        frame_8 = new QFrame(widget_8);
        frame_8->setObjectName(QStringLiteral("frame_8"));
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Raised);
        verticalLayout_5 = new QVBoxLayout(frame_8);
        verticalLayout_5->setSpacing(0);
        verticalLayout_5->setObjectName(QStringLiteral("verticalLayout_5"));
        verticalLayout_5->setContentsMargins(0, 0, 0, 0);
        pushButton_12 = new QPushButton(frame_8);
        pushButton_12->setObjectName(QStringLiteral("pushButton_12"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/icons/icons/aperture.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_12->setIcon(icon2);
        pushButton_12->setIconSize(QSize(43, 43));

        verticalLayout_5->addWidget(pushButton_12);

        captureBtn = new QPushButton(frame_8);
        captureBtn->setObjectName(QStringLiteral("captureBtn"));
        captureBtn->setFont(font2);
        captureBtn->setStyleSheet(QLatin1String("QPushButton:enabled {\n"
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
"}"));
        captureBtn->setIconSize(QSize(40, 40));

        verticalLayout_5->addWidget(captureBtn);


        verticalLayout_17->addWidget(frame_8);


        verticalLayout_13->addWidget(widget_8);


        horizontalLayout_13->addWidget(rightMenuSubContainer);


        horizontalLayout_8->addWidget(rightMenuContainer);


        verticalLayout_10->addWidget(mainBodyContent);

        footerContainer = new QWidget(mainBodyContainer);
        footerContainer->setObjectName(QStringLiteral("footerContainer"));
        horizontalLayout_11 = new QHBoxLayout(footerContainer);
        horizontalLayout_11->setSpacing(0);
        horizontalLayout_11->setObjectName(QStringLiteral("horizontalLayout_11"));
        horizontalLayout_11->setContentsMargins(0, 0, -1, 0);
        frame_10 = new QFrame(footerContainer);
        frame_10->setObjectName(QStringLiteral("frame_10"));
        frame_10->setFrameShape(QFrame::StyledPanel);
        frame_10->setFrameShadow(QFrame::Raised);
        horizontalLayout_12 = new QHBoxLayout(frame_10);
        horizontalLayout_12->setObjectName(QStringLiteral("horizontalLayout_12"));
        label_15 = new QLabel(frame_10);
        label_15->setObjectName(QStringLiteral("label_15"));
        QFont font3;
        font3.setPointSize(12);
        label_15->setFont(font3);
        label_15->setAlignment(Qt::AlignCenter);

        horizontalLayout_12->addWidget(label_15);

        label_16 = new QLabel(frame_10);
        label_16->setObjectName(QStringLiteral("label_16"));
        label_16->setMinimumSize(QSize(0, 0));
        label_16->setMaximumSize(QSize(57, 57));
        label_16->setFrameShape(QFrame::StyledPanel);
        label_16->setFrameShadow(QFrame::Plain);
        label_16->setPixmap(QPixmap(QString::fromUtf8(":/images/poltek.png")));
        label_16->setScaledContents(true);

        horizontalLayout_12->addWidget(label_16);


        horizontalLayout_11->addWidget(frame_10);


        verticalLayout_10->addWidget(footerContainer);


        horizontalLayout->addWidget(mainBodyContainer);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);
        QObject::connect(closeBtn, SIGNAL(clicked()), MainWindow, SLOT(close()));
        QObject::connect(captureBtn, SIGNAL(clicked()), rightMenuContainer, SLOT(show()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label_5->setText(QString());
        label_6->setText(QApplication::translate("MainWindow", "SERVICE FAULT BADMINTON DETECTION", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "NORMAL", nullptr));
#ifndef QT_NO_TOOLTIP
        closeBtn->setToolTip(QApplication::translate("MainWindow", "Close Window", nullptr));
#endif // QT_NO_TOOLTIP
        closeBtn->setText(QString());
        pushButton_11->setText(QString());
        pushButton->setText(QApplication::translate("MainWindow", "CAM 1", nullptr));
        pushButton_9->setText(QString());
        pushButton_16->setText(QApplication::translate("MainWindow", "CAM 2", nullptr));
        pushButton_12->setText(QString());
#ifndef QT_NO_SHORTCUT
        pushButton_12->setShortcut(QApplication::translate("MainWindow", "Ctrl+S", nullptr));
#endif // QT_NO_SHORTCUT
#ifndef QT_NO_TOOLTIP
        captureBtn->setToolTip(QApplication::translate("MainWindow", "Capture", nullptr));
#endif // QT_NO_TOOLTIP
        captureBtn->setText(QApplication::translate("MainWindow", "Replay", nullptr));
        label_15->setText(QApplication::translate("MainWindow", "Copyright Politeknik Negeri Madiun @2023", nullptr));
        label_16->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // INTERFACEBARUVXSCEM_H
