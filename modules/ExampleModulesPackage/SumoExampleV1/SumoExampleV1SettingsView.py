"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Settings viewer of the SumoExampleV1 plugin
"""

from qtpy import QtWidgets

from ExampleModulesPackage.SumoExampleV1.Ui_SumoExampleV1SettingsView import Ui_SumoExampleV1SettingsView
from commons.BaseSettingsView import BaseSettingsView

class SumoExampleV1SettingsView(BaseSettingsView, Ui_SumoExampleV1SettingsView, QtWidgets.QWidget):
    """
        SumoExampleV1View set the SumoExampleV1 settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._signals_topic = f'{self._parent_node.identifier}.signals'
        self._pub_sub_manager.subscribe(self, self._signals_topic)
        self._event_group_topic = f'{self._parent_node.identifier}.event_group'
        self._pub_sub_manager.subscribe(self, self._event_group_topic)
        self._event_name_topic = f'{self._parent_node.identifier}.event_name'
        self._pub_sub_manager.subscribe(self, self._event_name_topic)
        self._artifact_events_topic = f'{self._parent_node.identifier}.artifact_events'
        self._pub_sub_manager.subscribe(self, self._artifact_events_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artifact_events_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to SumoExampleV1
        self._pub_sub_manager.publish(self, self._signals_topic, str(self.signals_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_group_topic, str(self.event_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_name_topic, str(self.event_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artifact_events_topic, str(self.artifact_events_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._signals_topic:
            self.signals_lineedit.setText(message)
        if topic == self._event_group_topic:
            self.event_group_lineedit.setText(message)
        if topic == self._event_name_topic:
            self.event_name_lineedit.setText(message)
        if topic == self._artifact_events_topic:
            self.artifact_events_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._artifact_events_topic)
            