from django.urls import path
from .views import ImageListCreateView, ImageDetailView, PDFListCreateView, PDFDetailView

urlpatterns = [
    path('api/upload/', ImageListCreateView.as_view(), name='image-upload'),
    path('api/images/', ImageListCreateView.as_view(), name='image-list'),
    path('api/images/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('api/pdfs/', PDFListCreateView.as_view(), name='pdf-list'),
    path('api/pdfs/<int:pk>/', PDFDetailView.as_view(), name='pdf-detail'),
]
