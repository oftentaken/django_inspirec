from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery_images/')

    optimized_image = models.ImageField(upload_to='gallery_images/optimized/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and not self.optimized_image:
            self.create_optimized_image()

    def create_optimized_image(self):
        # Open the original image using Pillow
        img = PILImage.open(self.image.path)

        # Perform image optimization and resizing here
        # For example, resize the image to a specific width and height:
        img.thumbnail((800, 800))

        # Save the optimized image
        optimized_image_path = self.image.path.replace("gallery_images", "gallery_images/optimized")
        img.save(optimized_image_path, 'JPEG', quality=90)

        # Update the optimized_image field with the path to the optimized image
        self.optimized_image.name = optimized_image_path.split('/')[-1]
        self.save()