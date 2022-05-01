from django.db import models

# Create your models here.
class Todo(models.Model):
    """タスクモデル"""
    class Meta:
        db_table = 'todo'

    todo = models.CharField(verbose_name='Todo',  max_length=100, blank=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.todo