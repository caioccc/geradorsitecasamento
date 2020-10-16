"""default URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app.views import IndexView, submit_rsvp, submit_recado, UploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index_view'),
    path('submit', submit_rsvp, name='submit_rsvp'),
    path('send-recado', submit_recado, name='submit_recado'),
    path('upload-csv/', UploadView.as_view(), name="profile_upload"),
]
