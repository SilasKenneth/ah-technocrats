"""authors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='AUTHORS HAVEN API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('authors.apps.authentication.urls', "api-authenticate"), namespace='authentication')),
    path('api/docs/', schema_view, name='docs'),
    path('', schema_view, name='docs'),
    path('api/', include(('authors.apps.profiles.urls', 'api-profiles'), namespace='profiles')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/', include(('authors.apps.articles.urls', 'api-articles'), namespace='articles')),
    path('api/', include(('authors.apps.notifications.urls', 'api-notifications'), namespace='notifications')),

]
