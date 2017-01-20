from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.CreateThought.as_view(), name='create'),
]