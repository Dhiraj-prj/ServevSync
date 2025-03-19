from django import forms
from .models import HouseworkerProfile

class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = HouseworkerProfile
        fields = ['name', 'service', 'contact', 'bio']
