from django.shortcuts import render

def post_list(request):
    return render(request, 'conecta/post_list.html', {})
