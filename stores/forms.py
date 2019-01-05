from django import forms
from .models import Store, Policy


class StorePrimaryInfoForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'city']


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['return_policy', 'return_policy_description', 'exchange_policy', 'exchange_policy_description',
                  'cancellation_policy', 'cancellation_policy_description', 'further_description']
        widgets = {
            'return_policy': forms.RadioSelect,
            'exchange_policy': forms.RadioSelect,
            'cancellation_policy': forms.RadioSelect
        }
