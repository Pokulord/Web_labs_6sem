from django.db import models
from datetime import date
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Category", max_length=150)
    descr = models.TextField("Description")
    urls = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Actor(models.Model):
    name = models.CharField("Actor_name", max_length=100)
    age = models.PositiveSmallIntegerField("Actor_age", default=0)
    descr = models.TextField("Description")
    image = models.ImageField("Image", upload_to="actors/")


    def __str__(self):
        return self.name
    
    def absolute_url(self):
        return reverse('actor_detail', kwargs={'slug' : self.name})
    
    class Meta:
        verbose_name = "Actors and directors"
        verbose_name_plural = "Actors and directors"



class Genre(models.Model):
    name = models.CharField("name", max_length=100)
    descr = models.CharField("Description" , max_length=3000)
    url = models.SlugField(max_length=160, unique=True)


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    title = models.CharField("Title", max_length=100)
    tagline = models.CharField("Tag", max_length=100 , default='')
    descr = models.TextField("Description")
    poster = models.ImageField("Image", upload_to="movies_posters/")
    year = models.PositiveSmallIntegerField("Year of publish", default= 2019)
    country = models.CharField("Country", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Actor", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    world_premiere = models.DateField("Year of the World premire" , default=date.today)
    budget = models.PositiveIntegerField("Budget" , default=0 , help_text= "Enter the sum in $")
    fees_in_usa = models.PositiveIntegerField("Fees in USA" , default=0 , help_text= "Enter the sum in $")
    fees_in_world = models.PositiveIntegerField("Fees in the World", default= 0 , help_text="Enter the sum in $")
    category = models.ForeignKey(Category, verbose_name= "Category", on_delete=models.SET_NULL , null = True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("IsDraft", default= False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={'slug' : self.url})
    
    def get_review(self):
        return self.reviews_set_filter(parent__isnull = True)
    

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"





class MovieShots(models.Model):
    title = models.CharField("Title" , max_length=100)
    descr = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Movie Shot"
        verbose_name_plural = "Movie shots"



class RatingStar(models.Model):
    value = models.SmallIntegerField("Value", default=0)

    def __str__(self):
        return f"{self.value}"
    
    class Meta:
        verbose_name = "Rating star"
        verbose_name_plural = "Rating stars"
        ordering = ["-value"]



class Rating(models.Model):
    ip = models.CharField("IP address" , max_length= 15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name= "Star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"
    


    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey(
        "self", verbose_name="Parent" , on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} - {self.movie}"
    

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
    
