from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4 , editable=False , primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Question(BaseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="questions")
    question_text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question_text



class Answers(BaseModel):
    question = models.ForeignKey(Question , on_delete=models.CASCADE , related_name="answers")
    answer_text = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.answer_text


