from django.contrib import admin
from django.urls import path, include
from examenpractico1 import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register('transporte',views.TransporteViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
