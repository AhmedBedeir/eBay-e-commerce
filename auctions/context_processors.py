from .models import User, Listings

def numbers(request):
  return{
    'numberClosed': Listings.objects.filter(active = False).count,
    'numberActive': Listings.objects.filter(active = True).count,
  }