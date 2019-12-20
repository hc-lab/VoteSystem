from django.db import models

# Create your models here.
class Person(models.model):
    name= models.CharField(max_length=50)
    surnames=models.CharField(max_length=60)
    dni=models.CharField(max_length=8)

    def __str__(self):
	       return self.name

# heredamos de Person
class Candidate(Person):
    political_party= models.CharField(max_length=50)

class RegisterCandidate(models.Model):
    date=models.DateTimeField()
    number=models.IntegerField()

class SufrageTable(models.Model):
    name= models.CharField(max_length=30)
    table_number= models.IntegerField()
    lounge_number=models.IntegerField()

class RegisterVote(models.Model):
    persons=models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
    sufrageTable= models.ForeignKey(sufrageTable, null=True, blank=True, on_delete=models.CASCADE)
    date= models.DateTimeField()
