import uuid

from django.db import models


class QuestionTag(models.Model):
    question = models.ForeignKey(
        'Question', on_delete=models.CASCADE)
    tag = models.ForeignKey(
        'Tag', on_delete=models.CASCADE)


class Question(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    title = models.CharField(
        max_length=300)
    body = models.TextField()


class Tag(models.Model):
    name = models.CharField(
        max_length=200, unique=True, primary_key=True)
