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
    
    





    