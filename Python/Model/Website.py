class Website:
    def __init__(self,
    name:str,
    domain:str,
    product_type:str,
    tracking_support:bool,
    brute_force_support:bool):

        self.name = name
        self.domain = domain
        self.product_type = product_type
        self.tracking_support = tracking_support
        self.brute_force_support = brute_force_support


    def get_name(self):
        return self.name
    def get_domain(self):
        return self.domain
    def get_product_type(self):
        return self.product_type
    def get_tracking_support(self):
        return self.tracking_support
    def get_brute_force_support(self):
        return self.brute_force_support

    def set_name(self,name):
        self.name = name
    def set_domain(self,domain):
        self.domain = domain
    def set_product_type(self,product_type):
        self.product_type = product_type
    def set_tracking_support(self,tracking_support):
        self.tracking_support = tracking_support
    def set_brute_force_support(self,brute_force_support):
        self.brute_force_support = brute_force_support
    

    def __str__(self):
            return f"Website(name={self.name},domain={self.domain},url={self.url},product_type={self.product_type},tracking_support={self.tracking_support},brute_force_support={self.brute_force_support})"
