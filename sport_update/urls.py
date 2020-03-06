from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooter, name='rooter'),
    path('select/', views.playerSelect, name='select'),
    path('admin/', admin.site.urls),
]
