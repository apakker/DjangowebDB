'''django2 version'''
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('avinashweb/', include('avinashweb.urls')),
    path('admin/', admin.site.urls),
]
