import uuid

from django.db import models

# Create your models here.
class movies_table(models.Model):
    moviesuuid=models.UUIDField(default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    generes=models.CharField(max_length=100)
    class Meta:
        db_table="movies table"

    def __str__(self):
        return str(self.moviesuuid) + self.title

class collections_table(models.Model):
    collectionsuuid=models.UUIDField(default=uuid.uuid4,editable=False)
    #collectionsuuid=models.IntegerField()
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    movies=models.ManyToManyField(movies_table)

    class Meta:
        db_table="collections table"
    def __str__(self):
        return str(self.collectionsuuid)+self.title
