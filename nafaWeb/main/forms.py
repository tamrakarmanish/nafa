from django import forms
from .models import *

        
class MembershipForm(forms.ModelForm):
    
    class Meta:
        model = Membership
        fields = ("__all__")        

class ScholarshipForm(forms.ModelForm):

    class Meta:
        model = Scholarship
        fields = ("name", "description", "date")

class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ("name", "description", "date")


# class EventRSVPForm(forms.ModelForm):
    
#     class Meta:
#         model = EventRsvp
#         fields = ("__all__")