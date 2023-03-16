from django.db import models


class poll(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)
    option4_count = models.IntegerField(default=0)

    def total(self):
        return self.option1_count + self.option2_count + self.option3_count + self.option4_count