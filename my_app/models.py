from django.db import models


# Create your models here.
class Search(models.Model):
    # It will hold the search text
    search = models.CharField(max_length=500)
    # It will hold the timestamp when the search was done
    created = models.DateTimeField(auto_now=True)

    # To show the actual search string
    def __str__(self):
        return '{}'.format(self.search)

    # To create plural for search with 'es'
    class Meta:
        verbose_name_plural = 'Searches'


