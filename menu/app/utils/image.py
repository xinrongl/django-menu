from django.http import HttpResponse

def upload_image(request):
    if request.method == 'POST':
        file = request.FILES.get('upload_image', None)
        
    return HttpResponse(status=403)