from django.db import models
from login.models import Account


# Create your models here.
class Items(models.Model):
    seller = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=100, blank=False, null=False)
    item_desc = models.TextField(blank=True, null=True)
    item_price = models.FloatField(blank=False, null=False)
    item_rating = models.FloatField(blank=True, default=0.0)
    item_img = models.ImageField(default='default.png', upload_to='item_images')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.item_name

class Cart(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='cart')
    items = models.JSONField(default=dict, blank=True)  # Dictionary to store items and quantities

    def __str__(self):
        return f"Cart for {self.account.user.username}"

    def add_item(self, item_id, quantity=1):
        """Add an item to the cart or update its quantity."""
        if item_id in self.items:
            self.items[item_id] += quantity
        else:
            self.items[item_id] = quantity
        self.save()

    def remove_item(self, item_id):
        """Remove an item from the cart."""
        if item_id in self.items:
            del self.items[item_id]
            self.save()

    def clear_cart(self):
        """Clear all items from the cart."""
        self.items = {}
        self.save()

    def get_total_items(self):
        """Return the total number of items in the cart."""
        return sum(self.items.values())

    def get_items(self):
        """Return the items in the cart as a dictionary."""
        return self.items
