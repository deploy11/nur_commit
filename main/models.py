from django.db import models
# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)    
    body = models.CharField(max_length=150)
    date  = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "Comment of " + str(self.author.username)