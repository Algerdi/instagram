from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import debug_toolbar
from user.views import RegisterView

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', include('comments.urls')),
    path('', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('user.urls'), name='user'),
    path('register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)