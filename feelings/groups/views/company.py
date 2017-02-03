from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from braces.views import SetHeadlineMixin

from .. import forms
from .. import models


class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = forms.CompanyForm
    headline = 'Create Company'
    success_url = reverse_lazy('users:dashboard')
    template_name = 'companies/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = forms.CompanyForm
    template_name = 'companies/form.html'

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_headline(self):
        return f'Edit {self.object.name}'

    def get_success_url(self):
        return reverse('groups:companies:detail', kwargs={
            'slug': self.object.slug})


class Detail(LoginRequiredMixin, generic.FormView):
    form_class = forms.CompanyInviteForm
    template_name = 'companies/detail.html'

    def get_success_url(self):
        self.get_object()
        return reverse('groups:companies:detail', kwargs={
            'slug': self.object.slug})

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_object(self):
        self.object = self.request.user.companies.get(
            slug=self.kwargs.get('slug')
        )
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        models.CompanyInvite.objects.create(
            from_user=self.request.user,
            to_user=form.invitee,
            company=self.get_object()
        )
        return response


class Leave(LoginRequiredMixin, SetHeadlineMixin, generic.FormView):
    form_class = forms.LeaveForm
    template_name = 'companies/form.html'
    success_url = reverse_lazy('users:dashboard')

    def get_object(self):
        try:
            self.object = self.request.user.companies.filter(
                slug=self.kwargs.get('slug'),
            ).exclude(created_by=self.request.user).get()
        except models.Company.DoesNotExist:
            raise Http404

    def get_headline(self):
        self.get_object()
        return f'Leave {self.object}?'

    def form_valid(self, form):
        self.get_object()
        self.object.members.remove(self.request.user)
        return super().form_valid(form)


class Invites(LoginRequiredMixin, generic.ListView):
    model = models.CompanyInvite
    template_name = 'companies/invites.html'

    def get_queryset(self):
        return self.request.user.companyinvite_received.filter(status=0)


class InviteResponse(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('groups:companies:invites')

    def get(self, request, *args, **kwargs):
        invite = get_object_or_404(
            models.CompanyInvite,
            to_user=request.user,
            uuid=kwargs.get('code'),
            status=0
        )
        if kwargs.get('response') == 'accept':
            invite.status = 1
        else:
            invite.status = 2

        invite.save()

        return super().get(request, *args, **kwargs)



