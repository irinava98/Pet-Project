from django.urls import path
from authors import views

urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('details/', views.AuthorDetailView.as_view(), name='author-details'),
    path('delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('edit/', views.AuthorEditView.as_view(), name='author-edit')
]

