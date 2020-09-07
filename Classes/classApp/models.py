from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(max_length=5000, default=0, blank=True, null=False)
    Instructor_Number = models.CharField(max_length=60, default=0, blank=True, null=False)
    Duration = models.FloatField(default=None, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.Title
