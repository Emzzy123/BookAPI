from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Book
from .serializers import BookSerializer

# Custom pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Number of records per page
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.
class BookListCreateAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination  # Add pagination
    filter_backends = [filters.SearchFilter]  # Add filtering
    search_fields = ['title', 'author']  # Fields to filter by

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(title__icontains=name_filter)
        return queryset
