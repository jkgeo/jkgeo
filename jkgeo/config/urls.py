"""jkgeo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from machina import urls as machina_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('posts/', include('posts.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('resume/', include('resume.urls')),
    path('projects/forum/', include(machina_urls)),
    path('projects/beers/', include('beers.urls')),
    path('projects/recipes/', include('recipes.urls')),
    path('projects/low-energy-league/', include('league.urls')),
    path('projects/library/', include('library.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
