from django.db import models

class StoryInfo(models.Model):
    storyName = models.CharField(max_length=64, null=True, blank=True)
    storyURL = models.CharField(max_length=64, null=True, blank=True)
    story = models.CharField( null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    verbcount = models.IntegerField(null=True, blank=True)
    adjective = models.IntegerField(null=True, blank=True)
    noun = models.IntegerField(null=True, blank=True)
    pronouns = models.IntegerField(null=True, blank=True)
    names = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"ID:{self.id} - {self.storyName}"
