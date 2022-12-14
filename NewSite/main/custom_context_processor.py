from .models import Profile, Category, BlogPost, Post_Category, Tag, Settings, User
from django.contrib.auth.decorators import user_passes_test

def user_info(request):
   current_user = User.objects.get(is_superuser=True)
   return {'user': current_user }

def post_info(request):
  popular_posts = BlogPost.objects.filter(status='published').order_by('-created')[0:3]
  return {'popular_posts': popular_posts}

def category_info(request):
  categories = Post_Category.objects.all()[0:2]
  return {'categories': categories}


def tags_info(request):
  tags = Tag.objects.all()
  footer_tags = Tag.objects.all()[:4]
  return {'tags': tags, 'footer_tags': footer_tags}

def general_settings(request):
  settings = Settings.objects.all()
  return {'settings': settings}


