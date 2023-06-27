from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from firstapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', LoginView.as_view(), name='login'),
    path('home', views.home, name="home"),
    path('register/', views.signup_view, name="sign_up"),
    path('profile/', views.profile, name="profile"),
    path('ui-elements/', views.ui_elements, name="ui_elements"),
    path('update/', views.profile_update, name="update"),
    path('disable/<str:id>/', views.disable_user, name="disable_user"),
    path('theme', views.theme, name="theme"),
    path('social-auth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
