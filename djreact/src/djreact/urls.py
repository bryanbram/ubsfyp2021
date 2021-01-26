"""djreact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('', include('frontend.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
]





# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls', namespace='blog')),
#     path('api/', include('blog_api.urls', namespace='blog_api')),
#     path('api/user/', include('users.urls', namespace='users')),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
