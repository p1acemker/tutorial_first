from .models import Category
def menu_links(request):
    links=Category.objects.all()
    # print("menu_links"+str(type(links)))
    # print(dict(links=links))
    # 第一个links是字典的key名，后面的links是为key匹配的value
    return dict(links=links)