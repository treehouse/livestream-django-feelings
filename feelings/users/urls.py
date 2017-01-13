from django.conf.urls import url, include

urlpatterns = [
   url('^', include('django.contrib.auth.urls')),
]