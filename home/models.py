from django.db import models
from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator

# Create your models here.
# contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10,
            validators=[RegexValidator(regex='^\d{10}$', message='Phone number must be entered in the format: \'1234567890\'')])
    desc = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=90, 
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skills"
        ordering = ['-rating']

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(help_text='Enter a brief description of the project')
    tech = models.CharField(max_length=100,help_text='Enter comma separated tech stack')
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='project/')
    link = models.URLField(max_length=200, help_text='Enter the link to the project',blank=True,null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['date']