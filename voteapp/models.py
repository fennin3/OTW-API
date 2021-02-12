from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="categories/images/")

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name




class WeeklyPost(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="weekly_posts")
    image = models.ImageField(upload_to='weekly_post/images/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} post - {self.date_posted}"
    
    @staticmethod
    def avg_rating(id):
        ratings = Rating.objects.filter(post_id=id)
        total_num = len(ratings)
        avg_rating_ = 0
        for i in ratings:
            avg_rating_ += i.stars
        
        val = avg_rating_/total_num
        return round(val,2)


class Rating(models.Model):
    post = models.ForeignKey(WeeklyPost, on_delete=models.CASCADE, related_name='ratings')
    rater = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])

    def __str__(self):
        return str(self.product)+"---"+str(self.rater)


class WeeklyWinner(models.Model):
    post = models.ForeignKey(WeeklyPost, on_delete=models.CASCADE, related_name='winners')
    week_no = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(5.0)], null=True, blank=True)


    def save(self, *args, **kwargs):
        self.rating = self.post.avg_rating(self.post.id)
        super(WeeklyWinner, self).save(*args, **kwargs)

    def __str__(self):
        return f"Winner of {self.post.category.name} -- week {self.week_no}"