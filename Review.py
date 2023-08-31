# Define a class to manage customer reviews
class Review:
    reviews = []  # Store all reviews in this list

    def __init__(self, customer_object, restaurant_object, rating):
        self.customer_object = customer_object
        self.restaurant_object = restaurant_object
        self.customerRating = rating
        
        # Add review details to the reviews list
        Review.reviews.append({
            "customerName": self.customer_object.full_name(),
            "restaurantName": self.restaurant_object.restaurant_name,
            "rating": self.customerRating
        })

    # Method to get the customer's full name
    def customer(self):
        return self.customer_object.full_name()
    
    # Method to get the restaurant's name
    def restaurant(self):
        return self.restaurant_object.restaurant_name
    
    # Method to get the customer's rating
    def rating(self):
        return self.customerRating
    
    # Class method to retrieve all reviews
    @classmethod
    def all(instances):
        return instances.reviews


