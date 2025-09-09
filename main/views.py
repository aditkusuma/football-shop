from django.shortcuts import render

def show_main(request):
    context = {
        "app_name": "Football Store",
        "name": "Raditya Ikhlas Kusuma",  
        "class": "KKI",  
    }
    return render(request, "main.html", context)
