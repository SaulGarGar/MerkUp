from django import forms
from form models import User

class Log_user(forms.ModelForm):

        class Meta:
            model = User
            fields = ('first_name', 'last_name',)