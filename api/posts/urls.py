from cgitb import lookup
from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('instagram', views.PostViewSet,
                basename='post')
router.register('savedPosts', views.SavedPostsView,
                basename='saved')
router.register('tags', views.TagViewSet, basename='tags')
router.register('my_tags', views.MyTagsViewSet, basename='m_t')

urlpatterns = [
    path('', include(router.urls)),
    path('tagged_posts/<pk>/', views.TaggedPostsViewSet.as_view(), name = 'tp')
]