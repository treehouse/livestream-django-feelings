from django import forms

from . import models


class ThoughtForm(forms.ModelForm):
    class Meta:
        fields = ('condition', 'notes')
        model = models.Thought