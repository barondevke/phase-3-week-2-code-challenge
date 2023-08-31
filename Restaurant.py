# Define a class to represent restaurants
class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.reviewsList = []  # Store reviews for this restaurant
        
    # Method to get the restaurant's name
    def name(self):
        return self.restaurant_name
    
    # Method to add a review to the restaurant
    def addReview(self, review):
        self.reviewsList.append(review)
    
    # Method to get a list of ratings given by customers for the restaurant
    def reviews(self):
        return [x.customerRating for x in self.reviewsList]
    
    # Method to get a list of customer objects who reviewed the restaurant
    def customers(self):
        return [x.customer_object for x in self.reviewsList]
    
    # Method to calculate the average star rating for the restaurant
    def average_star_rating(self):
        if self.reviewsList == 0:
            return 0
        else:
            total = 0
            for x in self.reviewsList:
                total += x.customerRating
            return total / len(self.reviewsList)
