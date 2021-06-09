from django.contrib.auth.models import User

from posts.models import Post


class Posts:

    def create_post(self, title: str, content: str, creator: User) -> bool:
        if title is not None and content is not None:
            user: User = self.get_user(username=creator)
            if user is not None:
                Post.objects.create(title=title, content=content, creator=creator)
                return True
        return False

    def update_post(self, title: str, new_title: str):
        if title is not None and new_title is not None:
            obtain_post = self.get_post(title)
            if obtain_post is not None:
                obtain_post.title = new_title
                obtain_post.save()
                return True
        return False

    def delete_post(self, title: str):
        post = self.get_post(title)
        if post is not None:
            post.delete()
            return True
        return False

    def get_user(self, username: str) -> User:
        return User.objects.filter(username=username).last()

    def get_post(self, title: str):
        return Post.objects.filter(title=title).last()

