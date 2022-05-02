from unicodedata import name
from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('instagram', views.PostViewSet,
                basename='instagram')

comments_router = routers.NestedSimpleRouter(
    router, parent_prefix='instagram', lookup='p')
comments_router.register('comments', views.CommentViewSet,
                         basename='p-comments')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
]
