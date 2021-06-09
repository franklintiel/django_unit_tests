from unittest import TestCase

from rest_framework.authtoken.admin import User

from posts.post import Posts


class PostTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='admin2', first_name='John2',
                                        last_name='Doe2', email='info2@domain.com')
        self.user.set_password('admin123')
        self.user.save()

    def tearDown(self):
        if self.user != None:
            self.user.delete()

    def get_posts_class(self):
        return Posts()

    def test_create_post_success(self):
        post = self.get_posts_class()
        get_post = post.create_post(title='titulo',
                                    content='contenido',
                                    creator=self.user)
        self.assertTrue(get_post)

    def test_create_post_invalid_fields(self):
        post = self.get_posts_class()
        get_post = post.create_post(title=None,
                                    content='contenido',
                                    creator=self.user)
        self.assertFalse(get_post)

    def test_update_post(self):
        post = self.get_posts_class()
        post.create_post(title='titulo',
                         content='contenido',
                         creator=self.user)

        update_post = post.update_post(title='titulo', new_title='titulo cambiado')
        self.assertTrue(update_post)

    def test_update_post_invalid_fields(self):
        post = self.get_posts_class()
        post.create_post(title='probando',
                         content='admin123',
                         creator=self.user)

        update_post = post.update_post(title='probando', new_title=None)
        self.assertFalse(update_post)

    def test_update_post_not_found(self):
        post = self.get_posts_class()
        post.create_post(title='probando',
                         content='admin123',
                         creator=self.user)

        update_post = post.update_post(title='titulo', new_title='actualizar titulo')
        self.assertFalse(update_post)

    def test_delete_post(self):
        post = self.get_posts_class()
        post.create_post(title='probando',
                         content='admin123',
                         creator=self.user)

        delete_post = post.delete_post(title='probando')
        self.assertTrue(delete_post)

    def test_delete_post_not_found(self):
        post = self.get_posts_class()
        post.create_post(title='probando',
                         content='admin123',
                         creator=self.user)

        delete_post = post.delete_post(title='titulo')
        self.assertFalse(delete_post)

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
