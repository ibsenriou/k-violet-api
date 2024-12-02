from django.contrib.auth.models import User

from src.core.models import CustomUser


class AuthFactory:
    """
        This class is a container for helper functions that create 'Auth' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Auth' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")

    @staticmethod
    def create_user(email: str = 'username@username.com', password: str = 'password') -> User:
        user, created = CustomUser.objects.get_or_create(email='username@username.com')
        user.set_password(password)
        user.save()
        return user

    @staticmethod
    def create_test_user(username: str = 'testuser', password='12345') -> User:
        return User.objects.create_user(username=username, password=password)
