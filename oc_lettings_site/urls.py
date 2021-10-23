from django.contrib import admin
from django.urls import path, include
from lettings import urls as lettings
from profiles import urls as profiles
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(lettings, namespace="lettings")),
    path('profiles/', include(profiles, namespace='profiles')),
    path('admin/', admin.site.urls),
]
