from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from faces.views import PersonDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', PersonDetailView.as_view(), name='article-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)