<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.test import TestCase
=======
from django.test import TestCase
from django.contrib.auth import get_user_model
>>>>>>> PREP
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
<<<<<<< HEAD
        username="testuser",
        email="test@email.com",
        password="secret",
        )
        cls.post = Post.objects.create(
        author=cls.user,
        title="A good title",
        body="Nice body content",
        )

=======
            username="testuser",
            email="test@email.com",
            password="secret", 
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content",
        )
    
>>>>>>> PREP
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
