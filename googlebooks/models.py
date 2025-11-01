from django.db import models

class GoogleBook(models.Model):
    title = models.CharField(max_length=255, unique=True)
    authors = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    published_date = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)
    categories = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True)
    preview_link = models.URLField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
