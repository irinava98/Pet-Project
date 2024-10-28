from django.urls import path, include
from posts import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/', include([
        path('edit/', views.PostEditView.as_view(), name='post-edit'),
        path('details/', views.PostDetailView.as_view(), name='post-details'),
        path('delete/', views.PostDeleteView.as_view(), name='post-delete'),
    ]))
]




