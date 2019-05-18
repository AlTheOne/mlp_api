""" Main URL Configuration in project mlp_api """

from django.contrib import admin
from django.urls import include, path

import mlp_api.urls_api_v1 as apiv1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_v1/', include(apiv1)),
]