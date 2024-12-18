from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAchievement(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_achievement = models.ForeignKey('Achievement', on_delete=models.CASCADE)
    is_claimed = models.BooleanField('Resgatado', default=False)

    class Meta:
        unique_together = ('fk_user', 'fk_achievement')
        verbose_name = 'Conquista do Usuário'
        verbose_name_plural = 'Conquistas dos Usuários'

    def __str__(self):
        return f"{self.fk_user} - {self.fk_achievement}"