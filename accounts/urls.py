from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
