from django import forms
from django.db.models import fields
from django.forms import widgets
from . models import login


class Emplogin(forms.ModelForm):
  class Meta:
      model=login
      fields=['EmpName','Password']
      widgets={'Password':forms.PasswordInput()}