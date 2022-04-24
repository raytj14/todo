from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        db_table = 'book'

    title = models.CharField(verbose_name='タイトル', max_length=255, unique=True)

    price = models.IntegerField(verbose_name='価格', null=True, blank=True)

    def __str__(self):
        return self.title
