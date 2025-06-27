"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    SpindleDetectorSelStep
    Step in the spindle detection interface to select the spindle detectors and 
    define the commons settings.
"""
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from ..Commons import ContextConstants
from .Ui_SpindleDetectorSelStep import Ui_SpindleDetectorSelStep


from qtpy import QtWidgets
from qtpy.QtCore import QRegularExpression
from qtpy.QtGui import QRegularExpressionValidator

class SpindleDetectorSelStep( BaseStepView,  Ui_SpindleDetectorSelStep, QtWidgets.QWidget):
    """
        SpindleDetectorSelStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform modules of the spindle detector selection and
        all the commons settings.
    """
    # Key for the context shared with other step of the preset
    context_spindle_det = "detection"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # added
        # Set input validators
        # Create a QRegularExpressionValidator with the desired regular expression
        # Regular expression for alphanumeric, space, dash, and latin1 (ISO/CEI 8859-1) characters
        regex = QRegularExpression(r'^[a-zA-Z0-9ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ\s_-]*$')
        validator = QRegularExpressionValidator(regex)

        # added
        # Set the validator for the QLineEdit
        self.name_lineEdit.setValidator(validator)
        self.name_lineEdit.setMaxLength(64)
        self.group_lineEdit.setValidator(validator)
        self.group_lineEdit.setMaxLength(64)

        # added
        # Define topics for event settings
        self._node_id_constant_group = "53dc47dd-b65b-41d9-8534-c1d85c79363a"
        self._node_id_constant_name = "73b79daf-92e6-46e1-9ff3-cceacbf273f3"
        
        # added
        # Default values for event settings
        self.group_lineEdit.setText("spindle")
        self.name_lineEdit.setText("sumo")
        

        # Define modules and nodes to talk to
        self._node_id_SpindleDetails_det = "0e3df2c0-7c41-4fa5-89bb-f6601ef8831a" # provide the spindle_parameters when new spindles are detected
        self._node_id_SpindleDetails_anal = "28929dd9-a992-4e7b-be6b-9e0a6053ae4e" # provide the spindle_parameters when spindles are analyzed only
        self._node_id_FilterEvents_anal = "8bb37834-1a4d-4632-a729-d4f69234348c" # filter spindle event when we just analyze
        self._node_id_SleepStageEvent = "6323a842-eb2b-47cd-b444-d299d0d6f2df" # provide in which sleep stage we detect spindles
        self._node_id_DiscardEvents = "98cd55c4-2e21-42b1-abcb-21c89e76e677" # provide artefact/spindle to discard
        # modules to bypass or deactivate if we dont detect spindles
        self._node_id_FilterSignal = "fcf58c9f-1ad0-4bd5-bb47-228ac8b5ab91" 
        self._node_id_ResetSignalArtefact_NaN = "a91be608-8be8-4f87-92f7-d2f83a759d8c" 
        self._node_id_SpindleDetsumo = "4625208b-d806-42f2-9856-36a7d2b3946a"
        self._node_id_PSGWriter = "07601632-b7a4-4365-81b6-b312d3565ad5"
        self._node_id_DiscardEvents = "98cd55c4-2e21-42b1-abcb-21c89e76e677"
        self._node_id_EventCombine = "9c352a25-80da-4fd5-bd90-e916a3252751"
        self._node_id_SignalStats = "6e12e8a3-d6dc-4c43-a710-845a6eac1cf6"

        # added
        # Subscribe to context manager for each node you want to talk to
        self._group_topic = f'{self._node_id_constant_group}.constant'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._name_topic = f'{self._node_id_constant_name}.constant'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        self._spindle_param_sumo_det_topic = f'{self._node_id_SpindleDetails_det}.spindle_sel_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_sumo_det_topic)
        self._spindle_param_sumo_anal_topic = f'{self._node_id_SpindleDetails_anal}.spindle_sel_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_sumo_anal_topic)

        # added
        self._spindle_sumo_param = {}
        self._spindle_sumo_param['spindle_name'] = 'sumo'

        # Subscribe to the publisher for each node you want to talk to
        self._stages_topic = f'{self._node_id_SleepStageEvent}.stages'
        self._pub_sub_manager.subscribe(self, self._stages_topic)
        self._exclude_nremp_topic = f'{self._node_id_SleepStageEvent}.exclude_nremp'
        self._pub_sub_manager.subscribe(self, self._exclude_nremp_topic)
        self._exclude_remp_topic = f'{self._node_id_SleepStageEvent}.exclude_remp'
        self._pub_sub_manager.subscribe(self, self._exclude_remp_topic)
        self._in_cycle_topic = f'{self._node_id_SleepStageEvent}.in_cycle'
        self._pub_sub_manager.subscribe(self, self._in_cycle_topic)
        self._min_len_topic = f'{self._node_id_DiscardEvents}.min_len_sec'
        self._pub_sub_manager.subscribe(self, self._min_len_topic)        
        self._max_len_topic = f'{self._node_id_DiscardEvents}.max_len_sec'
        self._pub_sub_manager.subscribe(self, self._max_len_topic)   
        self._spindle_param_gen_det_topic = f'{self._node_id_SpindleDetails_det}.spindle_gen_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_gen_det_topic)    
        self._spindle_param_gen_anal_topic = f'{self._node_id_SpindleDetails_anal}.spindle_gen_param'
        self._pub_sub_manager.subscribe(self, self._spindle_param_gen_anal_topic) 

        # _context_manager is inherited from the BaseStepView
        # it allows to share information between steps in the step-by-step interface
        # ContextManager is a dictionary that publish an update through the 
        # PubSubManager whenever a value is modified.
        self._context_manager[ContextConstants.context_in_cycle] = True
        self._context_manager[SpindleDetectorSelStep.context_spindle_det] = True

        self._spindle_det_param = {}


    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_nremp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._exclude_remp_topic, 'ping')
        self._pub_sub_manager.publish(self, self._in_cycle_topic, 'ping')
        self._pub_sub_manager.publish(self, self._min_len_topic, 'ping')
        self._pub_sub_manager.publish(self, self._max_len_topic, 'ping')
        self._pub_sub_manager.publish(self, self._spindle_param_gen_det_topic, 'ping')

        #added
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._spindle_param_sumo_det_topic, 'ping')

        self._pub_sub_manager.publish(self, self._node_id_SpindleDetsumo+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_det+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_anal+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_FilterEvents_anal+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_PSGWriter+".get_activation_state", None)
        
    
    # Called when the user clic on RUN
    # Message are sent to the publisher   
    def on_apply_settings(self):
        # stages_str = '2'  # Always use stage 2 (N2) as default            
        # self._pub_sub_manager.publish(self, self._stages_topic, str(stages_str))
        # self._pub_sub_manager.publish(self, self._exclude_nremp_topic, str(int(self.checkBox_excl_nremp.isChecked())))
        # self._pub_sub_manager.publish(self, self._exclude_remp_topic, str(int(self.checkBox_excl_remp.isChecked())))
        # self._pub_sub_manager.publish(self, self._in_cycle_topic, str(int(self.checkBox_only_cycles.isChecked())))
        self._pub_sub_manager.publish(self, self._min_len_topic, self.min_length_lineEdit.text())
        self._pub_sub_manager.publish(self, self._max_len_topic, self.max_length_lineEdit.text())

        # added
        # Send the settings to the publisher
        self._pub_sub_manager.publish(self, self._group_topic, self.group_lineEdit.text())
        self._pub_sub_manager.publish(self, self._name_topic, self.name_lineEdit.text())

        # added
        # Init the _spindle_param_gen_topic and send the dict
        self._spindle_sumo_param['spindle_name'] = self.name_lineEdit.text()
        self._pub_sub_manager.publish(self, self._spindle_param_sumo_det_topic, self._spindle_sumo_param)
        self._pub_sub_manager.publish(self, self._spindle_param_sumo_anal_topic, self._spindle_sumo_param)
        
        
        if self.radioButton_detect_spindle.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_FilterSignal+".activation_state_change",ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_NaN+".activation_state_change",ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpindleDetsumo+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_PSGWriter+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_DiscardEvents+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_EventCombine+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SignalStats+".activation_state_change", ActivationState.ACTIVATED)

            self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_anal+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_det+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_FilterEvents_anal+".activation_state_change", ActivationState.DEACTIVATED)

        if self.radioButto_analyse_spindle.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_FilterSignal+".activation_state_change", ActivationState.BYPASS)   
            self._pub_sub_manager.publish(self, self._node_id_SpindleDetsumo+".activation_state_change", ActivationState.DEACTIVATED)   
            self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_NaN+".activation_state_change", ActivationState.BYPASS)   
            self._pub_sub_manager.publish(self, self._node_id_PSGWriter+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_DiscardEvents+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_EventCombine+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SignalStats+".activation_state_change", ActivationState.DEACTIVATED)

            self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_det+".activation_state_change", ActivationState.DEACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_SpindleDetails_anal+".activation_state_change", ActivationState.ACTIVATED)
            self._pub_sub_manager.publish(self, self._node_id_FilterEvents_anal+".activation_state_change", ActivationState.ACTIVATED)

        # Init the _spindle_param_gen_topic and send the dict
        self._spindle_det_param['min_duration'] = float(self.min_length_lineEdit.text())
        self._spindle_det_param['max_duration'] = float(self.max_length_lineEdit.text())
        # self._spindle_det_param['sleep_stage_sel'] = stages_str.split(',')
        # self._spindle_det_param['in_cycle'] = int(self.checkBox_only_cycles.isChecked())
        # self._spindle_det_param['exclude_nremp'] = int(self.checkBox_excl_nremp.isChecked())
        # self._spindle_det_param['exclude_remp'] = int(self.checkBox_excl_remp.isChecked())
        self._pub_sub_manager.publish(self, self._spindle_param_gen_det_topic, str(self._spindle_det_param))
        self._pub_sub_manager.publish(self, self._spindle_param_gen_anal_topic, str(self._spindle_det_param))


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        
        # added
        if topic == self._name_topic:
            self.name_lineEdit.setText(message)     
             
        # if topic == self._stages_topic:
        #     stages_lst = message.split(',')
        #     self.checkBox_n1.setChecked('1' in stages_lst)
        #     self.checkBox_n2.setChecked('2' in stages_lst)
        #     self.checkBox_n3.setChecked('3' in stages_lst)
        #     self.checkBox_r.setChecked('5' in stages_lst)
        # if topic == self._exclude_nremp_topic:
        #     self.checkBox_excl_nremp.setChecked(int(message))
        # if topic == self._exclude_remp_topic:
        #     self.checkBox_excl_remp.setChecked(int(message))
        # if topic == self._in_cycle_topic:
        #     self.checkBox_only_cycles.setChecked(int(message))
        if topic == self._min_len_topic:
            self.min_length_lineEdit.setText(message)
        if topic == self._max_len_topic:
            self.max_length_lineEdit.setText(message)
        if topic == self._spindle_param_gen_det_topic:
            if not message=='':
                self._spindle_det_param = eval(message)
        if topic == self._node_id_SpindleDetsumo+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.radioButton_detect_spindle.setChecked(True)
                self.radio_button_slot()
            else:
                self.radioButto_analyse_spindle.setChecked(True)
                self.radio_button_slot()

        # It's commented even in A7 
        # if topic == self._node_id_SpindleDetails_anal+".get_activation_state":
        #     if message == ActivationState.ACTIVATED:
        #         self.radioButto_analyse_spindle.setChecked(True)
        #     else:
        #         self.radioButto_analyse_spindle.setChecked(False)
    

    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    # def on_topic_update(self, topic, message, sender):
    #     if topic==self._context_manager.topic:
    #         # If the context_per_cycle is checked from MartinSettings 
    #         #   -> check the computation of the thresh per cycle (the opposite is not true)            
    #         if message==ContextConstants.context_per_cycle: # key of the context dict
    #             # Need to select only in cycle to compute threshold per cycle (the opposite is not true)
    #             if self._context_manager[ContextConstants.context_per_cycle]==True: 
    #                 self.checkBox_only_cycles.setChecked(True)


    # Called when user check/uncheck detection in_cycle_only checkbox
    # def detect_in_cycle_only_slot(self):
    #     self._context_manager[ContextConstants.context_in_cycle] = self.checkBox_only_cycles.isChecked()


    # Called when user check/uncheck the radio button to detect or analyze spindle
    #    The context is updated for the outputFileStep
    def radio_button_slot(self):
        if self.radioButton_detect_spindle.isChecked():
            self._context_manager[SpindleDetectorSelStep.context_spindle_det] = True
        else:
            self._context_manager[SpindleDetectorSelStep.context_spindle_det] = False


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            # self._pub_sub_manager.unsubscribe(self, self._stages_topic)
            # self._pub_sub_manager.unsubscribe(self, self._exclude_nremp_topic)
            # self._pub_sub_manager.unsubscribe(self, self._exclude_remp_topic)
            # self._pub_sub_manager.unsubscribe(self, self._in_cycle_topic)
            self._pub_sub_manager.unsubscribe(self, self._min_len_topic)
            self._pub_sub_manager.unsubscribe(self, self._max_len_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_gen_det_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_gen_anal_topic)

            # added
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_sumo_det_topic)
            self._pub_sub_manager.unsubscribe(self, self._spindle_param_sumo_anal_topic)