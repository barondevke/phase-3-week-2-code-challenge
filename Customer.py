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


