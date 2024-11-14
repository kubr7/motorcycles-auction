from django.contrib import admin
from auction.models import User, Brand, Category, Feature, Motorcycle, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Brand)
admin.site.register(Category)
# admin.site.register(EngineCapacity)
admin.site.register(Feature)
admin.site.register(Motorcycle)
admin.site.register(Bid)
admin.site.register(Comment)