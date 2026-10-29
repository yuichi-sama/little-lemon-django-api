from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from restaurant.views import RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/registration/", RegisterView.as_view(), name="registration"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include("restaurant.urls")),
]
