from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.shortcuts import redirect
from VENDAS_app.views import (
    
    ClienteViewSet,
    ProdutoViewSet,
    VendaViewSet,
    ItenvendaViewSet,
    home
)

# Criando o router da API
router = DefaultRouter()

router.register(r'cliente', ClienteViewSet, basename='cliente')
router.register(r'produto', ProdutoViewSet, basename='produto')
router.register(r'venda', VendaViewSet, basename='venda')
router.register(r'itenvenda', ItenvendaViewSet, basename='itenvenda')

# URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls),              # Admin Django
    path('', home, name='home'),                  # Raiz do site
    path('ADUMI/api/', include(router.urls)),    # API com interface web interativa
]
