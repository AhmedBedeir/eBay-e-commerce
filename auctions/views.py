from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Max
from .models import User,Listings, Bids, Comment
from .forms import newListing, itemBids
from django.contrib import messages

def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listings.objects.filter(active = True),
        'title': 'Active Listings',
        
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# to show a details of one list
def getItem(request, id):
    try:
        item = Listings.objects.get(id = id)
        maxPrice = item.bids.all().aggregate(Max('price'))
        numberBids = item.bids.all().count()
        return render(request, 'auctions/item.html',{
            'item': item,
            'maxPrice': maxPrice,
            'getPrice': itemBids,
            'numberBids': numberBids,
            
         })
    except:
        return render(request, 'auctions/404.html')

@login_required(login_url='/login')
def createListing(request):
    if request.method == "POST":
        form = newListing(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            listing = Listings(owner = request.user, title = data['title'], description = data['description'],
                                 category = data['category'], active = data['active'], photo = data['photo'])
            if data['startingBid'] > 0:
                listing.startingBid = data['startingBid']
            listing.save()
            messages.success(request, 'list added successfully ^_^')
            return redirect(reverse('index'))
        else:
            return render(request, 'auctions/create.html', {
                'form': newListing(),
                'error': 'invalid Data..!'
            })    
    else:
        return render(request, 'auctions/create.html', {
            'form': newListing()
        })

def category(request):
    return render(request, 'auctions/category.html')

def listCategory(request, title):
    return render(request, 'auctions/listCategory.html', {
        "allListOfThisCategory": Listings.objects.filter(category = title.lower(), active = True),
        "title": title,
    })

@login_required(login_url='/login')
def watchList(request):
    return render(request, 'auctions/watchList.html', {
        'watchList': User.objects.get(id = request.user.id).watchList.all()
    })

def addToWatchList(request, id):
    
    if request.method == 'POST':
        Listings.objects.get(id = id).watchList.add(request.user)
        request.session['added'] = True
    return redirect(reverse('item', args=[id]))

def removeFromWatchList(request, id):
    if request.method == 'POST':
        Listings.objects.get(id = id).watchList.remove(request.user)
        request.session['added'] = False
    return redirect(reverse('item', args=[id]))

# to make list un active with id of this list
def unActiveList(request, id):
    if request.method == 'POST':
        item = Listings.objects.get(id=id)
        item.active = False
        if item.bids.count() != 0:
            item.winner = item.bids.first().owner
        item.save()
    return redirect(reverse('index'))

# page for closed listings
def closedListing(request):
    return render(request, 'auctions/closed.html',{
        'listings': Listings.objects.filter(active = False),
        'title': "Closed Listing",
        'unActive': 'Closed',
    })

def placeBid(request, id):
    if request.method == 'POST':
        form = itemBids(request.POST)
        if form.is_valid():
            price = form.cleaned_data['getPrice']
            item = Listings.objects.get(id = id)
            currentPrice = item.bids.all().aggregate(Max('price')).get('price__max', 0.00)
            print(currentPrice)
            if currentPrice == None and price <= item.startingBid:
                messages.error(request, f'Price should greater than current price (${item.startingBid})')
            elif currentPrice != None and price <= currentPrice:
                messages.error(request, f'Price should greater than current price (${currentPrice})')
            else:
                newBid = Bids(owner = request.user, item = item, price = price )
                newBid.save()
                messages.success(request, 'Done, Your Bid is the greatest Bid.')
    return redirect(reverse('item', args=[id]))

def addComment(request, id):
    if request.method == 'POST':
        content = request.POST['comment']
        item = Listings.objects.get(id = id)
        newComment = Comment(creator = request.user, item = item, content = content)
        newComment.save()
    return redirect(reverse('item', args=[id]))
        