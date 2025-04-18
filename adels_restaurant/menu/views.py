from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Category

def menu_list(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    menu_items = MenuItem.objects.filter(category=category, is_available=True)
    return render(request, 'menu/category_detail.html', {
        'category': category,
        'menu_items': menu_items
    })

def menu_item_detail(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id, is_available=True)
    return render(request, 'menu/menu_item_detail.html', {'menu_item': menu_item})

