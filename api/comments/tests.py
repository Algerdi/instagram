from django.test import TestCase
from .models import Post, User, Comment
import json
from rest_framework import status
from django.test import TestCase, Client
from .serializers import PostSerializer, CommentSerializer, SimpleCommentSerializer


# initialize the APIClient app
client = Client()


class PostTest(TestCase):
    """ Test module for Post model """

    def setUp(self):
        self.post = Post.objects.create(postContent='Create post 1')
        self.post1 = Post.objects.filter(pk=self.post.pk)
        self.post2 = Post.objects.create(postContent='Create post 2')
        self.posts = Post.objects.all()

    def test_create_post(self):
        self.assertEqual(
            str(self.post), 'Create post 1')
        self.assertEqual(
            str(self.post2), 'Create post 2')

    def test_view_posts(self):
        response = self.client.get('/instagram/')
        serializer = PostSerializer(self.posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_post(self):
        post_id = self.post.id
        response = self.client.get(f'/instagram/{post_id}/')
        post01 = Post.objects.get(pk=self.post.pk)
        serializer = PostSerializer(post01)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        post_id = self.post.id
        response = self.client.delete(f'/instagram/{post_id}/')
        self.assertEqual(response.status_code, 204)


class CommentTest(TestCase):
    def setUp(self):
        self.author1 = User.objects.create(name='kira')
        self.author2 = User.objects.create(name='sasha')
        self.p1 = Post.objects.create(postContent='Create post 1')
        self.p2 = Post.objects.create(postContent='Create post 2')
        self.comment1 = Comment.objects.create(
            author=self.author1, comment='First comment', post_id=self.p1.id)
        self.comment10 = Comment.objects.create(
            author=self.author1, comment='First+++ comment', post_id=self.p1.id)
        self.comment2 = Comment.objects.create(
            author=self.author2, comment='Second comment', post_id=self.p2.id)
        self.posts = Post.objects.all()

    def test_create_comment(self):
        self.assertEqual(
            str(self.comment1.author), 'kira')
        self.assertEqual(
            str(self.comment2.comment), 'Second comment')

    def test_view_comments(self):
        post01 = Post.objects.get(pk=self.p1.pk)
        comments01 = Comment.objects.filter(post=post01)
        response = self.client.get(f'/instagram/{post01.id}/comments/')
        serializer = SimpleCommentSerializer(comments01, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_comment(self):
        post01 = Post.objects.get(pk=self.p1.pk)
        comment1 = Comment.objects.filter(
            post=post01).get(pk=self.comment1.pk)
        response = self.client.get(
            f'/instagram/{post01.id}/comments/{comment1.id}', follow=True)
        serializer = SimpleCommentSerializer(comment1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        post01 = Post.objects.get(pk=self.p1.pk)
        comment1 = Comment.objects.filter(
            post=post01).get(pk=self.comment1.pk)
        response = self.client.delete(
            f'/instagram/{post01.id}/comments/{comment1.id}', follow=True)
        self.assertEqual(response.status_code, 200)
