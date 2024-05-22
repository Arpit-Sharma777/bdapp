
from django import forms
from.models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name', 'age', 'weight', 'email', 'blood_group', 'phone_number', 'address', 'city', 'state', 'zip_code')

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Age must be 18 or older.')
        return age

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight < 50:
            raise forms.ValidationError('Weight must be 50 kg or more.')
        return weight