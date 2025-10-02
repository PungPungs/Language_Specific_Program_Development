# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '20250930_draft_ver1tCHQzA.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 489, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 0, 4, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_15.setFont(font1)
        self.label_15.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_15, 1, 6, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.rb_psbp = QRadioButton(self.gridLayoutWidget)
        self.rb_psbp.setObjectName(u"rb_psbp")

        self.gridLayout.addWidget(self.rb_psbp, 3, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.pb_convert = QPushButton(self.gridLayoutWidget)
        self.pb_convert.setObjectName(u"pb_convert")
        self.pb_convert.setMinimumSize(QSize(100, 50))

        self.gridLayout.addWidget(self.pb_convert, 4, 0, 1, 7)

        self.le_x_max = QLineEdit(self.gridLayoutWidget)
        self.le_x_max.setObjectName(u"le_x_max")
        self.le_x_max.setMaximumSize(QSize(70, 20))
        font3 = QFont()
        font3.setPointSize(7)
        self.le_x_max.setFont(font3)

        self.gridLayout.addWidget(self.le_x_max, 0, 5, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_14, 1, 3, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_17, 2, 6, 1, 1)

        self.le_y_min = QLineEdit(self.gridLayoutWidget)
        self.le_y_min.setObjectName(u"le_y_min")
        self.le_y_min.setMaximumSize(QSize(70, 20))
        self.le_y_min.setFont(font3)

        self.gridLayout.addWidget(self.le_y_min, 1, 2, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setPointSize(22)
        font4.setBold(True)
        font4.setStyleStrategy(QFont.NoAntialias)
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 2, 4, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_13, 0, 6, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.rb_4ch = QRadioButton(self.gridLayoutWidget)
        self.rb_4ch.setObjectName(u"rb_4ch")

        self.gridLayout.addWidget(self.rb_4ch, 3, 5, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 1, 4, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_16, 2, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.label_12, 0, 3, 1, 1)

        self.le_y_max = QLineEdit(self.gridLayoutWidget)
        self.le_y_max.setObjectName(u"le_y_max")
        self.le_y_max.setMaximumSize(QSize(70, 20))
        self.le_y_max.setFont(font3)

        self.gridLayout.addWidget(self.le_y_max, 1, 5, 1, 1)

        self.le_x_min = QLineEdit(self.gridLayoutWidget)
        self.le_x_min.setObjectName(u"le_x_min")
        self.le_x_min.setMaximumSize(QSize(70, 20))
        self.le_x_min.setFont(font3)

        self.gridLayout.addWidget(self.le_x_min, 0, 2, 1, 1)

        self.le_time_min = QLineEdit(self.gridLayoutWidget)
        self.le_time_min.setObjectName(u"le_time_min")
        self.le_time_min.setMaximumSize(QSize(70, 20))
        self.le_time_min.setFont(font3)

        self.gridLayout.addWidget(self.le_time_min, 2, 2, 1, 1)

        self.le_time_max = QLineEdit(self.gridLayoutWidget)
        self.le_time_max.setObjectName(u"le_time_max")
        self.le_time_max.setMaximumSize(QSize(70, 20))
        self.le_time_max.setFont(font3)

        self.gridLayout.addWidget(self.le_time_max, 2, 5, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.le_x_min, self.le_x_max)
        QWidget.setTabOrder(self.le_x_max, self.le_y_min)
        QWidget.setTabOrder(self.le_y_min, self.le_y_max)
        QWidget.setTabOrder(self.le_y_max, self.le_time_min)
        QWidget.setTabOrder(self.le_time_min, self.le_time_max)
        QWidget.setTabOrder(self.le_time_max, self.rb_psbp)
        QWidget.setTabOrder(self.rb_psbp, self.rb_4ch)
        QWidget.setTabOrder(self.rb_4ch, self.pb_convert)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ucd08\uc548", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"(max)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.rb_psbp.setText(QCoreApplication.translate("MainWindow", u"PSBP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"UTM X", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"UTM Y", None))
        self.pb_convert.setText(QCoreApplication.translate("MainWindow", u"\ubcc0\ud658", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc88c\ud45c", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"(min)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"(max)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"(max)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\ud0c0\uc785", None))
        self.rb_4ch.setText(QCoreApplication.translate("MainWindow", u"4CH", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"(min)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"(min)", None))
    # retranslateUi

