from django.forms import ModelForm, PasswordInput
from .models import User,Password

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','pwd']
        widgets = {
            'pwd': PasswordInput()
        }
class PasswordForm(ModelForm):
    class Meta:
        model = Password
        fields = ['domain_name','password']
        widgets = {
            'pwd': PasswordInput()
        }
