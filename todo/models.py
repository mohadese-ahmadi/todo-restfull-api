from django.db import models

# Create your models here.
class Todomodel(models.Model):
    title=models.CharField(max_length=30, verbose_name='tile of duty')
    priority=models.IntegerField(verbose_name='how important?')
    is_done=models.BooleanField(verbose_name='Finished?', default=0)
    content=models.TextField()
    class Meta:
        db_table="Todos"