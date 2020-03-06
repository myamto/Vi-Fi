from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('sport_update.urls')),
    path('select/', include('sport_update.urls')),
    path('admin/', admin.site.urls),
]
