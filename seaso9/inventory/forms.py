from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.models import User


"""
user Registration form
"""


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=25)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")
    captcha = ReCaptchaField()

    def clean_password2(self):
        password = self.cleaned_data['password']  # cleaned_data dictionary has the valid fields
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    class Meta:
        model = User
        fields = '__all__'

"""
class UpdateuserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = '__all__'
        """
