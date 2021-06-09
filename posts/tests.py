from django.test import TestCase

import posts.models
from .models import Posts
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    def setUp(self):
        #Set up a model of type Post to be used in the tests
        #Previouly, Create the the instance of an User

        self.user = User.objects.create(username="TestUser")
        self.post = Posts.objects.create(title= "title1",
                                         content= "it post is used to practice Django test Lesson",
                                         creator= self.user)
        #import pdb;  pdb.set_trace()
        #post = Posts() ; post.save()

    '''def tearDown(self):
        #if self.post  or self.user != None:
        self.post.get(creator=self.user).delete()
        self.user.get(username="TestUser").delete()'''

        #import pdb;  pdb.set_trace()

    def test_create_post_success(self):
        setUpPost = {"title": str(self.post.title),
                     "content": str(self.post.content),
                     "creator": str(self.post.creator)}

        newPost = {"title": "title1",
                     "content": "it post is used to practice Django test Lesson",
                     "creator": "TestUser"}
        self.assertEqual(newPost, setUpPost)

    def test_create_post_invalid_fields(self):
        invalidPost = Posts.objects.create(title= "",
                                         content= "it post is used to practice Django test Lesson",
                                         creator= self.user,
                                         update_at= "June 9, 2021")

        #import pdb;  pdb.set_trace()
        self.assertTrue(invalidPost)

    def test_update_post(self):
        self.post.title = "title2"
        self.assertEqual(str(self.post.title),"title2")

    def test_update_post_invalid_fields(self):
        self.post.title = " Titulo mayor a 150 caracteres Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu"
        self.assertEqual(str(self.post.content), "it post is used to practice Django test Lesson")

    def test_update_post_not_found(self):
        postNotFound = Posts.objects.get(title="title2")
        #postNotFound = Posts.objects.get(title=" Titulo mayor a 150 caracteres Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu")
        #import pdb;  pdb.set_trace()
        #self.assertFalse((Posts.objects.get(title=" Titulo mayor a 150 caracteres Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec qu")), "post.models.Posts.DoesNotExist")

        if postNotFound.DoesNotExist:
            message=False
        else:
            message=True

        self.assertEqual(message, False)

    def test_delete_post(self):
        newPost = self.post
        newPost.title = "title2"
        newPost.delete()

        if newPost.DoesNotExist:
            False
        else:
            True

        self.assertFalse(False)


    def test_delete_post_not_found(self):
        newPost = Posts.objects.get(title="title2")
        if newPost.DoesNotExist:
            False
        else:
            True

        self.assertFalse(False)