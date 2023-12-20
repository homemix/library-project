from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostList, PostDetail, UserList, UserDetail, UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')
urlpatterns = router.urls

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
#     path('', PostList.as_view(), name='post_list'),
#     path('users/', UserList.as_view(), name='user_list'),
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]
