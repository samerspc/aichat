from django.db import models

class Chat(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.text[:50]}...'
