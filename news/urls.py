from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.display_news, name='news'),
    path('<int:year>/<int:month>/<int:day>/<slug:new>/', views.display_detail_new, name='new_detail'),
    path('club/', views.display_club_information, name='club'),
]
