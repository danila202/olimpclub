from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('registration/',views.registration_of_user, name='user_form'),
    path('form/', views.display_user_form, name='form'),
    ]

