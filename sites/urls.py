from django.urls import path

from .views import (
    MessageCreateView,
    MessageDeleteView,
    MessageListView,
    MessageUpdateView,
    SiteCreateView,
    SiteDeleteView,
    SiteListView,
    SiteUpdateView,
)

app_name = "sites"

urlpatterns = [
    path("", SiteListView.as_view(), name="site_list"),
    path("create/", SiteCreateView.as_view(), name="site_create"),
    path("<int:pk>/edit/", SiteUpdateView.as_view(), name="site_update"),
    path("<int:pk>/delete/", SiteDeleteView.as_view(), name="site_delete"),
    path("messages/", MessageListView.as_view(), name="message_list"),
    path("messages/create/", MessageCreateView.as_view(), name="message_create"),
    path("messages/<int:pk>/edit/", MessageUpdateView.as_view(), name="message_update"),
    path("messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),
]
