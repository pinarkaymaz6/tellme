from django.db import models

# Create your models here.



class Question(models.Model):
    q_title = models.CharField(max_length=100)
    q_text = models.CharField(max_length=300)
    q_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.q_title


class Answer(models.Model):
    a_text = models.CharField(max_length=300)
    a_date = models.DateTimeField('Date published')
    a_votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.a_text