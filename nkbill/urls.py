"""nkbill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import path
from billmanage import views as billviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', billviews.dashboard, name='dashboard'),
    path('addbill', billviews.addbill, name='addbill'),
    path('records', billviews.records, name='records'),
    path('invoice/<int:billno>', billviews.invoice, name='invoice'),
    path('delete/<int:billno>', billviews.delete, name='delete'),
    path('addbill_submitted', billviews.addbill_submitted, name='addbill_submitted'),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
