from django.shortcuts import render
from .models import Restaurant
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

def restaurant_list(request):
    name_filter = request.GET.get("name", "")
    city_filter = request.GET.get("city", "")
    menu_filter = request.GET.get("menu", "")
    sort_by = request.GET.get("sort", "name")  # domyślne sortowanie po nazwie

    restaurants = Restaurant.objects.all()

    if name_filter:
        restaurants = restaurants.filter(name__icontains=name_filter)

    if city_filter:
        restaurants = restaurants.filter(address__icontains=city_filter)

    if menu_filter:
        restaurants = restaurants.filter(menu_type__icontains=menu_filter)

    if sort_by in ["name", "-name"]:
        restaurants = restaurants.order_by(sort_by)

    return render(request, "portal/restaurant_list.html", {"restaurants": restaurants})




def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    comments = restaurant.comments.all()
    avg_rating = restaurant.average_rating()

    return render(request, "portal/restaurant_detail.html", {
        "restaurant": restaurant,
        "comments": comments,
        "avg_rating": avg_rating,
    })
