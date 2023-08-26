class Review:
    reviews = []

    def __init__(self, customer,restaurant,rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)


    @classmethod
    def all(instances):
        return instances.reviews     