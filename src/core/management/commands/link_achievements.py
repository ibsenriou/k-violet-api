from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from src.core.models import Achievement, UserAchievement

User = get_user_model()

class Command(BaseCommand):
    help = "Link all existing achievements to all users."

    def handle(self, *args, **kwargs):
        achievements = Achievement.objects.all()
        users = User.objects.all()

        # Keep track of created entries
        created_count = 0

        self.stdout.write(f"Linking {achievements.count()} achievements to {users.count()} users...")

        for user in users:
            for achievement in achievements:
                # Create UserAchievement only if it doesn't exist
                if not UserAchievement.objects.filter(fk_user=user, fk_achievement=achievement).exists():
                    UserAchievement.objects.create(fk_user=user, fk_achievement=achievement)
                    created_count += 1

        self.stdout.write(f"Successfully linked {created_count} new UserAchievement entries.")
