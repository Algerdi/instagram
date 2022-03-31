from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Post


class PostFixtures:
    def setup_post(self):
        self.post = {
            "description": "Description for test"
        }
        Post.objects.create(**self.post).save()

    def setup_post_list(self):
        self.posts_list = [
            {"description": "1"},
            {"description": "2"},
            {"description": "3"},
        ]


class PostModelTests(TestCase, PostFixtures):

    def test_post_db(self):
        self.setup_post()
        post = Post.objects.filter(description="Description for test")
        for post in post:
            self.assertTrue(post.created)
            self.assertTrue(post.id)
            self.assertEqual("Description for test", post.description)

    def test_list_post(self):
        """
        Send a request to get a posts list
        Expect to receive the same posts list as in the database
        """
        self.setup_post()
        self.setup_post_list()
        url = reverse('post_list')
        response = self.client.get(url)
        post = response.json()
        self.assertTrue(all(post.pop('id') for post in post))

    def test_get_post_by_id(self):
        """
        Get info of post by its ID
        """
        self.setup_post()
        self.setup_post_list()
        url = reverse('post_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        post = response.json()
        self.assertTrue(post.pop('id'))
        self.assertTrue(post.pop('created'))

    def test_post_absolute_url_with_200(self):
        """
        Checking for the presence of a post
        """
        self.setup_post()
        post = Post.objects.first()
        self.assertEqual(post.get_absolute_url(), '/posts/3/')
        response = self.client.get(post.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_details(self):
        """
        Checking for the existence of the post
        If it exists - 200
        The post doesn't exist - 404
        """
        self.setup_post()
        url = reverse('post_detail', kwargs={'pk': 5})
        response = self.client.get(url)
        no_response = self.client.get('/posts/100/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(no_response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertContains(response, 'description')
