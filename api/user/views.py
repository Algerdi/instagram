from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import NewUser
from .serializers import NewUserSerializer


class UserList(generics.ListAPIView):
    """
    Return a user list.
    """
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Return current user by id.
    """
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer


class RegisterView(APIView):
    """
    Accepts username, email and password.
    Create a new user.
    """
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]
    authentication_classes = ()

    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data)
