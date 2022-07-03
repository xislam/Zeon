"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

from root import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Zeon IT hub API Docs.",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/", include("news.urls")),
    path("api/", include("career.urls")),
    path("api/", include("feedback.urls")),
    path("api/", include("quiz_answers.urls")),
    path("quiz/", include("quiz.urls", namespace="quiz")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]
