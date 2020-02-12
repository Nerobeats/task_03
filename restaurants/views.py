from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list" :[{
    "restaurant_name":"Smokey"
    , "food_type": "Burger",
    "restaurant_name": "Mosilli"
    , "food_type": "Shawerma",
    "restaurant_name":"Olivia"
    , "food_type": "Italian"}]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object" :{
    "Brisket": "Burger"
    }

    }
    return render(request, 'detail.html', context)
