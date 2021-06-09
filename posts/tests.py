from django.test import TestCase
from .models import *
from .forms import Publicar_Post_form
from django.contrib.auth.models import User


class PostTestCase(TestCase):

    def setUp(self):
        self.post = Publicar_Post.objects.create(creador='demo',
                                            comentarios='demo',
                                            correo='demo@gmail.com')

    def test_create_post_success(self):
        posts = Publicar_Post_form(data={"creador": self.post.creador,
                                         "comentarios": self.post.comentarios,
                                         "correo": self.post.correo})
        self.assertTrue(posts.is_valid())
        posts.save()

    def test_create_post_invalid_fields(self):
        posts = Publicar_Post_form(data={"creador":None, "comentarios": self.post.comentarios, "correo": self.post.correo})
        self.assertFalse(posts.is_valid())

    def test_update_post(self):
        post = Publicar_Post.objects.all().last()
        form = Publicar_Post_form(data={"creador": post.creador,
                                         "comentarios": post.comentarios,
                                         "correo": post.correo})
        self.assertTrue(form.is_valid())
        form.save()

    def test_update_post_invalid_fields(self):
        post = Publicar_Post.objects.all().last()
        form = Publicar_Post_form(data={"creador":None,
                                        "comentarios": post.comentarios,
                                        "correo": post.correo})
        self.assertFalse(form.is_valid())

    def test_update_post_not_found(self):
        with self.assertRaises(Publicar_Post.DoesNotExist):
            instancia = Publicar_Post.objects.get(pk=2)

    def test_delete_post(self):
      with self.assertRaises(Publicar_Post.DoesNotExist):
          pk= self.post.pk
          self.post.delete()
          instancia = Publicar_Post.objects.get(pk=pk)

    def test_delete_post_not_found(self):
        resp = True
        try:
            not_post = Publicar_Post.objects.get(id=3)
            if not_post:
                not_post.delete()
        except Publicar_Post.DoesNotExist:
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
