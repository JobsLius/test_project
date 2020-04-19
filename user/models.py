from django.db import models


# Create your models here.
class BookInfo(models.Model):
    class META:
        db_table = 'tb_books'

