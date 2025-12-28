# resume_builder_project/urls.py (The definitive, working content)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 🛑 All custom DRF imports, DefaultRouter creation, and router.register calls MUST BE REMOVED from this file! 🛑

urlpatterns = [
    path('admin/', admin.site.urls),
    # Standard Django authentication URLs (for login/logout)
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # This single line handles ALL URL traffic for your app (Experiments, React, API)
    path('', include('resumesite.urls')), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
