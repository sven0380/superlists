from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


def home_page(request):
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST.get('item_text', ''))
    #     return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})
    # list_ = List.objects.get(id=list_id)
    # items = Item.objects.filter(list=list_)
    # return render(request, 'list.html', {'items': items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text', ''), list=list_)
    return redirect('/lists/%d/' % (list_.id))


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))