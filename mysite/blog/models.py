from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust


'''
Category
-title - c 255
-slug - s 255
-

Tag
-title - c 50
-slug - s 50
-

Post
-title - c 255
-slug  -s 255
-content - text
-created_at -d
-photo
-category - fk category
'''


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_by_category', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.SlugField(max_length=50, verbose_name="Url", unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_with_tags', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Фото")
    medium_image = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFill(300, 188)], source='photo',
            format='JPEG', options={'quality': 70})
    small_image = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFill(100, 62)], source='photo',
            format='JPEG', options={'quality': 60})
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Публикации'


class ViewsCount(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    count = models.SmallIntegerField(verbose_name="Количество просмотров")

class Comment(models.Model):
    pass