from blog.models import Category
from django import template


register = template.Library()


@register.inclusion_tag('blog/menu.html')
def show_menu():
    categories = Category.objects.all()
    return {'categories': categories,}