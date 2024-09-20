from django.http import HttpResponse, JsonResponse


def homepage(request):
    if request.method == 'POST':  # If the request method is POST
        return JsonResponse({"message": "This is a POST request"})
    else:  # Default to GET if no other method is specified
        return HttpResponse("This is a GET request")