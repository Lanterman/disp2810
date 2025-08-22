import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.models import Group

from . import settings


admin.site.unregister(Group)
admin.site.site_header = "Good project administration"
admin.site.site_title = "Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    #Apps
    path("", include("apps.urls"))
]

# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)