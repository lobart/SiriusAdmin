from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views import static

urlpatterns = [
    path('admin/', admin.site.urls),
]