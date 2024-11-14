from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseBadRequest,
    Http404,
    HttpResponseForbidden,
)
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction
from auction.models import User, Brand, Category, Motorcycle, Bid, Comment

from .forms import (
    RegistrationForm,
    CreateListingForm,
    LoginForm,
    UserProfileForm,
    CommentForm,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Max
from django.core.paginator import Paginator


def index(request):
    site_name = "Motorcycles Auction Club"
    allCategories = Category.objects.all()
    allBrands = Brand.objects.all()
    recentListedMotorcycles = Motorcycle.objects.filter(isExpired=False).order_by('-created_at')
    print(f"Recent: {recentListedMotorcycles}")
    for bra in allBrands:
        print(bra)

    for cat in allCategories:
        print(cat)

    return render(
        request,
        "auction/index.html",
        {
            "site_name": site_name,
            "categories": allCategories,
            "brands": allBrands,
            "recentlisted": recentListedMotorcycles,
        },
    )


def active_listing(request):
    site_name = "Motorcycles Auction Club"

    # activeListings = Listing.objects.filter(isActive=True)
    activeListings = Motorcycle.objects.filter(isActive=True).order_by("-id")
    allCategories = Category.objects.all()
    allBrands = Brand.objects.all()

    for listing in activeListings:
        print(listing.name, listing.created_at)

    paginator = Paginator(activeListings, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "auction/active_listing.html",
        {
            "site_name": site_name,
            "motorcycles": page_obj,
            "categories": allCategories,
            "brands": allBrands,
        },
    )


# def displayBrand(request):
#     if request.method == "POST":
#         # Retrieve the 'brand' parameter from the POST data
#         brandFromForm = request.POST.get("brand")

#         # Use get_object_or_404 for better error handling
#         brand = get_object_or_404(Brand, brandName=brandFromForm)

#         # Use select_related to fetch related objects efficiently
#         activeListings = Listing.objects.filter(
#             isActive=True, brand=brand
#         ).select_related("brand")

#         # Retrieve all Brand objects from the database
#         allBrands = Brand.objects.all()

#         # Render the 'auction/index.html' template with the data
#         return render(
#             request,
#             "auction/active_listing.html",
#             {"listings": activeListings, "brands": allBrands},
#         )


def filter_result(request):
    site_name = "Motorcycles Auction Club"
    if request.method == "POST":
        brands = request.POST.getlist("brand")
        categories = request.POST.getlist("category")
        search_query = request.POST.get("search_query", "").strip()

        print(f"Selected Brands: {brands}")
        print(f"Selected Categories: {categories}")
        print(f"Search Query: {search_query}")
        print(f"Form POST Data: {request.POST}")

        # Remove empty strings from categories list
        categories = [cat for cat in categories if cat.strip()]
        brands = [bra for bra in brands if bra.strip()]

        # Check if both brands and categories are empty
        if not brands and not categories and not search_query:
            return render(
                request,
                "auction/error.html",
                {
                    "site_name": site_name,
                    "message": "Please select at least one brand or category.",
                },
            )

        # Use select_related to fetch related data in a single query
        activeListings = Motorcycle.objects.filter(isActive=True).select_related(
            "category",
            "brand",
        )

        # Optionally filter by brands
        if brands:
            brands = Brand.objects.filter(brand_name__in=brands)
            activeListings = activeListings.filter(brand__in=brands)

        # Optionally filter by categories
        if categories:
            categories = Category.objects.filter(category_name__in=categories)
            activeListings = activeListings.filter(category__in=categories)

        # Optionally filter by search query if not empty
        if search_query:
            activeListings = activeListings.filter(name__icontains=search_query)

        # Optionally pass the selected brands and categories to the template
        selectedBrands = brands if brands else None
        selectedCategories = categories if categories else None

        print(f"Active Listings Count: {activeListings.count()}")

        if not activeListings.exists():
            print("No listings found matching the criteria.")
            return render(
                request,
                "auction/error.html",
                {"site_name": site_name, "message": "No match found."},
            )
        else:
            allBrands = Brand.objects.all()
            allCategories = Category.objects.all()
            return render(
                request,
                "auction/active_listing.html",
                {
                    "site_name": site_name,
                    "motorcycles": activeListings,
                    "brands": allBrands,
                    "categories": allCategories,
                    "selectedBrands": selectedBrands,
                    "selectedCategories": selectedCategories,
                },
            )
    else:
        return render(request, "auction/error.html", {"message": "Invalid request"})


@login_required
def create_listing(request):
    site_name = "Motorcycles Auction Club"

    if request.method == "GET":
        form = CreateListingForm()
        return render(
            request, "auction/create.html", {"form": form, "site_name": site_name}
        )

    form = CreateListingForm(request.POST)
    if form.is_valid():
        with transaction.atomic():
            name = form.cleaned_data["name"]
            start_price = form.cleaned_data["start_price"]
            brand = form.cleaned_data["brand"]
            category = form.cleaned_data["category"]
            engine_capacity = form.cleaned_data["engine_capacity"]
            cylinders = form.cleaned_data["cylinders"]
            power = form.cleaned_data["power"]
            torque = form.cleaned_data["torque"]
            mileage = form.cleaned_data["mileage"]
            top_speed = form.cleaned_data["top_speed"]
            fuel_capacity = form.cleaned_data["fuel_capacity"]
            color = form.cleaned_data["color"]
            condition = form.cleaned_data["condition"]
            image_url = form.cleaned_data["image_url"]
            summary = form.cleaned_data["summary"]

            current_user = request.user
            brandData = get_object_or_404(Brand, brand_name=brand)
            categoryData = get_object_or_404(Category, category_name=category)

            # bid = Bid(bid=bid_price, user=current_user)
            # bid.save()

            newListing = Motorcycle(
                name=name,
                start_price=start_price,
                brand=brandData,
                category=categoryData,
                engine_capacity=engine_capacity,
                cylinders=cylinders,
                power=power,
                torque=torque,
                mileage=mileage,
                top_speed=top_speed,
                fuel_capacity=fuel_capacity,
                color=color,
                condition=condition,
                image_url=image_url,
                summary=summary,
                owner=current_user,
            )

            newListing.save()

            return HttpResponseRedirect(reverse("index"))

    return render(
        request, "auction/create.html", {"form": form, "site_name": site_name}
    )

@login_required(login_url="/accounts/login/")
def motorcycle(request, name):
    site_name = "Motorcycles Auction Club"
    # motorcycle_id = request.GET.get('id')
    # motorcycle = get_object_or_404(Motorcycle, name=name, id=motorcycle_id)
    motorcycle = get_object_or_404(Motorcycle, name=name)
    isMotorcycleInWatchlist = request.user in motorcycle.watchlist.all()
    isOwner = request.user.username == motorcycle.owner.username
    allBids = Bid.objects.filter(motorcycle=motorcycle).order_by("-bid_amount")
    allComments = Comment.objects.filter(motorcycle=motorcycle, parent=None).order_by(
        "-created_at"
    )
    comments_with_replies = [
        (comment, comment.get_all_replies()) for comment in allComments
    ]
    current_time = timezone.now()
    time_remaining = motorcycle.end_time - current_time
    message = ""
    update = False

    # Get the highest bid and the user who placed it
    highest_bid = Bid.objects.filter(motorcycle=motorcycle).aggregate(
        Max("bid_amount")
    )["bid_amount__max"]
    highest_bid_instance = None
    highest_bidder = None
    if highest_bid:
        highest_bid_instance = Bid.objects.filter(
            motorcycle=motorcycle, bid_amount=highest_bid
        ).first()
        highest_bidder = (
            Bid.objects.filter(motorcycle=motorcycle, bid_amount=highest_bid)
            .first()
            .bidder
        )

    # Handle adding a new bid
    if request.method == "POST":
        try:
            newBid = int(request.POST["newBid"])
        except (KeyError, ValueError):
            message = "Invalid bid value"
            newBid = None

        if newBid is not None:
            highest_bid_instance = Bid.objects.filter(
                motorcycle=motorcycle, bid_amount=highest_bid
            ).first()
            currentBid = (
                highest_bid_instance.bid_amount
                if highest_bid_instance
                else motorcycle.start_price
            )

            if current_time >= motorcycle.end_time:
                message = "Auction has already ended."
            elif isOwner:
                message = "Owner cannot place bids on their own listings."
            elif newBid <= currentBid:
                message = "Enter higher bid."
            else:
                # Create a new bid object
                new_bid_instance = Bid.objects.create(
                    bidder=request.user, bid_amount=newBid, motorcycle=motorcycle
                )
                new_bid_instance.save()
                motorcycle.current_bid = new_bid_instance
                print(motorcycle.current_bid)
                motorcycle.save()
                message = f"Bid updated successfully. New Bid { motorcycle.current_bid.bid_amount } by { motorcycle.current_bid.bidder.username }."
                update = True
        else:
            if highest_bid:
                message = f"Highest Bid: Rs. {highest_bid}"
            else:
                message = "No bids have been placed yet."

    # Check if listing is expired
    if current_time >= motorcycle.end_time:
        if not motorcycle.isExpired:
            motorcycle.isExpired = True
            if highest_bidder and highest_bidder != motorcycle.owner:
                motorcycle.collection.add(highest_bidder)
                motorcycle.sold = True
                message = f"Winner is {highest_bidder}"
            elif highest_bidder and highest_bidder == motorcycle.owner:
                message = "No bids were placed."
            else:
                message = "No bids have been placed yett."
            motorcycle.save()

        time_remaining = timedelta(0)

        # Set a flag to indicate auction closed
        auction_closed = True

    else:
        auction_closed = False

    # List all bids
    # Determine the starting price set by the owner
    starting_price = motorcycle.start_price
    print(f"Starting Price: {starting_price}")

    # Fetch all bids for the motorcycle, ordered by bid time descending
    allPlacedBids = Bid.objects.filter(motorcycle=motorcycle).order_by('-bid_time')

    # Exclude the starting bid if it exists
    valid_bids = [bid for bid in allPlacedBids if bid.bid_amount != starting_price]
    print(f"Valid Bids (excluding starting price): {valid_bids}")

    return render(
        request,
        "auction/motorcycle.html",
        {
            "motorcycle": motorcycle,
            "isMotorcycleInWatchlist": isMotorcycleInWatchlist,
            "allComments": allComments,
            "isOwner": isOwner,
            "site_name": site_name,
            "comments_with_replies": comments_with_replies,
            "time_remaining": time_remaining,
            "message": message,
            "update": update,
            "sold": motorcycle.sold,
            "winner": highest_bidder,
            "highest_bid": highest_bid,
            "allBids": allBids,
            "auction_closed": auction_closed,
            "valid_bids": valid_bids,
            'range_200': range(200),
        },
    )


def close_auction(request, name):
    motorcycle_id = request.GET.get("id")
    site_name = "Motorcycles Auction Club"
    motorcycle = Motorcycle.objects.get(name=name, id=motorcycle_id)
    # motorcycle.isActive = False
    # motorcycle.isExpired = True
    # motorcycle.save()
    if request.user == motorcycle.owner:
        motorcycle.isActive = False
        motorcycle.save()
    isMotorcycleInWatchlist = request.user in motorcycle.watchlist.all()
    allComments = Comment.objects.filter(motorcycle=motorcycle)
    isOwner = request.user.username == motorcycle.owner.username
    # return redirect('listing', name=name)
    # return redirect("index")
    return render(
        request,
        "auction/motorcycle.html",
        {
            "site_name": site_name,
            "motorcycle": motorcycle,
            "isMotorcycleInWatchlist": isMotorcycleInWatchlist,
            "allComments": allComments,
            "isOwner": isOwner,
            "update": True,
            "message": "Motorcycle is No more Available For Auction.",
        },
    )


@login_required
@csrf_protect
def add_comment(request, name):
    motorcycle_id = request.GET.get("id")
    print(f"Received name: {name}, motorcycle_id: {motorcycle_id}")  # Debug log

    if request.method == "POST":
        current_user = request.user
        motorcycle = get_object_or_404(Motorcycle, name=name)
        print(f"Retrieved motorcycle: {motorcycle}")  # Debug log
        message = request.POST.get("newComment")
        parent_id = request.POST.get("parent_id")

        print(f"Received message: {message}, parent_id: {parent_id}")  # Debug log

        if message:
            # Retrieve the parent comment if parent_id is provided
            parent_comment = None
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(pk=parent_id)
                except Comment.DoesNotExist:
                    return JsonResponse(
                        {"success": False, "error": "Parent comment does not exist."}
                    )

            newComment = Comment(
                author=current_user,
                motorcycle=motorcycle,
                message=message,
                parent=parent_comment,
            )
            newComment.save()

            print("Comment saved successfully.")  # Debug log

            # Redirect to the same listing page after adding comment
            return redirect("motorcycle", name=name)
        else:
            return JsonResponse(
                {"success": False, "error": "Comment message cannot be empty."}
            )
    else:
        return HttpResponseBadRequest("Invalid request method.")


@login_required
@csrf_protect
def delete_comment(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=comment_id)
        motorcycle = comment.motorcycle
        current_user = request.user

        if (
            current_user == comment.author
            or current_user == motorcycle.owner
            or current_user.is_superuser
        ):
            comment.delete()
            messages.success(request, "Comment deleted successfully.")
            return redirect("motorcycle", name=motorcycle.name)
        else:
            messages.error(request, "You are not authorized to delete this comment.")
            return redirect("motorcycle", name=motorcycle.name)
            # return HttpResponseForbidden(
            #     "You are not authorized to delete this comment."
            # )
    else:
        return HttpResponseBadRequest("Invalid request method.")


# @login_required
# @csrf_protect
# def delete_comment(request, comment_id):
#     if request.method == "DELETE":
#         comment = get_object_or_404(Comment, pk=comment_id)
#         motorcycle = comment.motorcycle
#         current_user = request.user

#         if current_user == comment.author or current_user == motorcycle.owner or current_user.is_superuser:
#             comment.delete()
#             return JsonResponse({"success": True, "message": "Comment deleted successfully."})
#         else:
#             return HttpResponseForbidden("You are not authorized to delete this comment.")
#     else:
#         return HttpResponseBadRequest("Invalid request method.")


def login_view(request):
    site_name = "Motorcycles Auction Club"
    if request.method == "POST":

        # Bind the form with the POST data
        form = LoginForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, attempt to sign the user in
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                form.add_error(None, "Invalid username and/or password.")

    else:
        # If the request method is not POST, create an instance of the form
        form = LoginForm()

    # Render the login page with the form
    return render(request, "auction/login.html", {"form": form, "site_name": site_name})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    site_name = "Motorcycles Auction Club"

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))
    else:
        form = RegistrationForm()

    return render(
        request, "auction/register.html", {"form": form, "site_name": site_name}
    )


@login_required
def user_profile(request, username):
    if username:
        print(f"Querying for username: {username}")  # Debug statement
        profile_user = get_object_or_404(User, username=username)
    else:
        profile_user = request.user

    site_name = "Motorcycles Auction Club"
    all_users = User.objects.all()
    collection_count = profile_user.collection.all().count()
    user_listings_count = Motorcycle.objects.filter(owner=profile_user).count()

    if request.method == "POST" and profile_user == request.user:
        form = UserProfileForm(request.POST, request.FILES, instance=profile_user)
        if form.is_valid():
            form.save()
            return redirect("user_profile", username=profile_user.username)
    else:
        form = UserProfileForm(instance=profile_user)

    return render(
        request,
        "auction/user_profile.html",
        {
            "form": form,
            "site_name": site_name,
            "profile_user": profile_user,
            "current_user": request.user,
            "all_users": all_users,
            "collection_count": collection_count,
            "user_listings_count": user_listings_count,
        },
    )


@login_required
def edit_profile(request, username):
    current_user = request.user
    site_name = "Motorcycles Auction Club"
    user_instance = get_object_or_404(User, username=username)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            form.save()
            return redirect(
                "user_profile", username=username
            )  # Redirect to the user profile page
    else:
        form = UserProfileForm(instance=user_instance)

    return render(request, "auction/edit.html", {"form": form, "site_name": site_name})


@login_required
def users(request):
    all_users = User.objects.all()
    site_name = "Motorcycles Auction Club"
    paginator = Paginator(all_users, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, "auction/users.html", {"all_users": page_obj, "site_name": site_name}
    )


@login_required
def user_listings(request, username):
    site_name = "Motorcycles Auction Club"
    profile_user = get_object_or_404(User, username=username)
    user_listings = Motorcycle.objects.filter(owner=profile_user)

    return render(
        request,
        "auction/user_listings.html",
        {
            "site_name": site_name,
            "current_user": request.user,
            "profile_user": profile_user,
            "user_listings": user_listings,
        },
    )


# @login_required
# def all_bids(request):
#     bids = Bid.objects.all().select_related('motorcycle', 'bidder')  # Assuming Bid model has ForeignKeys to Motorcycle and User models
#     return render(request, 'auction/all_bids.html', {'bids': bids})

@login_required
def all_bids(request):
    site_name = "Motorcycles Auction Club"
    bids_list = Bid.objects.all().select_related('motorcycle', 'bidder')
    paginator = Paginator(bids_list, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'auction/all_bids.html', {'page_obj': page_obj,  "site_name": site_name,})

@login_required
def listing_bids(request, name):
    print("View function called")
    motorcycle_id = request.GET.get("id")
    print(f"Motorcycle ID from GET parameter: {motorcycle_id}")

    site_name = "Motorcycles Auction Club"
    motorcycle = get_object_or_404(Motorcycle, name=name, id=motorcycle_id)

    print("Motorcycle found")
    print(f"Motorcycle Name: {motorcycle.name}")

    # Determine the starting price set by the owner
    starting_price = motorcycle.start_price
    print(f"Starting Price: {starting_price}")

    # Fetch all bids for the motorcycle, ordered by bid time descending
    allBids = Bid.objects.filter(motorcycle=motorcycle).order_by('-bid_time')

    # Exclude the starting bid if it exists
    valid_bids = [bid for bid in allBids if bid.bid_amount != starting_price]
    print(f"Valid Bids (excluding starting price): {valid_bids}")

    paginator = Paginator(valid_bids, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "auction/listing_bids.html",
        {
            "motorcycle": motorcycle,
            "page_obj": page_obj,
            "site_name": site_name,
        },
    )


@login_required
def watchlist(request, username):
    site_name = "Motorcycles Auction Club"
    current_user = request.user

    user = User.objects.get(username=username)
    motorcycles = user.motorcycleWatchList.all()
    return render(
        request,
        "auction/watchlist.html",
        {"site_name": site_name, "motorcycles": motorcycles, "user": current_user},
    )


def removeWatchList(request, name):
    motorcycle_id = request.GET.get("id")
    print(f"Listing ID: {id}, Listing Name: {name}")
    motorcycle = Motorcycle.objects.get(name=name, id=motorcycle_id)

    # motorcycle.watchlist.remove(request.user)
    if request.user in motorcycle.watchlist.all():
        motorcycle.watchlist.remove(request.user)

    return redirect("motorcycle", name=name)


def addWatchList(request, name):
    motorcycle_id = request.GET.get("id")
    print(f"Listing ID: {id}, Listing Name: {name}")
    motorcycle = Motorcycle.objects.get(name=name, id=motorcycle_id)

    # motorcycle.watchlist.add(request.user)
    if request.user not in motorcycle.watchlist.all():
        motorcycle.watchlist.add(request.user)

    return redirect("motorcycle", name=name)


@login_required
def collection(request, username):
    site_name = "Motorcycles Auction Club"
    # Get the User object based on the username provided
    profile_user = get_object_or_404(User, username=username)

    # Get listings related to the profile_user
    collection_motorcycles = profile_user.collection.all()
    collection_count = collection_motorcycles.count()
    print(f"Collection Count: {collection_motorcycles.count()}")
    print(f"Collection Count: {collection_count}")

    return render(
        request,
        "auction/collection.html",
        {
            "site_name": site_name,
            "current_user": request.user,
            "profile_user": profile_user,
            "collection_motorcycles": collection_motorcycles,
            "collection_count": collection_count,
        },
    )
