from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """Post model for storing blog posts.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)  # must exist
    status = models.IntegerField(choices=STATUS, default=0)  # must exist
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_on"]  # newest posts first

    def __str__(self):
        return self.title


# Comment model
class Comment(models.Model):
    """Comment model for storing blog comments.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """


    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']   # oldest comments first

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'       

