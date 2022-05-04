from django import forms
from .models import *


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ("__all__")
        exclude = ["user"]


class SendEmailForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=Event.objects.all(),
                                           widget=forms.SelectMultiple())
