from django.db import models

# Create your models here.
class Todo(models.Model):
    """タスクモデル"""
    class Meta:
        db_table = 'todo'
        
    todo = models.CharField('Todo',  max_length=100, blank=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('作成日時', auto_now=True)

    def __str__(self):
        return self.todo