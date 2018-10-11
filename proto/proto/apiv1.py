
from django.urls import path
from django.urls import include

urlpatterns = [
    path("", include("common.api.urls", namespace="common-api")),
    path("auth/", include("authentication.api.urls", namespace="authentication-api")),
    path("accounts/", include("account.api.urls", namespace="user-api")),
    path("yuyue/", include("yuyue.api.urls", namespace="yuyue-api")),
    path("suandao/", include("suandao.api.urls", namespace="suandao-api")),
]
