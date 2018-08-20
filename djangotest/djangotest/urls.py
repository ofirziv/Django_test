"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

import newsletter.views as newsletter_views 
import djangotest.views as djangotest_views

urlpatterns = [
	url(r'^$', newsletter_views.home, name='home'),
	url(r'^contact/', newsletter_views.contact, name='contact'),
    url(r'^blablabla/', djangotest_views.about, name='about'),
	url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # path('', newsletter.views.home, name='home'),

]
    

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)