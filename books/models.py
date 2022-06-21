import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Publisher(models.Model):
    name = models.CharField(_("Name"), max_length=30)
    address = models.CharField(_("Address"), max_length=50)
    city = models.CharField(_("City"), max_length=60)
    state_province = models.CharField(_("Province"), max_length=30)
    country = models.CharField(_("Country"), max_length=50)
    website = models.URLField(_("Website"))
    
    
    class Meta:
        verbose_name = ("Publisher")
        verbose_name_plural = _("Publishers")
        
    def __str__(self):
        return f"{self.name} {self.city} {self.country}"


class Author(models.Model):
    first_name = models.CharField(_("First Name"), max_length=30)
    last_name = models.CharField(_("Last Name"), max_length=40)
    email = models.EmailField(_("Email"))


    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = _("Authors")
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
 
        
class Book(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    authors = models.ManyToManyField("books.Author", related_name="books")
    publisher = models.ForeignKey("books.Publisher", on_delete=models.CASCADE, related_name="books")
    classification = models.ForeignKey("books.Classification", on_delete=models.CASCADE, related_name="classifications")
    publication_date = models.DateField()


    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = _("Books")
        
    
    def was_published_recently(self):
        date_today = timezone.now().date()
        return self.publication_date >= date_today - datetime.timedelta(days=1)   
    
        
    def __str__(self):
        return f"{self.title}"
    

class Classification(models.Model):
    code = models.CharField(_("Code"), max_length=3)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
   
   
    class Meta:
        verbose_name = ("Classification")
        verbose_name_plural = _("Classifications")
        
    def __str__(self):
        return f"{self.code}"