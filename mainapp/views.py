from django.shortcuts import render

# Create your views here

def main(request):
    user = request.user
    content = {'page_title': 'Главная', 'user': user}
    return render(request, 'mainapp/index.html', context=content)


