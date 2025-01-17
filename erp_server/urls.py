"""erp_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastenvin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-api/', include('rest_framework.urls')),
    path('rest-swagger/', schema_view),
    
    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]

# admin/
# rest-auth/ ^password/reset/$ [name='rest_password_reset']
# rest-auth/ ^password/reset/confirm/$ [name='rest_password_reset_confirm']
# rest-auth/ ^login/$ [name='rest_login']
# rest-auth/ ^logout/$ [name='rest_logout']
# rest-auth/ ^user/$ [name='rest_user_details']
# rest-auth/ ^password/change/$ [name='rest_password_change']
# api-token-auth/
# api-token-refresh/
# api-token-verify/