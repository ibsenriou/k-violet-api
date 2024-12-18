from django.db import models, IntegrityError
from django.contrib.auth import get_user_model

User = get_user_model()

class Achievement(models.Model):
    name = models.CharField('Nome da Conquista', max_length=100)
    description = models.TextField('Descrição', blank=True, null=True)
    target_points = models.PositiveIntegerField('Pontos Alvo')
    image = models.CharField('Imagem', max_length=100)
    unlocked_message = models.CharField('Mensagem Desbloqueada', max_length=255, blank=True, null=True)
    is_secret = models.BooleanField('Secreto', default=True)

    class Meta:
        verbose_name = 'Conquista'
        verbose_name_plural = 'Conquistas'

    def save(self, *args, **kwargs):
        # Check if the object is being created or updated
        is_new = self.pk is None
        super(Achievement, self).save(*args, **kwargs)

        # Proceed only if this is a new achievement being created
        if is_new:
            from src.core.models import UserAchievement

            # Fetch all users
            users = User.objects.all()

            # Create UserAchievement objects for each user if they don't already exist
            user_achievements = [
                UserAchievement(fk_user=user, fk_achievement=self)
                for user in users
                if not UserAchievement.objects.filter(fk_user=user, fk_achievement=self).exists()
            ]

            # Bulk create the UserAchievement objects
            UserAchievement.objects.bulk_create(user_achievements)


    def __str__(self):
        return self.name



