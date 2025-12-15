from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Rota de Login (Recebe user/senha -> Devolve Access + Refresh Token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Rota de Refresh (Recebe Refresh Token -> Devolve novo Access Token)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
