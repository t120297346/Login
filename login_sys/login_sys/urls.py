from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from login import views

router = DefaultRouter()
router.register(r'login', views.LoginViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
