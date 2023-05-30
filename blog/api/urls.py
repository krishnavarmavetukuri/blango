
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

from blog.api.views import UserDetail, TagViewSet, PostViewSet

from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("tags", TagViewSet)

router.register("posts", PostViewSet)

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    # ... other patterns omitted
    path("", include(router.urls)),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)




