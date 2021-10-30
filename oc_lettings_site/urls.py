from django.contrib import admin
from django.urls import path, include
from lettings import urls as lettings
from lettings.views import index_home
from profiles import urls as profiles


urlpatterns = [
    path('', index_home, name='index'),
    path('lettings/', include(lettings, namespace="lettings")),
    path('profiles/', include(profiles, namespace='profiles')),
    path('admin/', admin.site.urls),
]
