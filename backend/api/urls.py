from django.urls import path, include

from rest_framework import routers

from . import views
from threads.views import ContentThreadViewSet, UserViewSet, CommentViewSet

from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'threads', ContentThreadViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test_endpoint'),
    # path('', views.getRoutes)
]