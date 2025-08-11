# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpindleDetectorSelStep.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_SpindleDetectorSelStep(object):
    def setupUi(self, SpindleDetectorSelStep):
        if not SpindleDetectorSelStep.objectName():
            SpindleDetectorSelStep.setObjectName(u"SpindleDetectorSelStep")
        SpindleDetectorSelStep.resize(875, 763)
        SpindleDetectorSelStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_5 = QHBoxLayout(SpindleDetectorSelStep)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_13 = QLabel(SpindleDetectorSelStep)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(SpindleDetectorSelStep)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.group_lineEdit = QLineEdit(SpindleDetectorSelStep)
        self.group_lineEdit.setObjectName(u"group_lineEdit")

        self.horizontalLayout_9.addWidget(self.group_lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(35, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(SpindleDetectorSelStep)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)

        self.name_lineEdit = QLineEdit(SpindleDetectorSelStep)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.horizontalLayout_10.addWidget(self.name_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.label_5 = QLabel(SpindleDetectorSelStep)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_8 = QLabel(SpindleDetectorSelStep)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SpindleDetectorSelStep)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(SpindleDetectorSelStep)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.min_length_lineEdit = QLineEdit(SpindleDetectorSelStep)
        self.min_length_lineEdit.setObjectName(u"min_length_lineEdit")

        self.horizontalLayout.addWidget(self.min_length_lineEdit)

        self.label_4 = QLabel(SpindleDetectorSelStep)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.max_length_lineEdit = QLineEdit(SpindleDetectorSelStep)
        self.max_length_lineEdit.setObjectName(u"max_length_lineEdit")

        self.horizontalLayout.addWidget(self.max_length_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label_10 = QLabel(SpindleDetectorSelStep)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_3.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.radioButton_detect_spindle = QRadioButton(SpindleDetectorSelStep)
        self.radioButton_detect_spindle.setObjectName(u"radioButton_detect_spindle")
        self.radioButton_detect_spindle.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_detect_spindle)

        self.radioButto_analyse_spindle = QRadioButton(SpindleDetectorSelStep)
        self.radioButto_analyse_spindle.setObjectName(u"radioButto_analyse_spindle")

        self.verticalLayout_3.addWidget(self.radioButto_analyse_spindle)

        self.verticalSpacer_4 = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(162, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.retranslateUi(SpindleDetectorSelStep)
        self.radioButton_detect_spindle.clicked.connect(SpindleDetectorSelStep.radio_button_slot)
        self.radioButto_analyse_spindle.clicked.connect(SpindleDetectorSelStep.radio_button_slot)

        QMetaObject.connectSlotsByName(SpindleDetectorSelStep)
    # setupUi

    def retranslateUi(self, SpindleDetectorSelStep):
        SpindleDetectorSelStep.setWindowTitle("")
        self.label_13.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Event  Settings</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"                       Group                     ", None))
        self.group_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"spindle", None))
        self.label_14.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"                       Name                      ", None))
        self.name_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"sumo", None))
        self.label_5.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle duration filtering</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Define the minimum and maximum duration of a valid spindle (shorter and longer spindle will be discarded)", None))
        self.label.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Length Limit (s)", None))
        self.label_3.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"min", None))
        self.min_length_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"0.3", None))
        self.label_4.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"max", None))
        self.max_length_lineEdit.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"2.5", None))
        self.label_10.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Detections and/or analyses</span></p></body></html>", None))
        self.radioButton_detect_spindle.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Detect spindles", None))
        self.radioButto_analyse_spindle.setText(QCoreApplication.translate("SpindleDetectorSelStep", u"Do not detect spindles, just analyze spindles previously detected and saved in the accessory file.", None))
    # retranslateUi

