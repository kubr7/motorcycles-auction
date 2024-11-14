from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("activelisting/", views.active_listing, name="active_listing"),
    path("accounts/login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("motorcycle/<str:name>/", views.motorcycle, name="motorcycle"),
    path("addWatchList/<str:name>/", views.addWatchList, name="addWatchList"),
    path('add_comment/<str:name>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path("removeWatchList/<str:name>/", views.removeWatchList, name="removeWatchList"),
    path('users/', views.users, name='users'),
    path('motorcycle/<str:name>/bids/', views.listing_bids, name='listing_bids'),
    path('bids/', views.all_bids, name='all_bids'),
    path('<str:username>/profile/edit/', views.edit_profile, name='edit_profile'), 
    path("filter-result", views.filter_result, name="filter_result"),
    path('<str:username>/collection/', views.collection, name='collection'),
    path('<str:username>/listing/', views.user_listings, name='user_listings'),
    path('close_auction/<str:name>/', views.close_auction, name='close_auction'),
    path("<str:username>/watchlist/", views.watchlist, name="watchlist"),
    path("<str:username>/profile/", views.user_profile, name="user_profile"),
]