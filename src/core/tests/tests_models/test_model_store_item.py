from django.test import TestCase

from src.core.models import StoreItem
from src.core.models.model_daily_mission import DailyMission
from utils.factories.core_factories import CoreFactory


class StoreItemTest(TestCase):
    ### SETUP ###
    def setUp(self) -> None:

        # Create mock data
        self.mock_items = [
            {"name": "Vale Doce", "cost": 300, "image": "/images/little-store/icons/candy2.webp"},
            {"name": "Vale Brinquedo", "cost": 500, "image": "/images/little-store/icons/toy2.webp"},
            {"name": "Passeio no Parquinho", "cost": 100, "image": "/images/little-store/icons/park.webp"},
        ]
        for item in self.mock_items:
            StoreItem.objects.create(**item)

    ### ATTRIBUTES TESTS ###
    def test_create_store_item(self):
        self.assertTrue(StoreItem.objects.exists())

    def test_created_store_item_has_name(self):
        self.assertEqual(StoreItem.objects.first().name, 'Vale Doce')

    def test_created_store_item_has_cost(self):
        self.assertEqual(StoreItem.objects.first().cost, 300)

    def test_created_store_item_has_image(self):
        self.assertEqual(StoreItem.objects.first().image, '/images/little-store/icons/candy2.webp')

    def test_created_store_item_has_verbose_name(self):
        self.assertEqual(StoreItem._meta.verbose_name, 'Item da Loja')

    def test_created_store_item_has_verbose_name_plural(self):
        self.assertEqual(StoreItem._meta.verbose_name_plural, 'Itens da Loja')

    def test_store_item_as_string(self):
        self.assertEqual(str(StoreItem.objects.first()), 'Vale Doce')
