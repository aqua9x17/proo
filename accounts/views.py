from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LoginForm, UserForm
from .mixins import RoleRequiredMixin
from .models import User


class AppLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm


class AppLogoutView(LogoutView):
    pass


class UserListView(RoleRequiredMixin, ListView):
    allowed_roles = (User.Roles.ADMIN,)
    model = User
    template_name = "accounts/user_list.html"


class UserCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = (User.Roles.ADMIN,)
    model = User
    form_class = UserForm
    template_name = "common/form.html"
    success_url = reverse_lazy("accounts:user_list")

    def form_valid(self, form):
        messages.success(self.request, "User created successfully.")
        return super().form_valid(form)


class UserUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = (User.Roles.ADMIN,)
    model = User
    form_class = UserForm
    template_name = "common/form.html"
    success_url = reverse_lazy("accounts:user_list")


class UserDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = (User.Roles.ADMIN,)
    model = User
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("accounts:user_list")
