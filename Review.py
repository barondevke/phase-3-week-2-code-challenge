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
        self.reviews = []
        self.restaurantsVisited = []

    def given_name(self):
        return self.first_name
    
    def family_name(self):
        return self.last_name


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def create_review(self,restaurant,rating):
        review = Review(self.full_name(),restaurant,rating)
        self.reviews.append(review)
        restaurant.addReview(review)

    def restaurants(self):
        return[x.restaurant_name for x in self.reviews]
    
    def num_reviews(self):
        return len(self.reviews)
    
    
    @classmethod
    def find_by_given_name(instances,fullName):
         for customer in instances.customer_instances:
            if customer.full_name() == fullName:
                return customer
            else:
                return None  

      
    @classmethod
    def find_all_by_given_name(instances,fullName):
         customerList = []
         for customer in instances.customer_instances:
            if customer.full_name() == fullName:
                customerList.append(customer)


    
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

    def addReview(self,review):
        self.reviewsList.append(review)

    def customers(self):
        return [x.customer_object for x in self.reviewsList]


    def average_star_rating(self):
        if self.reviewsList == 0:
            return 0
        else:
            total = 0
            for x in self.reviewsList:
                total+=x
            return total/len(self.reviewsList)    


        
