from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
