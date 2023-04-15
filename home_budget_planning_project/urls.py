from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include('home_budget_planning.urls')),
    path('api/', include('home_budget_planning.api.urls')),
    path('api/accounts/', include('accounts.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
