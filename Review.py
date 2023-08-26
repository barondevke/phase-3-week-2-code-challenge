class Review:
    reviews = []

    def __init__(self, customer_object,restaurant_object,rating):
        self.customer_object = customer_object
        self.restaurant_object = restaurant_object
        self.rating = rating
        Review.reviews.append(self)

    def customer(self):
        return self.customer_object
    
    def restaurant(self):
        return self.restaurant_object


    @classmethod
    def all(instances):
        return instances.reviews     


class Customer:
    customer_instances = []

    def __init__(self,first_name,last_name ):
        self.first_name = first_name
        self.last_name = last_name
        Customer.customer_instances.append(self)

    def given_name(self):
        return self.first_name
    
    def family_name(self):
        return self.last_name


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def all(instances):
        return instances.customer_instances
    
    

class Restaurant:

    def __init__(self,restaurant_name):
        self.restaurant_name = restaurant_name
        self.reviewsList = []


    def name(self):
        return self.restaurant_name   
    
    def reviews(self):
        return self.reviewsList
