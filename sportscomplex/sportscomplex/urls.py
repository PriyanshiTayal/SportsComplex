"""sportscomplex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from sports import views as s_views
from users import views as u_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',u_views.login, name = 'login'),
    path('dologin/',u_views.dologin, name = 'dologin'),
    path('register/',u_views.register, name = 'register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('profile/',u_views.profile, name = 'profile'),
    path('add_staff/',u_views.add_staff, name = 'add_staff'),
    path('remove_staff/',u_views.remove_staff, name = 'remove_staff'),

    path('',s_views.home, name = 'home'),
    path('sport_page/<slug:sport>', s_views.sport_page, name = 'sport_page'), 
    path('slot_book/<slug:slot_id>',s_views.slot_book, name = 'slot_book'),
    path('add_sport/',s_views.add_sport, name = 'add_sport'),
    path('add_court/',s_views.add_court, name = 'add_court'),
    path('add_equipment/',s_views.add_equipment, name = 'add_equipment'),
    path('add_slot/',s_views.add_slot, name = 'add_slot'),
    path('available_slot/<slug:court>', s_views.available_slot, name = 'available_slot'),
]
