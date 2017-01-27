from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from feelings.groups import forms


class CompanyCreate(LoginRequiredMixin, generic.CreateView):
    form_class = forms.CompanyForm
    success_url = reverse_lazy('users:dashboard')
    template_name = 'companies/company_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response

