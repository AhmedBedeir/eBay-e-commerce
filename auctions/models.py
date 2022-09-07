from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listings(models.Model):
    categoryList = [
        ("fashion" , "Fashion"),
        ("toys" , "Toys"),
        ("electronics" , "Electronics"),
        ("watches" , "Watches"),
        ("other", "Other"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=('Title'))
    description = models.TextField()
    photo = models.ImageField(upload_to = 'listing', default = './images/default.png', null = True, blank = True)
    active = models.BooleanField(default=True)
    startingBid = models.DecimalField(max_digits=9, decimal_places=2, default= 1)
    category = models.CharField(max_length=50, choices= categoryList)
    createdOn = models.DateTimeField(auto_now_add= True)
    watchList = models.ManyToManyField(User, related_name='watchList', blank= True)
    winner = models.ForeignKey(User,on_delete=models.SET_NULL,  related_name="wins", null=True, blank=True)
    
    def __str__(self):
        return self.title

# make bids models to store list and user and price for this list
class Bids(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'bids')
    item = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='bids')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta:
        ordering = ['-price']

    
    def __str__(self):
        return self.owner.username + " paid " + str(self.price) + " to " + self.item.title

class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    item = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    createdOn = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.creator.username + ' comment in ' + self.item.title + ' at ' + str(self.createdOn)
    