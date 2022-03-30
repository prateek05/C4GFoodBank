"""food_bank_survey URL Configuration

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
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from campaigns import views as surveyViews

schema_url_patterns = [
    path(
        "api/survey/<str:campaign_id>/<str:site_id>", surveyViews.survey, name="survey"
    ),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Survey API",
        default_version="v1",
    ),
    patterns=schema_url_patterns,
)


def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("admin", admin.site.urls, name="admin"),
    path(
        "openapi/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="openapi-schema",
    ),
    path(
        "api/survey/<str:campaign_id>/<str:site_id>", surveyViews.survey, name="survey"
    ),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
    # re_path(r"^$", index),
    # re_path(r"^(?:.*)/?$", index),
]
