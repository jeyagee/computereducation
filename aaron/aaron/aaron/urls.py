"""aaron URL Configuration

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
from django.contrib import admin
from django.urls import path
from students import views
from django.urls import path

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('index',views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('course', views.course, name="course"),
    path('login', views.login, name="login"),
    path('forgot', views.forgot, name="forgot"),
    path('reset', views.reset, name="reset"),
    path('register', views.register, name="register"),
    path('studentdetails', views.studentdetails, name="studentdetails"),
    path('payment', views.payment, name="payment"),
    path('certificate', views.certificate, name="certificate"),
    path('exam', views.exam, name="exam"),
    path('display', views.display,name='display'),
    path('read', views.read,name='read'),
    path('display1',views.display1,name='display1'),
    path('read1',views.read1,name='read1'),
#     url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
#     url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
 ]
# urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
