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
            # categoryは文字型->数値型に変更が必要(右辺にint()で変換してあげる)
            category = int(request.GET.get('category'))
            if category == 0:
                items = models.Item.objects.filter(name__contains=keyword)
            else:
                items = models.Item.objects.filter(category_id=category, name__contains=keyword)
            context = {
                'items': items,
            }
            return render(request, 'shopping/searchResult.html', context)