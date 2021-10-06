from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    #  メタクラスとは https://teratail.com/questions/87695
    class Meta:
        model = Todo
        exclude = ('created_at', 'update_at')

class TestForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')