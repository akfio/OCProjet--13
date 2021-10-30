from django.contrib import admin
from django.urls import path, include
from lettings import urls as lettings
from lettings.views import index_home
from profiles import urls as profiles


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', index_home, name='index'),
    path('lettings/', include(lettings, namespace="lettings")),
    path('profiles/', include(profiles, namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
