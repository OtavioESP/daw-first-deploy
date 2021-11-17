from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()

router.register('produtos', views.ProdutosViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

