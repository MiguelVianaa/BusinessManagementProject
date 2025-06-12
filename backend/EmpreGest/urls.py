import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),

    path('', include('apps.home.urls')), # HOME

    path('empresas/', include(('apps.empresas.urls', 'empresas'), namespace='empresas')),
    path('setores/', include(('apps.setores.urls', 'setores'), namespace='setores')),
    # path('api/setores/', include('apps.setores.urls_api')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
