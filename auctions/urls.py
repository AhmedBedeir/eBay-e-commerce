from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('category', views.category, name='category'),
    path("category/<str:title>", views.listCategory , name="listCategory"),
    path('listing/<int:id>', views.getItem, name='item'),
    path('create', views.createListing, name='create'),
    path('watchlist',views.watchList ,name='watchList'),
    path('listing/watch/add/<int:id>', views.addToWatchList, name='addToWatchList'),
    path('listing/watch/remove/<int:id>', views.removeFromWatchList, name='removeFromWatchList'),
    path('listing/unactive/<int:id>',views.unActiveList, name='unActiveList'),
    path('listing/closed', views.closedListing, name='closed'),
    path('listing/bid/<int:id>', views.placeBid, name='placeBid'),
    path('listing/comment/<int:id>', views.addComment, name='comment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)