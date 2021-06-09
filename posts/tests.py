from django.test import TestCase
from .models import Post
from posts import posts
from django.contrib.auth.models import User
from .posts import postestings

class PostTestCase(TestCase):

    def test_create_post_success(self):
        post=postestings.create_post(title='ESTE ES EL TITULO', content='Soy el contenido de este post de Maryori Sabalza', created_at='08:06:2021', creator='Maryori Sabalza')
        self.assertEqual(post)
        post.save()

    def test_create_post_invalid_fields(self):
        post=postestings.create_post(title=None, content=None, created_at='08:06:2021', creator='Maryori Sabalza')
        self.assertEqual(post)
    
    def test_update_post(self):
        post=postestings.update_post(content='Nuevo contenido', created_at='09:06:2021')
        self.assertEqual(post)
        post.save()

    def test_update_post_invalid_fields(self):
        post=postestings.update_post(content=None, created_at=None)
        self.assertEqual(post)

    def test_update_post_not_found(self):
        post=postestings.update_post(title='este post existe')
        self.assertEqual(post.not_found)
        self.assertEqual(response.status_code, 404)

    def test_delete_post(self):
        post=postestings.update_post(title='ESTE ES EL TITULO',)
        self.assertEqual(post.delete())


    def test_delete_post_not_found(self):
        post=postestings.update_post(title='este post existe')
        self.assertEqual(response.status_code, 404)

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
