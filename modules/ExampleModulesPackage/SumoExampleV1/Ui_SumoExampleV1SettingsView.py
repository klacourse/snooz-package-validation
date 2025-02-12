# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SumoExampleV1SettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SumoExampleV1SettingsView(object):
    def setupUi(self, SumoExampleV1SettingsView):
        if not SumoExampleV1SettingsView.objectName():
            SumoExampleV1SettingsView.setObjectName(u"SumoExampleV1SettingsView")
        SumoExampleV1SettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SumoExampleV1SettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SumoExampleV1SettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(SumoExampleV1SettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(SumoExampleV1SettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.event_group_horizontalLayout = QHBoxLayout()
        self.event_group_horizontalLayout.setObjectName(u"event_group_horizontalLayout")
        self.event_group_label = QLabel(SumoExampleV1SettingsView)
        self.event_group_label.setObjectName(u"event_group_label")

        self.event_group_horizontalLayout.addWidget(self.event_group_label)

        self.event_group_lineedit = QLineEdit(SumoExampleV1SettingsView)
        self.event_group_lineedit.setObjectName(u"event_group_lineedit")

        self.event_group_horizontalLayout.addWidget(self.event_group_lineedit)


        self.verticalLayout.addLayout(self.event_group_horizontalLayout)

        self.event_name_horizontalLayout = QHBoxLayout()
        self.event_name_horizontalLayout.setObjectName(u"event_name_horizontalLayout")
        self.event_name_label = QLabel(SumoExampleV1SettingsView)
        self.event_name_label.setObjectName(u"event_name_label")

        self.event_name_horizontalLayout.addWidget(self.event_name_label)

        self.event_name_lineedit = QLineEdit(SumoExampleV1SettingsView)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")

        self.event_name_horizontalLayout.addWidget(self.event_name_lineedit)


        self.verticalLayout.addLayout(self.event_name_horizontalLayout)

        self.artifact_events_horizontalLayout = QHBoxLayout()
        self.artifact_events_horizontalLayout.setObjectName(u"artifact_events_horizontalLayout")
        self.artifact_events_label = QLabel(SumoExampleV1SettingsView)
        self.artifact_events_label.setObjectName(u"artifact_events_label")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_label)

        self.artifact_events_lineedit = QLineEdit(SumoExampleV1SettingsView)
        self.artifact_events_lineedit.setObjectName(u"artifact_events_lineedit")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_lineedit)


        self.verticalLayout.addLayout(self.artifact_events_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SumoExampleV1SettingsView)

        QMetaObject.connectSlotsByName(SumoExampleV1SettingsView)
    # setupUi

    def retranslateUi(self, SumoExampleV1SettingsView):
        SumoExampleV1SettingsView.setWindowTitle(QCoreApplication.translate("SumoExampleV1SettingsView", u"Form", None))
        self.signals_label.setText(QCoreApplication.translate("SumoExampleV1SettingsView", u"signals", None))
        self.event_group_label.setText(QCoreApplication.translate("SumoExampleV1SettingsView", u"event_group", None))
        self.event_name_label.setText(QCoreApplication.translate("SumoExampleV1SettingsView", u"event_name", None))
        self.artifact_events_label.setText(QCoreApplication.translate("SumoExampleV1SettingsView", u"artifact_events", None))
    # retranslateUi

