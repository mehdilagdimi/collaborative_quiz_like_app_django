from django.db import models

# Create your models here.
class Survey(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    numberOfSubmissions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=500)
    survey = models.ForeignKey(Survey, on_delete=models.SET_NULL, null=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    correctAnswer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer =  models.TextField()
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer
