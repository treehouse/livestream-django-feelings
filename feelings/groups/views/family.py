from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic

from braces.views import SetHeadlineMixin

from .. import forms
from .. import models


class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = forms.FamilyForm
    headline = 'Create Family'
    success_url = reverse_lazy('users:dashboard')
    template_name = 'families/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = forms.FamilyForm
    template_name = 'families/form.html'

    def get_queryset(self):
        return self.request.user.families.all()

    def get_headline(self):
        return f'Edit {self.object.name}'

    def get_success_url(self):
        return reverse('groups:families:detail', kwargs={
            'slug': self.object.slug})


class Detail(LoginRequiredMixin, generic.DetailView):
    template_name = 'families/detail.html'

    def get_queryset(self):
        return self.request.user.families.all()


class Invites(LoginRequiredMixin, generic.ListView):
    model = models.FamilyInvite
    template_name = 'families/invites.html'

    def get_queryset(self):
        return self.request.user.familyinvite_received.filter(status=0)


class InviteResponse(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('groups:families:invites')

    def get(self, request, *args, **kwargs):
        invite = get_object_or_404(
            models.FamilyInvite,
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

