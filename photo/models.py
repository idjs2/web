from django.db import models

# Create your models here.
class Photo(models.Model) :
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    image = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.IntegerField()

class Todo(models.Model) :
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    created = models.DateTimeFiled(auto_now_add = True)
    complete = models.BooleanField(default = False)
    important = models.BooleanField(default = False)

    def __str_(self) :
        return self.title