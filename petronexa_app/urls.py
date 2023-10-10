from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'petronexa_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('blog/<int:det_id>/', views.blog, name='blog'),
    path('fuelfinder/', views.fuelfinder, name='fuelfinder'),
    path('addstation/', views.addstation, name='addstation'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='frontend/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),   
]