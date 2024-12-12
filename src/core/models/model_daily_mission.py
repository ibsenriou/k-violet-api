from django.db import models

class DailyMission(models.Model):
    description = models.CharField('Descrição', max_length=255)
    points = models.PositiveSmallIntegerField('Pontos', default=0)
    is_completed = models.BooleanField('Concluída', default=False)

    target_date = models.DateField('Data Alvo')
    fk_user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return self.description

    def complete_mission(self):
        """
        Completes the mission and adds the points to the user's total points.
        :return: Int
        """

        # If the mission is already completed, return 0
        if self.is_completed:
            raise Exception('Missão já concluída')

        user = self.fk_user
        user.coins += self.points
        user.amassed_coins += self.points
        user.save()

        self.is_completed = True
        self.save()

        return 1


    class Meta:
        verbose_name = 'Missão Diária'
        verbose_name_plural = 'Missões Diárias'
