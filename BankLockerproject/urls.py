"""BankLockerproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from banklockerapp.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('dashboard/', dashboard, name="dashboard"),
    path('profile/', profile, name="profile"),
    path('authentication-login/', authentication_login, name="authentication_login"),
    path('logout_user/', logout_user, name="logout_user"),
    path('add_subbanker/', add_subbanker, name="add_subbanker"),
    path('edit_subbanker/<int:pid>/', add_subbanker, name="edit_subbanker"),
    path('delete_subbanker/<int:pid>/', delete_subbanker, name="delete_subbanker"),
    path('view_subbanker/', view_subbanker, name="view_subbanker"),
    path('add-lockertype/', add_lockertype, name="add_lockertype"),
    path('edit_lockertype/<int:pid>/', add_lockertype, name="edit_lockertype"),
    path('delete_lockertype/<int:pid>/', delete_lockertype, name="delete_lockertype"),
    path('view-lockertype/', view_lockertype, name="view_lockertype"),
    path('add_assign/', add_assign, name="add_assign"),
    path('edit_assign/<int:pid>/', edit_assign, name="edit_assign"),
    path('delete_assign/<int:pid>/', delete_assign, name="delete_assign"),
    path('view_assign/', view_assign, name="view_assign"),
    path('index_search_locker/', index_search_locker, name="index_search_locker"),
    path('report_date/', report_date, name="report_date"),
    path('search_report/', search_report, name="search_report"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('detail/<int:pid>', detail, name="detail"),
    path('change_password/', change_password, name="change_password"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
