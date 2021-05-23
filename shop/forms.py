from django.forms import ModelForm
from .models import Todo,userdetail,order
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model =Todo
        fields = ['title', 'memo', 'important']


class userdetals (ModelForm):
        class Meta:
            model =userdetail
            fields = ['name', 'phone', 'address', 'order']



class orders (ModelForm):
        class Meta:
            model =order
            fields = ['item',]
