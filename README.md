# E-commerce-Product-API
Django REST Framework-based E-commerce Product API
The E-commerce Product API is designed to manage products on an e-commerce platform. It enables users to perform CRUD operations on products, categories, and users. The API also includes features such as authentication, search functionality, and filtering.
# E-commerce Product API Project Setup
    1 Clone the repository:
        git clone https://github.com/selam199/E-commerce-Product-API.git
        cd  E-commerce-Product-API/
    2 Install the required dependencies:
        pip install django djangorestframework
        pip install djangorestframework-authtoken
    3 Set up the MySQL database
    4 Configure the MySQL database connection
    5 Apply the database migrations
    6 Create a superuser to access the Django admin
    7 Run the development server
# Functional Requirements
##  Product Management (CRUD)
### Implement CRUD operations and create API endpoints for Products, Users, and Categories,Cart,CartItem,Order and OrderItem
- Added views, serializers, and URLs for managing Products
- Created user management endpoints for registration and authentication
- Set up Category model with endpoints for create, read, update, and delete operations
  Users can create, read, update, and delete products.
  -Install Django REST Framework
  Then, add 'rest_framework' to the INSTALLED_APPS in settings.py
       1.Create a Serializer
       2.Create Views
       3.Define URLs for CRUD Operations
       4.Include the URLs in ecommerce_api_project
## Category Model Attributes
1.name: CharField (max_length=255) - Name of the category.
2.description: TextField - Description of the category.
3.created_by: ForeignKey (User) - The user who created the category.
## Product Model Attributes
 1.name: CharField (max_length=255) 
 2.description: TextField 
 3.price: DecimalField (max_digits=10, decimal_places=2) 
 4.category: ForeignKey (Category) 
 5.created_by: ForeignKey (User) 
 6.stock_quantity: PositiveIntegerField 
 7.image_url: URLField (max_length=255, blank=True, null=True) 
 8.created_date: DateTimeField (auto_now_add=True) 
## Cart Model Attributes
  1.user:models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
  2.created_at = models.DateTimeField(auto_now_add=True)
  3.updated_at = models.DateTimeField(auto_now=True)
## CartItem Model Attributes
  1.cart:models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
  2.product:models.ForeignKey(Product, on_delete=models.CASCADE)
  3.quantity:models.PositiveIntegerField(default=1)
## Order Model Attributes
  1.user:models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders')
  2.created_at:models.DateTimeField(auto_now_add=True)
  3.status:models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
  4.total_amount:models.DecimalField(max_digits=10, decimal_places=2)
## OrderItem Model Attributes
  1.order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
  2.product = models.ForeignKey(Product, on_delete=models.PROTECT)
  3.quantity = models.PositiveIntegerField()
# Endpoints
## 1. API Endpoints Products for Model
   1.GET api/products/ - List all products.
   2.POST api/products/ - Create a new product.
   3.GET api/products/{id}/ - Retrieve a specific product by ID.
   4.PUT api/products/{id}/ - Update a product by ID.
   5.DELETE api/products/{id}/ - Delete a product by ID.
## 2. API Endpoints Category for Model
   1.GET api/categories/ - List all categories.
   2.POST api/categories/ - Create a new category.
   3.GET api/categories/{id}/ - Retrieve a specific category by ID.
   4.PUT api/categories/{id}/ - Update a category by ID.
   5.DELETE api/categories/{id}/ - Delete a category by ID.
## 3.API Endpoints for User Management
   1.POST api/register/ - Register a new user.
   2.POST api/auth/login/ - Authenticate a user.
   3.POST api/auth/logout/ - Log out a user.
   4.GET api/users/ - Retrieve details of the authenticated user.
## 4. Cart Management:
   1.Create, update, retrieve, and delete carts and cart items.
   2.Prevent duplicate items in the cart.
   ### API Endpoints for Cart Model
   1.GET /api/carts/: List all carts.
   2.POST /api/carts/: Create a new cart.
   3.GET /api/carts/{id}/: Retrieve details of a specific cart.
   4.PUT /api/carts/{id}/: Update a specific cart.
   5.DELETE /api/carts/{id}/: Delete a specific cart.
   ### API Endpoints for CartItem Model
   1.GET /api/cart-items/: List all cart items.
   2.POST /api/cart-items/: Create a new cart item.
   3.GET /api/cart-items/{id}/: Retrieve details of a specific cart item.
   4.PUT /api/cart-items/{id}/: Update a specific cart item.
   5.DELETE /api/cart-items/{id}/: Delete a specific cart item.
## 5.Order Management:
   1.Create, update, retrieve, and delete orders and order items.
   2.Track the status of orders (Pending, Completed, Failed).
   ### API Endpoints for Order Models
   1.GET /api/orders/: List all orders.
   2.POST /api/orders/: Create a new order.
   3.GET /api/orders/{id}/: Retrieve details of a specific order.
   4.PUT /api/orders/{id}/: Update a specific order.
   5.DELETE /api/orders/{id}/: Delete a specific order.  
   ### API Endpoints for OrderItem Models
   1.GET /api/order-items/: List all order items.
   2.POST /api/order-items/: Create a new order item.
   3.GET /api/order-items/{id}/: Retrieve details of a specific order item.
   4.PUT /api/order-items/{id}/: Update a specific order item.
   5.DELETE /api/order-items/{id}/: Delete a specific order item. 
#### **Links**
    [GitHub] (https://github.com/selam199/E-commerce-Product-API.git)
