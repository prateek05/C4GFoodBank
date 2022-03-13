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
from django.urls import re_path as url
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from campaigns import views as surveyViews



schema_url_patterns = [
    path("api/survey", surveyViews.survey, name="survey"),
]

schema_view = get_swagger_view(title="Survey API", patterns=schema_url_patterns)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("openapi/", schema_view, name="openapi-schema"),
    path("api/survey/<str:campaign_id>/<str:site_id>", surveyViews.survey, name="survey"),
]
