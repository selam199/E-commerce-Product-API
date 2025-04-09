from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CategoryViewSet, LogoutView,RegisterView,CartViewSet, CartItemViewSet, OrderViewSet, OrderItemViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),  # URL for user registration
    path('api-token-auth/', obtain_auth_token), #  login url for token authentications
    path('logout/', LogoutView.as_view(), name ='logout'), # logout url for token authentications
    path('auth/', include('rest_framework.urls')),   # Provides login/logout endpoints for the browsable API  
]