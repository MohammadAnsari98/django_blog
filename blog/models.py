from django.db import models
# from django.utils import timezone
import django

class Post(models.Model):
    post_author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    post_title=models.CharField(max_length=200)
    post_text=models.TextField()
    created_date=models.DateTimeField(default=django.utils.timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
