from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Product, Category,Cart, CartItem, Order, OrderItem
from .serializers import ProductSerializer, CategorySerializer, UserSerializer, RegisterSerializer,CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import ProductPagination  # Import custom pagination class
from rest_framework.authtoken.models import Token



# Create your views here.
# Product ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter 
    pagination_class = ProductPagination  # Apply pagination
    search_fields = ['name','description']
    ordering_fields = ['price', 'created_by']  # Enable sorting by price and creation date
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
# Category ViewSets
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def get_queryset(self):
        return Category.objects.filter(created_by=self.request.user)
# User ViewSets
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated] 
# Register API Methods
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Temporarily allow unauthenticated users
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            # Create Token For the new user
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED )    
        #return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # For Token Authentication: Delete the token from the DB
        if request.user.auth_token:
            request.user.auth_token.delete()

        # For Session Authentication: Flush the session (logout the user)
        request.session.flush()

        return Response({"message": "Successfully logged out."})   
# Cart ViewSet
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Cart Item ViewSet
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


# Order Item ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]