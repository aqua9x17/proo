from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.mixins import RoleRequiredMixin
from accounts.models import User
from .forms import SiteForm, SiteMessageForm
from .models import Site, SiteMessage


class SiteListView(LoginRequiredMixin, ListView):
    model = Site
    template_name = "sites/site_list.html"


class SiteCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = Site
    form_class = SiteForm
    template_name = "common/form.html"
    success_url = reverse_lazy("sites:site_list")


class SiteUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = Site
    form_class = SiteForm
    template_name = "common/form.html"
    success_url = reverse_lazy("sites:site_list")


class SiteDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = (User.Roles.ADMIN,)
    model = Site
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("sites:site_list")


class MessageListView(LoginRequiredMixin, ListView):
    model = SiteMessage
    template_name = "sites/message_list.html"


class MessageCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = SiteMessage
    form_class = SiteMessageForm
    template_name = "common/form.html"
    success_url = reverse_lazy("sites:message_list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class MessageUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = SiteMessage
    form_class = SiteMessageForm
    template_name = "common/form.html"
    success_url = reverse_lazy("sites:message_list")


class MessageDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = (User.Roles.ADMIN,)
    model = SiteMessage
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("sites:message_list")
