from django.urls import path
from accounts.views import UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
   path("user/register/",UserRegisterView.as_view()),
   path("jwt/token/",TokenObtainPairView.as_view()),
   path("jwt/token/refresh/",TokenRefreshView.as_view())
]