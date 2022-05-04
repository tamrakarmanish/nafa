from django import forms
from .models import *


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ("__all__")
        exclude = ['user']


class SendEmailForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': ('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=Group.objects.all(),
                                           widget=forms.SelectMultiple())
