from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClothingCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ClothingItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clothing_items")
    category = models.ForeignKey(ClothingCategory, on_delete=models.SET_NULL, null=True, related_name="items")
    image = models.ImageField(upload_to="clothes/")
    color = models.CharField(max_length=30)
    style = models.CharField(max_length=50, blank=True, null=True)  # e.g., casual, formal
    brand = models.CharField(max_length=50, blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s {self.category.name} - {self.color}"

class Wardrobe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wardrobe")
    items = models.ManyToManyField(ClothingItem, related_name="in_wardrobes", blank=True)

    def __str__(self):
        return f"{self.user.username}'s Wardrobe"

class OutfitCombination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="outfit_combinations")
    clothing_items = models.ManyToManyField(ClothingItem, related_name="outfits")
    occasion = models.CharField(max_length=100, blank=True, null=True)  # e.g., daily wear, wedding
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"Outfit for {self.user.username} - {self.occasion or 'General'}"
