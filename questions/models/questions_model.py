import uuid

from django.db import models

vote_types = (
    ('UP_VOTE', 'UP_VOTE'),
    ('DOWN_VOTE', 'DOWN_VOTE'),
)


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
    is_question_deleted = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(
        max_length=200, unique=True, primary_key=True)


class Answer(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    body = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)


# class Test(models.Model):
#     field1 = models.IntegerField(blank=True)
#     field2 = models.IntegerField(null=True)
#     field3 = models.IntegerField(null=True, blank=True)

class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    body = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=20, choices=vote_types)


