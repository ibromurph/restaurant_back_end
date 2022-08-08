from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static, serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', include('content.urls')),
    path('booking/', include('booking.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Cafe Website"
admin.site.site_header = "Cafe Admin Panel"
admin.site.site_title = "Cafe Web App"
