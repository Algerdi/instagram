from rest_framework import generics, status
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostNew(APIView):
    def post(self, request):
        serializers = PostSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        if serializers:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.data)
