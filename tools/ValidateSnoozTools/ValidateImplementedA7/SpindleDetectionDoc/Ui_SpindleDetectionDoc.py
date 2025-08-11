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
        SpindleDetectionDoc.resize(1082, 749)
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

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.textEdit = QTextEdit(SpindleDetectionDoc)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SpindleDetectionDoc)

        QMetaObject.connectSlotsByName(SpindleDetectionDoc)
    # setupUi

    def retranslateUi(self, SpindleDetectionDoc):
        SpindleDetectionDoc.setWindowTitle("")
        self.spindle_image.setText("")
        self.label.setText(QCoreApplication.translate("SpindleDetectionDoc", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle detection</span></p></body></html>", None))
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
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool allows detecting spindles using the algorithms from (Lacourse et al., 2019) [2] and validating the detection set against the MODA [3] database.<br />This version sets the minimum spindle length to 0.3 s to replicate the results published in MODA [3].</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">1 - Input Files : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Add your PSG files (xx-xx-xxxx PSG.edf from MASS [4]).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The S"
                        "nooz .tsv annotation files are also required for the EDF format; <br />	they need to be converted from the EDF+ format provided by the MASS team.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">2 - Non valid events :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Select events to disable the spindle detection (i.e. artefacts previously detected and saved in the accessory file).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" text-decoration: underline;\">3 - Spindle Detector : </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Set the minimum and maximum durations to 0.3 s and 2.5 s, respectively, to replicate the MODA results.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">4 - Output Files :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	The spindle events are added into the accessory file (.tsv).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	Define your"
                        " output files for the spindles characteristics (signal characteristics). </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	    - Check &quot;To save the detailed spindles report for the cohort&quot; if wanted and select the filename to save the report.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	    - Check &quot;To export characteristics of each spinlde (one file per recording)&quot; if wanted.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">References:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [1] Iber, C., American Ac"
                        "ademy of Sleep Medicine, 2007. The AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. American Academy of Sleep Medicine. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [2] Lacourse, K., Delfrate, J., Beaudry, J., Peppard, P., Warby, S.C., 2019. A sleep spindle detection algorithm that emulates human expert spindle scoring. Journal of Neuroscience Methods 316, 3\u201311. <a href=\"https://doi.org/10.1016/j.jneumeth.2018.08.014\"><span style=\" text-decoration: underline; color:#0000ff;\">https://doi.org/10.1016/j.jneumeth.2018.08.014</span></a> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [3] Lacourse, K., Yetton, B., Mednick, S., &amp; Warby, S. C. (2020). Massive online data annotation, crowdsourcing to generate high quality sleep spindle annotations from EEG data. <span style=\" "
                        "font-style:italic;\">Scientific Data</span>, <span style=\" font-style:italic;\">7</span>(1), Article 1. <a href=\"https://doi.org/10.1038/s41597-020-0533-4\"><span style=\" text-decoration: underline; color:#003e92;\">https://doi.org/10.1038/s41597-020-0533-4</span></a> </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   [4] O\u2019Reilly, C., Gosselin, N., Carrier, J., &amp; Nielsen, T. (2014, December 1). <span style=\" font-style:italic;\">Montreal Archive of Sleep Studies: An open\u2010access resource for instrument benchmarking and exploratory research</span>. Journal of Sleep Research. <a href=\"https://doi.org/10.1111/jsr.12169\"><span style=\" text-decoration: underline; color:#003e92;\">https://doi.org/10.1111/jsr.12169</span></a> </p></body></html>", None))
    # retranslateUi

