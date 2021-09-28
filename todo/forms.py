from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    #  メタクラスとは https://teratail.com/questions/87695
    class Meta:
        model = Todo
        exclude = ('created_at', 'update_at')
