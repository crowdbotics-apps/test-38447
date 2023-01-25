from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OrderViewSet,SalesViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('sales', SalesViewSet )
router.register('order', OrderViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
