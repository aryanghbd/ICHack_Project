from django.db import models
# For databases
# Create your models here.
# For when you add new fields to the db, how would you handle the previously inserted elements without the new field?
    # blank=False means field will be rendered as required,; 
    # null = True means field can be empty in the database (for previously inserted elements), default= "insert value that you want to populate the empty fields of existing elements"
class Product(models.Model):
    title = models.CharField(max_length=120);
    description = models.TextField(); 
    price = models.DecimalField(decimal_places=2,max_digits=1000 );
    summary = models.TextField(default="default summary");
    