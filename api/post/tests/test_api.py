from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from post.models import Post
from post.serializers import PostSerializer
from user.models import NewUser


class GetPostSuccessfulTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        
        self.user = NewUser.objects.create_user(
            "testuser@user.com", 
            "testuser", 
            "firstname", 
            "qwerty"
        )
        self.post = Post.objects.create(
            author=self.user,
            description="Post description",
        )
    
    def test_get_post(self):
        """
        Given Post ID
        When user is unauthenticated
        and the Post with the ID is present
        Then return full data on this Post
            Post ID
            Post description
            Post creation date
            Post author
        """
        url = reverse('post_detail', kwargs={'pk': self.post.id})

        response = self.client.get(url, format='json')

        self.assertDictEqual(
            response.json(),
            PostSerializer(self.post).data
        )

class GetPostNotFoundTest(APITestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_get_post_not_found(self):
        """
        Given Post ID
        When the Post with such ID doesn't exist
        Then return error specifying the problem
        And HTTP status code equal to 404
        """
        url = reverse('post_detail', kwargs={'pk': 1})
        
        response = self.client.get(url, format='json')

        self.assertAlmostEqual(response.status_code, 404)
        self.assertAlmostEqual(response.json(), {'detail': 'Not found.'})
