from django import forms

class Log_user(forms.ModelForm):

        class Meta:
            model = User
            fields = ('first_name', 'last_name',)