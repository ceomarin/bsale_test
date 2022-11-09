from django.urls import path,include
from rest_framework import routers
from .views import CategoriaViewset,ProductoViewset

router = routers.DefaultRouter()
router.register('producto',ProductoViewset)
router.register('categoria',CategoriaViewset)


# localhost:8000/api/producto
urlpatterns = [
    path('api/', include(router.urls)),
]