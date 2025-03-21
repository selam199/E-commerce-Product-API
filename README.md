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
## Functional Requirements
## 1. Product Management (CRUD)
Implement CRUD operations and create API endpoints for Products, Users, and Categories
- Added views, serializers, and URLs for managing Products
- Created user management endpoints for registration and authentication
- Set up Category model with endpoints for create, read, update, and delete operations
   Users can create, read, update, and delete products. 
      1 Install Django REST Framework
          Then, add 'rest_framework' to the INSTALLED_APPS in settings.py
      2 Create a Product Serializer
      3 Create Product Views
      4 Define URLs for CRUD Operations
      5 Include the URLs in ecommerce_api_project
      6 Test the API
           GET api/products/ - List all products.
           POST api/products/ - Create a new product.
           GET api/products/{id}/ - Retrieve a specific product by ID.
           PUT api/products/{id}/ - Update a product by ID.
           DELETE api/products/{id}/ - Delete a product by ID
## Category Model Attributes        
- name: CharField (max_length=255) - Name of the category.
- description: TextField - Description of the category.
- created_by: ForeignKey (User) - The user who created the category.

## Product Model Attributes
- name: CharField (max_length=255) - Name of the product.
- description: TextField - Description of the product.
- price: DecimalField (max_digits=10, decimal_places=2) - Price of the product.
- category: ForeignKey (Category) - The category the product belongs to.
- created_by: ForeignKey (User) - The user who created the product.
- stock_quantity: PositiveIntegerField - Available stock quantity.
- image_url: URLField (max_length=255, blank=True, null=True) - Optional image URL for the product.
- created_date: DateTimeField (auto_now_add=True) - Timestamp when the product was created.
## Endpoints
1. Products
      GET api/products/ - List all products.
      POST api/products/ - Create a new product.
      GET api/products/{id}/ - Retrieve a specific product by ID.
      PUT api/products/{id}/ - Update a product by ID.
      DELETE api/products/{id}/ - Delete a product by ID.

2. Categories
      GET api/categories/ - List all categories.
      POST api/categories/ - Create a new category.
      GET api/categories/{id}/ - Retrieve a specific category by ID.
      PUT api/categories/{id}/ - Update a category by ID.
      DELETE api/categories/{id}/ - Delete a category by ID.

3. User Management
      POST api/register/ - Register a new user.
      POST /login/ - Authenticate a user and generate an authentication token.
      POST /logout/ - Log out a user by deleting their authentication token.
      GET api/user/ - Retrieve details of the authenticated user (requires token).