from django import forms
from django.contrib.auth import password_validation

from contentmanagement.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            password_validation.validate_password(password, self.instance)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('password', error)
        return password
