from django.urls import path
from . import views

app_name = 'petronexa_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('blog/<int:det_id>/', views.blog, name='blog'),
    path('fuelfinder/', views.fuelfinder, name='fuelfinder'),
    path('addstation/', views.addstation, name='addstation'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),   
]