from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from datetime import date
from django.core.validators import RegexValidator


class User(AbstractUser):
    name = models.CharField(default="", max_length=20)
    firstName = models.CharField(default="", max_length=20)
    lastName = models.CharField(default="", max_length=20)
    dob = models.DateField()
    profile_picture = models.ImageField(
        upload_to="profile_pics/", null=True, blank=True
    )
    dob = models.DateField(default=date.today)
    mobileNo = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\d{10}$", message="Enter a valid 10-digit mobile number."
            )
        ],
        help_text="Enter your 10-digit mobile number",
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=255, help_text="Enter your address", null=True, blank=True
    )

    def full_name(self):
        return f"{self.firstName} {self.lastName}"

    def __str__(self):
        return self.username


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.category_name


# class EngineCapacity(models.Model):
#     capacity = models.CharField(max_length=50)

#     def __str__(self):
#         return self.capacity


class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Motorcycle(models.Model):
    COLOR_CHOICES = [
        ("", ""),
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Black", "Black"),
        ("White", "White"),
        ("Green", "Green"),
        ("Yellow", "Yellow"),
        ("Silver", "Silver"),
        ("Grey", "Grey"),
        ("Orange", "Orange"),
        ("Purple", "Purple"),
    ]

    CONDITION_CHOICES = [
        ("", ""),
        ("New", "New"),
        ("Used", "Used"),
        ("Restored", "Restored"),
        ("Salvage", "Salvage"),
    ]

    name = models.CharField(max_length=50)
    start_price = models.IntegerField(default=0)
    current_bid = models.OneToOneField(
        "Bid",
        related_name="current_bid",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, blank=True, null=True, related_name="brand"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="category",
    )
    # engine_capacity = models.ForeignKey(EngineCapacity, on_delete=models.SET_NULL, null=True, blank=True)
    cylinders = models.IntegerField(default=4)
    engine_capacity = models.FloatField(default=0)
    power = models.FloatField(default=0)
    torque = models.FloatField(default=0)
    mileage = models.FloatField(default=0)
    top_speed = models.IntegerField(default=0)
    fuel_capacity = models.FloatField(default=0)
    features = models.ManyToManyField(Feature, blank=True)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    image_url = models.CharField(max_length=1000)
    summary = models.CharField(max_length=1000)
    isActive = models.BooleanField(default=True)
    isExpired = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="user"
    )
    watchlist = models.ManyToManyField(
        User, blank=True, related_name="motorcycleWatchList"
    )
    collection = models.ManyToManyField(User, blank=True, related_name="collection")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    end_time = models.DateTimeField(default=timezone.now() + timedelta(minutes=40))

    def __str__(self):
        return self.name

    def get_winner(self):
        return self.current_bid.bidder if self.current_bid else None

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set end_time for new listings
            self.end_time = timezone.now() + timedelta(minutes=40)
        super().save(*args, **kwargs)

        if not self.current_bid:  # Only set initial price to bid_price if it's a new listing
            initial_bid = Bid.objects.create(
                bid_amount=self.start_price, bidder=self.owner, motorcycle=self
            )
            self.current_bid = initial_bid
            self.save()


class Bid(models.Model):
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, null=True)
    bidder = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="bidUser"
    )
    bid_amount = models.IntegerField(default=0)
    bid_time = models.DateTimeField(default=timezone.now, editable=False)

    # def __str__(self):
    #     return f"Bid {self.bid_amount} on {self.motorcycle.name} by {self.bidder.username}"
    def __str__(self):
        motorcycle_name = self.motorcycle.name if self.motorcycle else "None"
        bidder_username = self.bidder.username if self.bidder else "None"
        return f"Bid {self.bid_amount} on {motorcycle_name} by {bidder_username}"


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="userComment",
    )
    motorcycle = models.ForeignKey(
        Motorcycle,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="motorcycleComment",
    )
    message = models.CharField(max_length=200)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies"
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.author} comment on {self.motorcycle}"

    def get_all_replies(self):
        replies = []

        def recursive_replies(comment):
            for reply in comment.replies.all():
                replies.append(reply)
                recursive_replies(reply)

        recursive_replies(self)
        return replies

    # def get_all_replies(self):
    #     return Comment.objects.filter(parent=self).order_by('created_at')
