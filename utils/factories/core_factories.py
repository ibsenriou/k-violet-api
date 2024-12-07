from src.core.models import CustomUser


class CoreFactory:
    """
        This class is a container for helper functions that create 'Core' objects for testing purposes.

        The main purpose of this class is to abstract the creation of 'Core' objects, reducing boilerplate code
        in test files and allowing for more complex testing.
    """

    def __new__(cls, *args, **kwargs):
        raise TypeError("This is a static class and cannot be instantiated")



    @staticmethod
    def create_custom_user(
            email: str = 'admin@admin.com',
            first_name: str = 'Admin',
            last_name: str = 'Admin',
            is_active: bool = True,
            is_staff: bool = True,
            is_superuser: bool = True,
            password: str = 'admin'
    ) -> CustomUser:
        custom_user, _ = CustomUser.objects.get_or_create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        custom_user.set_password(password)
        custom_user.save()

        return custom_user
