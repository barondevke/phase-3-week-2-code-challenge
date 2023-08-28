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


# Define a class to represent customers
class Customer:
    customer_instances = []  # Store all customer instances here

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.customer_instances.append(self)
        self.reviews = []  # Store reviews written by this customer
        self.restaurantsVisited = []  # Store restaurants visited by this customer
        
    # Method to get the customer's first name
    def given_name(self):
        return self.first_name
    
    # Method to get the customer's last name
    def family_name(self):
        return self.last_name
    
    # Method to get the customer's full name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Method to create a review for a restaurant
    def create_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.addReview(review)
    
    # Method to get a list of restaurant names where the customer has written reviews
    def restaurants(self):
        return [x.restaurant_object.restaurant_name for x in self.reviews]
    
    # Method to get the number of reviews written by the customer
    def num_reviews(self):
        return len(self.reviews)
    
    # Method to record a visited restaurant
    def restaurantVisiting(self, restaurant):
        self.restaurantsVisited.append(restaurant)
    
    # Class method to find a customer's full name based on given first name
    @classmethod
    def find_by_given_name(instances, fullName):
        for customer in instances.customer_instances:
            if customer.given_name() == fullName:
                return customer.full_name()
            else:
                return None

    # Class method to find all customer full names based on given first name
    @classmethod
    def find_all_by_given_name(instances, fullName):
        customerList = []
        for customer in instances.customer_instances:
            if customer.given_name() == fullName:
                customerList.append(customer.full_name())
        return customerList

    # Class method to retrieve all customer full names
    @classmethod
    def all(instances):
        return [x.full_name() for x in instances.customer_instances]


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
