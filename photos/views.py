from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, ImageCategory, ImageLocation
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    images = Image.objects.all()
    categories = ImageCategory.objects.all()
    locations = ImageLocation.objects.all()
    return render(request, 'index.html', {"images": images, "categories": categories, "locations": locations})


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        print(search_term)
        try:
            categories = ImageCategory.objects.get(name=search_term)
            searched_images = Image.search_image(categories)
            print(searched_images)

            return render(request, 'search.html', {'images': searched_images})

        except ObjectDoesNotExist:
            message = "No images found"
            categories = ImageCategory.objects.all()
            return render(request, "search.html", {"message": message, "categories": categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})


def view_image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        return render(request, 'image.html', {'image': image})

    except ObjectDoesNotExist:
        message = 'Sorry, we could not find what you are looking for'
        return render(request, 'image.html', {'message': message})


def get_category(request, category_id):
    category = ImageCategory.objects.get(id=category_id)
    image = Image.search_image(category)

    return render(request, 'search.html', {'images': image})


def get_location(request,location_id):
    location = ImageLocation.objects.get(id=location_id)
    image = Image.search_by_location(location)

    return render(request, 'search.html', {'images': image})

