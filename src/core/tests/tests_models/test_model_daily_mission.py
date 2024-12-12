from django.test import TestCase

from src.core.models.model_daily_mission import DailyMission
from utils.factories.core_factories import CoreFactory


class DailyMissionTest(TestCase):
    ### SETUP ###
    def setUp(self) -> None:

        self.user = CoreFactory.create_custom_user()
        self.mission = DailyMission.objects.create(
            description='Comprar um café',
            points=10,
            is_completed=False,
            target_date='2024-12-01',
            fk_user=self.user
        )

    ### ATTRIBUTES TESTS ###
    def test_create_daily_mission(self):
        self.assertTrue(DailyMission.objects.exists())

    def test_created_daily_mission_has_description(self):
        self.assertEqual(self.mission.description, 'Comprar um café')

    def test_created_daily_mission_has_points(self):
        self.assertEqual(self.mission.points, 10)

    def test_created_daily_mission_has_is_completed(self):
        self.assertFalse(self.mission.is_completed)

    def test_created_daily_mission_has_target_date(self):
        self.assertEqual(self.mission.target_date, '2024-12-01')

    def test_created_daily_mission_has_fk_user(self):
        self.assertEqual(self.mission.fk_user, self.user)

    def test_created_daily_mission_has_verbose_name(self):
        self.assertEqual(DailyMission._meta.verbose_name, 'Missão Diária')

    def test_created_daily_mission_has_verbose_name_plural(self):
        self.assertEqual(DailyMission._meta.verbose_name_plural, 'Missões Diárias')

    def test_daily_mission_as_string(self):
        self.assertEqual(str(self.mission), 'Comprar um café')


    ### METHODS TESTS ###
    def test_complete_mission(self):
        self.mission.complete_mission()
        self.assertTrue(self.mission.is_completed)
        self.assertEqual(self.user.coins, 10)
        self.assertEqual(self.user.amassed_coins, 10)

    def test_completed_mission_cannot_be_completed_again(self):
        self.mission.complete_mission()
        with self.assertRaises(Exception):
            self.mission.complete_mission()

