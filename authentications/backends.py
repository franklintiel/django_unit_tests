from django.contrib.auth.models import User


class BaseAuthentication:

    def authenticate(self, username: str, password: str):
        if username is not None and password is not None:
            if username in ['demo', 'test'] and password in ['demo', 'test']:
                user = User(username=username, password=password)
                if self.is_user_active(user=user) is True:
                    return user
        return None

    def is_user_active(self, user: User):
        return True if user.username == 'demo' else False

    def get_token(self, user: User):
        if user is not None and user.username == 'demo':
            return 'adfasdfasdfsadfasd'
        return None
