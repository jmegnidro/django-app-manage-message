from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home, us

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('dashbord/', home, name='home'),
                  path('app/', include('app.urls')),
                  path('account/', include('account.urls')),
                  path('', us, name='us')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
