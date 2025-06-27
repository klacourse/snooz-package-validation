# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpindleDetectionDoc.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
from . import spindle_rc
import themes_rc

class Ui_SpindleDetectionDoc(object):
    def setupUi(self, SpindleDetectionDoc):
        if not SpindleDetectionDoc.objectName():
            SpindleDetectionDoc.setObjectName(u"SpindleDetectionDoc")
        SpindleDetectionDoc.resize(1440, 797)
        SpindleDetectionDoc.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(SpindleDetectionDoc)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spindle_image = QLabel(SpindleDetectionDoc)
        self.spindle_image.setObjectName(u"spindle_image")
        self.spindle_image.setMaximumSize(QSize(16777215, 100))
        self.spindle_image.setPixmap(QPixmap(u":/spindle_moda/e0004-b1-01-05-0001-smp303751_res80.png"))
        self.spindle_image.setScaledContents(False)
        self.spindle_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.spindle_image)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SpindleDetectionDoc)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(SpindleDetectionDoc)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.Shape.HLine)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SpindleDetectionDoc)

        QMetaObject.connectSlotsByName(SpindleDetectionDoc)
    # setupUi

    def retranslateUi(self, SpindleDetectionDoc):
        SpindleDetectionDoc.setWindowTitle("")
        self.spindle_image.setText("")
        self.label.setText(QCoreApplication.translate("SpindleDetectionDoc", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle detector validation</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("SpindleDetectionDoc", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A spindle is &quot;a train of distinct waves with frequency 11\u201316 Hz (most commonly 12\u201314 Hz) with a duration \u22650.5 s, usually maximal in amplitude using central derivations&quot; [1]</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool allows to validate the SUMO spindle detector [2] on the MODA dataset and replicate the original reported performance.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">1 - Input Files : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Add your PSG files (.edf, .sts or .eeg). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The .tsv file is also needed for the edf format.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\">	The .sig file is also needed for the Stellate format.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The whole NATUS subject folder is also needed for the NATUS format. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Channel Selection: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                        SUMO was trained on EEG data recorded from C3-A2 or C3-LE montages.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                        - For datasets containing <span style=\" font-weight:700;\">C3-CLE</span>, "
                        "reformatting is required:<br />                             \u2192 Select <span style=\" font-weight:700;\">C3-CLE</span> as the main EEG channel and <span style=\" font-weight:700;\">A2-CLE</span> as the reference.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                        - For datasets containing <span style=\" font-weight:700;\">C3-LE </span>(or<span style=\" font-weight:700;\"> C3-LER</span>), reformatting is <span style=\" font-weight:700;\">not</span> required:<br />                             \u2192 Select <span style=\" font-weight:700;\">C3-LE</span> (or <span style=\" font-weight:700;\">C3-LER</span>)<span style=\" font-weight:700;\"> </span>as the main EEG channel and leave the reference field empty.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">2 - Non valid events :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Select events to disable the spindle detection (i.e. artefacts previously detected and saved in the accessory file).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">3 - Spindle Detector : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Define the minimum and maximum duration of kept spindles.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Define in which sleep stage you want to detect spindles.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	You can also choose to detect spindle in the sleep cycles only or to exclude sleep periods from the analysis.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">4 - Output Files :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The spindle events are added into the accessory file (.tsv, .STS or .ent).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "	Define your output files for the spindles characteristics (signal characteristics). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	    - Check &quot;To save the detailed spindles report for the cohort&quot; if wanted and select the filename to save the report.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	    - Check &quot;To export characteristics of each spinlde (one file per recording)&quot; if wanted.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Notes:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  1- The default sett"
                        "ings are based on the original SUMO data processing pipeline. Please avoid modifying these settings when replicating the reported performance.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  2- The MODA segments consist of clean, artifact-free EEG extracted from N2 sleep. When replicating the reported performance, please do not specify non-valid events. This may negatively impact spindle detection accuracy and evaluation metrics.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">References:</p>\n"
"<p style=\" margin-top:0px; margin-bo"
                        "ttom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [1] Iber, C., American Academy of Sleep Medicine, 2007. The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. American Academy of Sleep Medicine. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [2] <span style=\" font-family:'Helvetica Neue';\">Kaulen, L., Schwabedal, J.T., Schneider, J., Ritter, P. and Bialonski, S., 2022. Advanced sleep spindle identification with neural networks.\u00a0</span><span style=\" font-family:'Helvetica Neue'; font-style:italic;\">Scientific reports</span><span style=\" font-family:'Helvetica Neue';\">,\u00a0</span><span style=\" font-family:'Helvetica Neue'; font-style:italic;\">12</span><span style=\" font-family:'Helvetica Neue';\">(1), p.7686.</span>  <a href=\"https://doi.org/10.1038/s41598-022-11210-y\"><span style=\" font-family:'Helvetica Neue'; t"
                        "ext-decoration: underline; color:#419cff;\">https://doi.org/10.1038/s41598-022-11210-y</span></a> </p></body></html>", None))
    # retranslateUi

