from django.db import models


class Books(models.Model): # Model Class for Book table name books_books
    title = models.CharField(max_length=60) # Char Text limit 255
    summary = models.TextField(max_length=250) # Text 
    author = models.CharField(max_length=35)
    publication_date = models.DateField(null=True)
    subject = models.CharField(max_length=60)
    publication = models.TextField(max_length=30)
    pages = models.IntegerField() # Integer number
   
