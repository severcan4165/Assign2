from django.db import models

# Create your models here.
# class Category(models.Model):
#     id=models.OneToOneField( primary_key=True, on_delete=models.CASCADE)
#     name=models.CharField(max_length=30, null=False, blank=False)

#     def __str__(self):
#         return self.name

class Post(models.Model):
    # id=models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, primary_key=True)
    title=models.CharField(max_length=30)
    content=models.TextField(blank=True, null=True)
    category_id=models.PositiveBigIntegerField()
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now=True)
    updated_date=models.DateTimeField(auto_now_add=True)

