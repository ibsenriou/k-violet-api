from django.test import TransactionTestCase

from rest_framework.test import APIClient

from src.core.models import CustomUser


AUTH_LOGIN_URL = "/api/auth/login/"

class AuthenticatedAPITestCase(TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.user = self.create_user()
        self.client = APIClient()
        resolved_permissions, user_filters = '', ''
        self.client.session['resolved_permissions'] = list(resolved_permissions)
        self.client.session['user_filters'] = user_filters
        self.client.session.modified = True
        self.client.session.save()
        self.client.post(AUTH_LOGIN_URL, {
            'email': 'admin@admin.com', 'password': 'admin'
        })
        self.client.force_authenticate(self.user)

    @staticmethod
    def create_user():
        user, _ = CustomUser.objects.get_or_create(
            email = 'admin@admin.com',
            first_name = 'Admin',
            last_name= 'Admin',
            is_active = True,
            is_staff = True,
            is_superuser = True,
            password = 'admin'
        )
        user.set_password('admin')
        user.save()

        return user

    def tearDown(self):
        super().tearDown()
        self.client.logout()
        self.client = None

