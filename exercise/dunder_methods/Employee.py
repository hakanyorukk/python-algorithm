class Employee:
    # company = "DXC" # class variable shared by all - static
    #
    # def __init__(self,name):
    #     self.name = name   # instance variable - unique per object
    #
    #

    count = 0

    def __init__(self,name):
        self.name = name
        Employee.count += 1

    @staticmethod
    def is_valid_name(name):
        return len(name) > 0  # doesn't need self or the class

    @classmethod
    def from_dict(cls,d):  # receives the class not an instance
        return cls(d["name"])

    @property
    def display_name(self):
        return self.name.upper()






