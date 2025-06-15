import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.setores.urls import router as setores_router

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),

    path('api/', include(setores_router.urls)),
    path('', include('apps.home.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)