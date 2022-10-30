from django.db import models

# Create your models here.


class Projects(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
