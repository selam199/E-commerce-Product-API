from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Allows clients to set custom page sizes
    max_page_size = 50  # Limits max page size to prevent overloading the API