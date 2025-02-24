from django.db import models


NATIONALITY_CHOICE = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('OUTRA', 'Outra Nacionalidade'),
)

class Actor(models.Model):

    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100,choices=NATIONALITY_CHOICE,blank=True, null=True)


    def __str__(self):
        return self.name
    
