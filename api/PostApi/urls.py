from django.urls import path
from .views import PostList, PostDetail, PostEdit, PostNew

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('edit/<int:pk>/', PostEdit.as_view(), name='post_edit'),
    path('new/', PostNew.as_view(), name='post_new'),
]
