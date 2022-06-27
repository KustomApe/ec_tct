from django.shortcuts import render

# Create your views here.
def search(request):
    #method がgetであればこのsearch()メソッドを実行させる
    if request.method == 'GET':
        