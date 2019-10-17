"""image_upload URL Configuration

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
from django.urls import path, include  # 인클루두해야 밀어낼수있음
from django.conf.urls.static import static
from django.conf import settings  # MASTER_APP/settings.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsfeed/', include('sns.urls')),
    path('accounts/', include('accounts.urls')),
] 
# sns.urls로 포워딩해줌
# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
