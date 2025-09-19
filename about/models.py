from django.db import models


class About(models.Model):
    """Model for storing information about the author.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """


    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):
    """Model for storing collaboration requests.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """


    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
    