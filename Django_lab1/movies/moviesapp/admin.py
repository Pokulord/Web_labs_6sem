from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots , Actor , Rating , RatingStar , Reviews



list_to_reg= [Category, Genre, Movie, MovieShots, Actor, Rating , RatingStar, Reviews]

for elem in list_to_reg: admin.site.register(elem)

# Register your models here.
