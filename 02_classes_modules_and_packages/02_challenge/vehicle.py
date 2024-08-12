class Vehicle:
    discount_rule_lambda = None
    discount_rule_value = None

    def __init__(self):
        self.model = None
        self.make = None
        self.year = None
        self.price = None
        self._discount = None
        return
    
    def set(self, model, make, year, price, discount = 0):
        self.model = model
        self.make = make
        self.year = year
        self.price = price
        self._discount = discount

    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year
    
    def get_price(self):
        return self.price
    
    def get_discount(self):
        return self._discount
    
    def display(self):
        print(f"Model:{self.model}, Make:{self.make}, Year:{self.year}, Price:{self.price}, Discount:{self._discount}")
    
    @classmethod
    def overwrite_discount_rule(cls, rule_lambda, discount):
        cls.discount_rule_lambda = rule_lambda
        cls.discount_rule_value = discount
        return
    
    def apply_discount(self):
        aaa = self.discount_rule_lambda(self)
        if self.discount_rule_lambda(self):
            self._discount = self.discount_rule_value
        return
    
    
    def apply_discount_2(self, rule_lambda, discount):
        aaa = rule_lambda(self)
        if aaa:
            return discount