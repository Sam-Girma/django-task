from django.urls import path, include
from .views import signup, login, login_view, signup_view


urlpatterns = [
    path('signupw/', signup_view, name='signupw'),
    path('loginw/', login_view, name='loginw'),

    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('accounts/', include('allauth.urls')),
]
