from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BaseAuthentication:
    def authenticate(self, username: str, password: str):
        if username is not None and password is not None:
            user: User = self.get_user(username=username)
            if user is not None:
                if user.check_password(raw_password=password) is True \
                        and self.is_user_active(user=user) is True:
                    return user
        return None

    def get_user(self, username: str):
        return User.objects.filter(username=username).last()

    def is_user_active(self, user: User):
        return user.is_active

    def get_token(self, user: User) -> str or None:
        key: str = None
        try:
            token = Token.objects.get_or_create(user=user)
            key = token[0]
        except User.DoesNotExist as err:
            print(err)
        except Exception as err:
            print(err)
        return key
