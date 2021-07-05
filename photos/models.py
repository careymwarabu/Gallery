from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class ImageCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, name):
        cls.objects.filter(id=id).update(name=name)


class ImageLocation(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.location_name}"

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
        
    @classmethod
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(name=name)



class Image(models.Model):
    image = CloudinaryField('photo')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    posted_at = models.DateField(auto_now_add=True)
    image_location = models.ForeignKey(ImageLocation, on_delete=models.CASCADE, null=True)
    image_category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.image_name}"

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        image_update = cls.objects.filter(id=id).update(image=image)

    @classmethod
    def get_image_by_id(cls, id):
        image = Image.objects.filter(id=id)
        return image

    @classmethod
    def search_image(cls, category):
        image = cls.objects.filter(image_category=category)
        return image
    
    @classmethod
    def search_by_location(cls, location):
        image = cls.objects.filter(image_location=location)
        return image

