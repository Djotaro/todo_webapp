from django.db import models

class ToDo(models.Model):
    title = models.CharField('Название задачи', max_length=500)
    is_complete = models.BooleanField('Завершено', default=False)
    specific_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.titled