from django.shortcuts import render

# Create your views here.
def search(request):
    #method がgetであればこのsearch()メソッドを実行させる
    if request.method == 'GET':
        form = forms.SearchForm(request.GET)
        # Formがvalidかどうか確認する
        if form.is_valid():
        # keyword, categoryにユーザーが入力した値を代入する
            keyword = request.GET.get('keyword')
            category = request.GET.get('category')