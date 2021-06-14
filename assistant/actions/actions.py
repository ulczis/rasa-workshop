import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet, EventType, SessionStarted, ActionExecuted

class IncidentStatus(Action):

    def name(self):
        return 'action_incident_status'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("The status of your ticket is : pending")
        return []