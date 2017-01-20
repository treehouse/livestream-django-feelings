from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from .forms import ThoughtForm


class CreateThought(LoginRequiredMixin, CreateView):
    form_class = ThoughtForm
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
