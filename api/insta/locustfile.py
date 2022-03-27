from unicodedata import name
from locust import HttpUser, task
from random import randint


class InstagramUser(HttpUser):
    @task(5)
    def view_posts(self):
        print('view_posts')
        self.client.get('/instagram', name='/instagram')

    @task(10)
    def create_post(self):
        self.client.post('/instagram/', name='/instagram',
                         json={'postContent': "hello"}
                         )

    @task(3)
    def view_post(self):
        print('view_post')
        post_id = randint(1, 100)
        self.client.get(f'/instagram/?p_id={post_id}/', name='/instagram/:id')

    @task(2)
    def view_comments(self):
        print('view_comments')
        post_id = randint(1, 100)
        self.client.get(
            f'/instagram/?p_id={post_id}/comments/', name='/instagram/:id/comments')

    @task(1)
    def view_comment(self):
        print('view_comment')
        post_id = randint(1, 100)
        comment_id = randint(1, 100)
        self.client.get(
            f'/instagram/?id={post_id}/comments/?comment_id={comment_id}/', name='/instagram/:id/comments/:id')

    # @task(20)
    # def create_comment(self):
    # Have not implemented it yet
       