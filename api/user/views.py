from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema


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
    Allow to retrieve, change and delete user.
    """
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer


class RegisterView(APIView):
    """
    Accepts user parameters.
    Creates a new user.
    """
    permission_classes = (permissions.AllowAny,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    authentication_classes = ()

    @swagger_auto_schema(request_body=NewUserSerializer)
    def post(self, request, format=None):
        serializer = NewUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer:
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data)


class BlacklistTokenUpdateView(APIView):
    """
    Adds refresh token to the blacklist
    """
    permission_classes = [AllowAny]
    authentication_classes = ()

    @swagger_auto_schema(request_body=TokenRefreshSerializer)
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
