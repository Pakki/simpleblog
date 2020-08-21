from blog.models import Tag, ViewsCount
from django import template

register = template.Library()

@register.inclusion_tag('blog/popular_posts.html')
def get_popular_posts(cnt):
    return {'posts':[record.post for record in ViewsCount.objects.order_by('-count')[:cnt]]}

@register.inclusion_tag('blog/tags_cloud.html')
def get_tags_cloud():
    return {'tags': Tag.objects.all()}