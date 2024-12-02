from django.test import TransactionTestCase

from rest_framework.test import APIClient
from rest_framework.reverse import reverse_lazy

from src.core.models import CustomUser
from src.access_control.models import Role, RolePermission, UserRole

AUTH_LOGIN_URL = "/api/auth/login/"

class AuthenticatedAPITestCase(TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.user = self.create_user()
        self.client = APIClient()
        resolved_permissions, user_filters = UserRole.get_permissions(self.user)
        self.client.session['resolved_permissions'] = list(resolved_permissions)
        self.client.session['user_filters'] = user_filters
        self.client.session.modified = True
        self.client.session.save()
        self.client.post(AUTH_LOGIN_URL, {
            'email': 'admin@admin.com', 'password': 'admin'
        })
        # self.client.force_authenticate(self.user)

    @staticmethod
    def create_user():
        user, _ = CustomUser.objects.get_or_create(
            email='admin@admin.com',
            password='admin',
        )
        user.set_password('admin')
        user.save()
        
        # Clear all roles
        UserRole.objects.all().delete()
        RolePermission.objects.all().delete()
        Role.objects.all().delete()

        # Create global roles
        sindicator = Role.objects.create(name='Sindico', is_global=True)

        # Create global role permissions
        RolePermission.objects.create(fk_role=sindicator, permission='condominium.*:*')
        RolePermission.objects.create(fk_role=sindicator, permission='people.*:*')
        RolePermission.objects.create(fk_role=sindicator, permission='access_control.*:*')

        # Create global user roles
        UserRole.objects.create(fk_user_id=str(user.id), fk_role=sindicator)
        return user

    def tearDown(self):
        super().tearDown()
        self.client.logout()
        self.client = None

