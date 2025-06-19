from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    menu_type = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)

    def average_rating(self):
        ratings = [c.rating for c in self.comments.all()]
        return round(sum(ratings) / len(ratings), 1) if ratings else 0.0
    
    def rating_stars(self):
        avg = self.average_rating()
        full = int(avg)
        half = 1 if avg - full >= 0.5 else 0
        empty = 5 - full - half
        return "★" * full + "⯨" * half + "☆" * empty
    @property
    def city(self):
        # Przykład: jeśli adres jest "ul. X 10, Warszawa"
        # to wyciągamy część po przecinku
        if ',' in self.address:
            return self.address.split(',')[-1].strip()
    def __str__(self):
        return self.name


class Comment(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(blank=True)
    rating = models.PositiveIntegerField()  # 1–5

    def __str__(self):
        return f"{self.restaurant.name} - Ocena: {self.rating}"
