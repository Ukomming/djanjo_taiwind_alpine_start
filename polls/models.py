from django.db import models

# Create your models here.

class Home(models.Model):
    """Model definition for Home."""

    # TODO: Define fields here
    Title = models.CharField( max_length=50)
    Body = models.TextField()

 

    def __str__(self):
        """Unicode representation of Home."""
        return self.Title
