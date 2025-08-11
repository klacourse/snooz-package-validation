# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFilesStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_OutputFilesStep(object):
    def setupUi(self, OutputFilesStep):
        if not OutputFilesStep.objectName():
            OutputFilesStep.setObjectName(u"OutputFilesStep")
        OutputFilesStep.resize(786, 631)
        OutputFilesStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.gridLayout = QGridLayout(OutputFilesStep)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)

        self.label_4 = QLabel(OutputFilesStep)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_7 = QLabel(OutputFilesStep)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 9, 1, 1, 1)

        self.label_8 = QLabel(OutputFilesStep)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cohort_lineedit = QLineEdit(OutputFilesStep)
        self.cohort_lineedit.setObjectName(u"cohort_lineedit")
        self.cohort_lineedit.setMinimumSize(QSize(350, 0))
        self.cohort_lineedit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.cohort_lineedit)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_cohort = QPushButton(OutputFilesStep)
        self.pushButton_cohort.setObjectName(u"pushButton_cohort")

        self.horizontalLayout.addWidget(self.pushButton_cohort)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)

        self.checkBox_spindle_file = QCheckBox(OutputFilesStep)
        self.checkBox_spindle_file.setObjectName(u"checkBox_spindle_file")

        self.gridLayout.addWidget(self.checkBox_spindle_file, 8, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(OutputFilesStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(OutputFilesStep)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(OutputFilesStep)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(OutputFilesStep)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(175, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 2, 1, 1)

        self.label_6 = QLabel(OutputFilesStep)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)

        self.label_5 = QLabel(OutputFilesStep)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.checkBox_cohort_file = QCheckBox(OutputFilesStep)
        self.checkBox_cohort_file.setObjectName(u"checkBox_cohort_file")
        self.checkBox_cohort_file.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_cohort_file, 5, 1, 1, 1)

        self.textEdit = QTextEdit(OutputFilesStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 270))
        self.textEdit.setMaximumSize(QSize(16777215, 297))
        self.textEdit.setFrameShape(QFrame.Shape.HLine)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 4, 1, 1, 1)


        self.retranslateUi(OutputFilesStep)
        self.pushButton_cohort.clicked.connect(OutputFilesStep.browse_cohort_slot)
        self.checkBox_cohort_file.clicked.connect(OutputFilesStep.enable_cohort_slot)
        self.checkBox_spindle_file.clicked.connect(OutputFilesStep.enable_spindle_slot)

        QMetaObject.connectSlotsByName(OutputFilesStep)
    # setupUi

    def retranslateUi(self, OutputFilesStep):
        OutputFilesStep.setWindowTitle("")
        self.label_4.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle characteristics</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("OutputFilesStep", u"    * Files are saved in a new folder named \"spindles_characteristics\" at the cohort report level.", None))
        self.label_8.setText(QCoreApplication.translate("OutputFilesStep", u"* The spindle details are appended at the end of the cohort report if it exists.", None))
        self.cohort_lineedit.setPlaceholderText(QCoreApplication.translate("OutputFilesStep", u"Select the file to save detailed cohort report...", None))
        self.pushButton_cohort.setText(QCoreApplication.translate("OutputFilesStep", u"Browse", None))
        self.checkBox_spindle_file.setText(QCoreApplication.translate("OutputFilesStep", u"To export characteristics of each spindle (one file per recording)", None))
        self.label_2.setText(QCoreApplication.translate("OutputFilesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle events</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("OutputFilesStep", u"Spindle events are added in the accessory file (.tsv, .sts or .ent)", None))
        self.label_3.setText(QCoreApplication.translate("OutputFilesStep", u"Spindle events are defined as [group, name, start_sec, duration_sec, channels]", None))
        self.label_9.setText(QCoreApplication.translate("OutputFilesStep", u"Performance results are saved in a text file ending with _perf.tsv in the same directory as the data", None))
        self.label_6.setText(QCoreApplication.translate("OutputFilesStep", u"    * Without cohort report : the file is saved in the same folder as the PSG file.", None))
        self.label_5.setText(QCoreApplication.translate("OutputFilesStep", u"List of characteristics exported", None))
        self.checkBox_cohort_file.setText(QCoreApplication.translate("OutputFilesStep", u"To save the detailed events report for the cohort (cohort report)", None))
        self.textEdit.setHtml(QCoreApplication.translate("OutputFilesStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">For each spindle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   - duration (s)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   - dominent frequency (Hz), <span style=\" color:#000000;\""
                        ">where spectral energy is maximum</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">   - average frequency (Hz) counting peaks</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">   - peak-to-peak amplitude (\u00b5V)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">   - Root Mean Square (rms) amplitude (\u00b5V)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">F"
                        "or the cohort</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - spindle count</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - spindle density (spinde count per minute)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    - the average spindle characteristics listed above</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - total (all selected stages)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - per sleep stage</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        - per sleep cycle</p></body></html>", None))
    # retranslateUi

