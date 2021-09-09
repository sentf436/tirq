from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def str(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
