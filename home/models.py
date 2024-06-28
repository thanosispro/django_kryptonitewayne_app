from django.db import models
from django.utils import timezone
# Create your models here.
class games(models.Model):
    games_id=models.AutoField(primary_key=True)
    heading=models.CharField(max_length=200,default='')
    content=models.TextField()
    image=models.ImageField(upload_to='images/',default='')
    date=models.DateField(auto_now_add=True)
    search=models.CharField(max_length=3000,default='')
    download_url=models.CharField(max_length=2000,default='')
    total_views=models.IntegerField(default=0)
    category=models.CharField(max_length=200,default='')
    date=models.DateTimeField(timezone.now())
    def __str__(self):
        return self.heading
    

class comments(models.Model):
    comments_id=models.AutoField(primary_key=True)
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    comment_id=models.ForeignKey(games,on_delete=models.CASCADE)
    
    person=models.CharField(max_length=200,default='')

    def __str__(self):
        return self.comment + ' by ' +self.person
    
class replies(models.Model):
    replies_id=models.AutoField(primary_key=True)
    reply=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    reply_id=models.ForeignKey(comments,on_delete=models.CASCADE)
    person=models.CharField(max_length=200,default='')

    def __str__(self): 
        return self.reply + 'by' + self.person