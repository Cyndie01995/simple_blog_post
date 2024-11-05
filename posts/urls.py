from . import views
from django.urls import path

urlpatterns = [
    path('homepage/', views.homepage, name='posts_home'),
    # path('list-posts/', views.list_posts, name='posts_list'), #url for the function based view
    path('list-posts/', views.PostListCreateView.as_view(), name='list_posts'),
    # path('<int:post_id>', views.post_detail, name='posts_detail'),  # Replace <int:post_index> with the actual variable name for the post index.
    # path('update/<int:post_id>/', views.update_post, name='update_post'),
    # path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='post_retrieve_update'), #for class based api_view
    path('posts_for/', views.ListPostsForAuthor.as_view(), name='posts_for_current_user'), #for class based api_view
]