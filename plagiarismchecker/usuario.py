from djongo import models

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.email
