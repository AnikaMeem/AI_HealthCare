from django import forms

from .models import Appoinment


class AppoinmentsForm(forms.ModelForm):
    class Meta:
        model = Appoinment
        fields = "__all__"
        labels = {
            "patient": "Patient",
            "doctor": "Doctor",
            "date": "Pick a date and time"
        }
        error_messages = {
            "doctor": {
              "required": "Doctor name must not be empty!"
            },
            "patient": {
              "required": "Patient name must not be empty!"
            },
            "date":{
                "required": "You have to select a date"
            }
        }