from django import forms
from home.models import Password, Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class HomeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('useridas',)


class CreatePinForm(forms.ModelForm):
    pin = forms.CharField()
    class Meta:
        model = Password
        fields = (
            'website',
            'name',
            'pin',
        )

class PasswordCreationForm(UserCreationForm):

    class Meta:
        model = Password
        fields = (
            'website',
            'name',
            'passwordGenerator',
        )

    def save(self, commit=True):
        new_password = super(PasswordCreationForm, self).save(commit=False)
        new_password.website = self.cleaned_data['website']
        new_password.name = self.cleaned_data['name']
        new_password.pin = self.cleaned_data['passwordGenerator']

        if commit:
            new_password.save()

        return new_password
