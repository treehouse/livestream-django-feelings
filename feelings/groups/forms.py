from django import forms
from django.db.models import Q

from . import models


class CompanyForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'description')
        model = models.Company


class FamilyForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'description')
        model = models.Family


class CompanyInviteForm(forms.Form):
    email_or_username = forms.CharField(label="Email/Username")

    def clean_email_or_username(self):
        data = self.cleaned_data['email_or_username']
        try:
            self.invitee = models.User.objects.get(
                Q(email=data) | Q(username=data)
            )
        except models.User.DoesNotExist:
            raise forms.ValidationError('That user/email does not exist!')
        return data


class LeaveForm(forms.Form):
    pass
