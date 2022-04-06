from django.urls import path

from .views import UserList, UserDetail, RegisterView, BlacklistTokenUpdateView


urlpatterns = [
    path('', UserList.as_view(), name='list_users'),
    path('<int:pk>/', UserDetail.as_view(), name='get_user'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
