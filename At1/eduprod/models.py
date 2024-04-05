from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    from django.db import models

class Question(models.Model):
    # Your existing fields
    question_text = models.CharField(max_length=200)
    # Add an image field for the question
    question_image = models.ImageField(upload_to='question_images/', null=True, blank=True)

class Answer(models.Model):
    # Your existing fields
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    # Add an image field for the answer
    answer_image = models.ImageField(upload_to='answer_images/', null=True, blank=True)
