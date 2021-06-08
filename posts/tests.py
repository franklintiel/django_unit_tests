from django.test import TestCase
from .models import Post
from .forms import FormPost
from django.contrib.auth.models import User
from faker import Factory

fake = Factory.create()


class PostTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username=fake.user_name(),
                                        first_name=fake.first_name(),
                                        last_name=fake.last_name(),
                                        email=fake.ascii_company_email())

        self.post = Post.objects.create(user=self.user, text_content=fake.paragraph(nb_sentences=3))

    def tearDown(self):
        if self.user is not None:
            self.user.delete()
            self.post.delete()

    def test_create_post_success(self):
        form = FormPost(data={"user": self.user, "text_content": fake.paragraph(nb_sentences=3), "state": True})
        self.assertTrue(form.is_valid())
        form.save()

    def test_create_post_invalid_fields(self):
        form = FormPost(data={"user": None, "text_content": None, "state": False})
        self.assertFalse(form.is_valid())

    def test_update_post(self):
        post1 = Post.objects.all().last()
        form = FormPost(data={"user": post1.user,
                              "text_content": post1.text_content,
                              "state": False})
        self.assertTrue(form.is_valid())
        form.save()

    def test_update_post_invalid_fields(self):
        post1 = Post.objects.all().last()
        form = FormPost(data={"user": post1.user,
                              "text_content": '',
                              "state": True})
        self.assertFalse(form.is_valid())

    def test_update_post_not_found(self):
        resp = True
        try:
            last_post = Post.objects.get(id=2)
            if last_post:
                last_post.state = True
                last_post.save()
        except Post.DoesNotExist:
            resp = False
        self.assertFalse(resp)

    def test_delete_post(self):
        resp = True
        try:
            last_post = Post.objects.get(id=1)
            if last_post:
                last_post.delete()
        except Post.DoesNotExist:
            resp = False
        self.assertTrue(resp)

    def test_delete_post_not_found(self):
        resp = True
        try:
            last_post = Post.objects.get(id=2)
            if last_post:
                last_post.delete()
        except Post.DoesNotExist:
            resp = False
        self.assertFalse(resp)

    def test_publish_post(self):
        pass

    def test_publish_post_not_found(self):
        pass

    def test_publish_post_already_published(self):
        pass

    def test_lock_post(self):
        pass

    def test_lock_post_already_locked(self):
        pass

    def test_lock_post_not_found(self):
        pass

    def test_close_post(self):
        pass

    def test_close_post_not_found(self):
        pass

    def test_close_post_already_closed(self):
        pass

    def test_list_posts(self):
        pass

    def test_list_posts_empty(self):
        pass

    def test_publish_post_list(self):
        pass

    def test_publish_post_empty(self):
        pass

    def test_get_post(self):
        pass

    def test_get_post_not_found(self):
        pass

    def test_create_comments_success(self):
        pass

    def test_create_comments_post_not_found(self):
        pass

    def test_create_comments_invalid_fields(self):
        pass

    def test_response_comments(self):
        pass

    def test_response_comments_post_not_found(self):
        pass

    def test_response_comments_not_found(self):
        pass

    def test_list_publication_dates_by_post(self):
        pass

    def test_list_publication_dates_empty_by_post(self):
        pass

    def test_list_publication_dates_by_post_not_found(self):
        pass

    def test_create_publication_dates(self):
        pass

    def test_create_publication_dates_invalid_fields(self):
        pass

    def test_create_publication_dates_invalid_date_fields(self):
        pass

    def test_create_publication_dates_post_not_found(self):
        pass

    def test_update_publication_dates(self):
        pass

    def test_update_publication_dates_not_found(self):
        pass

    def test_update_publication_dates_post_not_found(self):
        pass

    def test_update_publication_dates_invalid_fields(self):
        pass

    def test_update_publication_dates_invalid_date_fields(self):
        pass

    def test_delete_publication_dates(self):
        pass

    def test_delete_publication_dates_not_found(self):
        pass

    def test_delete_publication_dates_post_not_found(self):
        pass

    def test_active_publication_dates(self):
        pass

    def test_active_publication_dates_not_found(self):
        pass

    def test_active_publication_dates_post_not_found(self):
        pass

    def test_active_publication_dates_already_active(self):
        pass

    def test_stop_publication_dates(self):
        pass

    def test_stop_publication_dates_not_found(self):
        pass

    def test_stop_publication_dates_post_not_found(self):
        pass

    def test_stop_publication_dates_already_active(self):
        pass

    def test_close_publication_dates(self):
        pass

    def test_close_publication_dates_not_found(self):
        pass

    def test_close_publication_dates_post_not_found(self):
        pass

    def test_close_publication_dates_already_active(self):
        pass

    def test_create_publication_after_create_post(self):
        pass

    def test_disable_post_on_unavailable_publication_access(self):
        pass

    def test_disable_post_on_available_publication_access(self):
        pass

    def test_validate_post_before_publish(self):
        pass

    def test_validate_post_before_publish_invalid(self):
        pass

    def test_validate_post_before_publish_invalid_not_dates(self):
        pass

    def test_validate_post_before_publish_invalid_without_images(self):
        pass

    def test_accept_only_images_png(self):
        pass

    def test_accept_only_images_invalid_extension(self):
        pass

    def test_upload_only_limit_images_by_post(self):
        pass

    def test_upload_only_limit_images_by_post_invalid(self):
        pass

    def test_create_image_from_post(self):
        pass

    def test_create_image_from_post_not_found(self):
        pass

    def test_create_image_from_post_invalid_fields(self):
        pass

    def test_delete_image_from_post(self):
        pass

    def test_delete_image_from_post_image_not_found(self):
        pass

    def test_delete_image_from_post_not_found(self):
        pass

    def test_creator_information_displayed_on_api(self):
        pass

    def test_creator_information_not_displayed_on_api(self):
        pass
