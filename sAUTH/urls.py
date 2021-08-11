from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('rest_framework.urls')),

]
