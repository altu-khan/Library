from django.contrib import admin
from .models import Books # Model class import 


class BookAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'author', 'subject', 'pages'] # which model fileds to be displayed


admin.site.register(Books, BookAdmin) # Register model to admin panel
