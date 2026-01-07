from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rota de Login (Recebe user/senha -> Devolve Access + Refresh Token)
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # Rota de Refresh (Recebe Refresh Token -> Devolve novo Access Token)
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/products/", include("products.urls"), name="products"),
    # Rotas da Documentação (Swagger)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Interface visual (Swagger UI)
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Interface alternativa (Redoc)
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
