from django.urls import path,include
from users.views import dashboard,register
from django.contrib.auth import views

from users.forms import UserLoginForm

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),


    
#     path('login/',views.LoginView.as_view(template_name="login.html",
#     authentication_form=UserLoginForm),
#     name='login'
# )
]
