from django.db import models

class Dozimetr(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dozimetry/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dose_power_range = models.CharField(max_length=100)
    dose_range = models.CharField(max_length=100)
    energy_range = models.CharField(max_length=100)
    error = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Radiometr(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='radiometry/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    alpha_range = models.CharField(max_length=100)
    beta_range = models.CharField(max_length=100)
    error = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Запрос от {self.name} ({self.email})"
