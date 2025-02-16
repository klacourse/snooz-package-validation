# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SumoExampleV2SettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SumoExampleV2SettingsView(object):
    def setupUi(self, SumoExampleV2SettingsView):
        if not SumoExampleV2SettingsView.objectName():
            SumoExampleV2SettingsView.setObjectName(u"SumoExampleV2SettingsView")
        SumoExampleV2SettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SumoExampleV2SettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SumoExampleV2SettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.original_signals_horizontalLayout = QHBoxLayout()
        self.original_signals_horizontalLayout.setObjectName(u"original_signals_horizontalLayout")
        self.original_signals_label = QLabel(SumoExampleV2SettingsView)
        self.original_signals_label.setObjectName(u"original_signals_label")

        self.original_signals_horizontalLayout.addWidget(self.original_signals_label)

        self.original_signals_lineedit = QLineEdit(SumoExampleV2SettingsView)
        self.original_signals_lineedit.setObjectName(u"original_signals_lineedit")

        self.original_signals_horizontalLayout.addWidget(self.original_signals_lineedit)


        self.verticalLayout.addLayout(self.original_signals_horizontalLayout)

        self.cleaned_signals_horizontalLayout = QHBoxLayout()
        self.cleaned_signals_horizontalLayout.setObjectName(u"cleaned_signals_horizontalLayout")
        self.cleaned_signals_label = QLabel(SumoExampleV2SettingsView)
        self.cleaned_signals_label.setObjectName(u"cleaned_signals_label")

        self.cleaned_signals_horizontalLayout.addWidget(self.cleaned_signals_label)

        self.cleaned_signals_lineedit = QLineEdit(SumoExampleV2SettingsView)
        self.cleaned_signals_lineedit.setObjectName(u"cleaned_signals_lineedit")

        self.cleaned_signals_horizontalLayout.addWidget(self.cleaned_signals_lineedit)


        self.verticalLayout.addLayout(self.cleaned_signals_horizontalLayout)

        self.norm_stat_horizontalLayout = QHBoxLayout()
        self.norm_stat_horizontalLayout.setObjectName(u"norm_stat_horizontalLayout")
        self.norm_stat_label = QLabel(SumoExampleV2SettingsView)
        self.norm_stat_label.setObjectName(u"norm_stat_label")

        self.norm_stat_horizontalLayout.addWidget(self.norm_stat_label)

        self.norm_stat_lineedit = QLineEdit(SumoExampleV2SettingsView)
        self.norm_stat_lineedit.setObjectName(u"norm_stat_lineedit")

        self.norm_stat_horizontalLayout.addWidget(self.norm_stat_lineedit)


        self.verticalLayout.addLayout(self.norm_stat_horizontalLayout)

        self.event_group_horizontalLayout = QHBoxLayout()
        self.event_group_horizontalLayout.setObjectName(u"event_group_horizontalLayout")
        self.event_group_label = QLabel(SumoExampleV2SettingsView)
        self.event_group_label.setObjectName(u"event_group_label")

        self.event_group_horizontalLayout.addWidget(self.event_group_label)

        self.event_group_lineedit = QLineEdit(SumoExampleV2SettingsView)
        self.event_group_lineedit.setObjectName(u"event_group_lineedit")

        self.event_group_horizontalLayout.addWidget(self.event_group_lineedit)


        self.verticalLayout.addLayout(self.event_group_horizontalLayout)

        self.event_name_horizontalLayout = QHBoxLayout()
        self.event_name_horizontalLayout.setObjectName(u"event_name_horizontalLayout")
        self.event_name_label = QLabel(SumoExampleV2SettingsView)
        self.event_name_label.setObjectName(u"event_name_label")

        self.event_name_horizontalLayout.addWidget(self.event_name_label)

        self.event_name_lineedit = QLineEdit(SumoExampleV2SettingsView)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")

        self.event_name_horizontalLayout.addWidget(self.event_name_lineedit)


        self.verticalLayout.addLayout(self.event_name_horizontalLayout)

        self.artifact_events_horizontalLayout = QHBoxLayout()
        self.artifact_events_horizontalLayout.setObjectName(u"artifact_events_horizontalLayout")
        self.artifact_events_label = QLabel(SumoExampleV2SettingsView)
        self.artifact_events_label.setObjectName(u"artifact_events_label")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_label)

        self.artifact_events_lineedit = QLineEdit(SumoExampleV2SettingsView)
        self.artifact_events_lineedit.setObjectName(u"artifact_events_lineedit")

        self.artifact_events_horizontalLayout.addWidget(self.artifact_events_lineedit)


        self.verticalLayout.addLayout(self.artifact_events_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SumoExampleV2SettingsView)

        QMetaObject.connectSlotsByName(SumoExampleV2SettingsView)
    # setupUi

    def retranslateUi(self, SumoExampleV2SettingsView):
        SumoExampleV2SettingsView.setWindowTitle(QCoreApplication.translate("SumoExampleV2SettingsView", u"Form", None))
        self.original_signals_label.setText(QCoreApplication.translate("SumoExampleV2SettingsView", u"original_signals", None))
        self.cleaned_signals_label.setText(QCoreApplication.translate("SumoExampleV2SettingsView", u"cleaned_signals", None))
        self.norm_stat_label.setText(QCoreApplication.translate("SumoExampleV2SettingsView", u"norm_stat", None))
        self.event_group_label.setText(QCoreApplication.translate("SumoExampleV2SettingsView", u"event_group", None))
        self.event_name_label.setText(QCoreApplication.translate("SumoExampleV2SettingsView", u"event_name", None))
        self.artifact_events_label.setText(QCoreApplication.translate("SumoExampleV2SettingsView", u"artifact_events", None))
    # retranslateUi

