
from django.contrib import admin
from django.urls import path,include, re_path
from django.contrib.auth.views import LoginView
from firstapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', LoginView.as_view(), name='login'),
    path('home', views.home, name="home"),
    path('register/', views.signup_view, name="sign_up"),
]
