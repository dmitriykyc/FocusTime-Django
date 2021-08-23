from django.shortcuts import render

# Create your views here.

def main(request):
    content = {'page_title': 'Hello'}
    return render(request, 'mainapp/index.html', context=content)


