import os
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from App1.Functions.read import get_texts
from App1.Functions.extraction_data import extract_id_info
from App1.Functions.collect import save_id_data
from App1.models import IdentityInfo


def home(request):
    return HttpResponse("Hello, Django!")



def index(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        id_type = request.POST.get('idType')

        # print(id_type,uploaded_file)

        # Define the save path
        app_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(app_dir, 'downloads', uploaded_file.name)

        # Save the file manually
        with open(save_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        txt=get_texts(save_path)
        print(txt)

        # print(txt)
        info1 = extract_id_info(txt)
        # print(info1)
        save_id_data(info1)




        return render(request, 'App1/index.html', {
            'message': f"File '{uploaded_file.name}' uploaded successfully "
        })

    return render(request, 'App1/index.html')


def identity_table_view(request):
    identities = IdentityInfo.objects.all()  # Replace with your model
    return render(request, 'App1/display.html', {'identities': identities})
