from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('user/', include('userApp.urls')),
    path('page/', include('staticPageApp.urls')),
    path('project/', include('projectApp.urls')),
    path('group/', include('groupProjectApp.urls')),
    path('task/', include('taskApp.urls')),
    path('', schema_view),
]