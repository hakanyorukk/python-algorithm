class Package:

    def __init__(self,name,version):
        self.name = name
        self.version = version

    @classmethod
    def from_string(cls,text):
        if not "==" in text:
            raise ValueError("Doesn't contain ==")
        try:
            name,version = text.split("==")
        except (ValueError, AttributeError):
            raise ValueError("Invalid")
        return cls(name, version)

    @property
    def major(self):
        nums = self.version.split(".")
        return int(nums[0])

    def __str__(self):
        return f"{self.name}=={self.version}"

    def __repr__(self):
        return f"Package('{self.name}', '{self.version}')"

    def __eq__(self, other):
        if isinstance(other, Package):
            if self.name == other.name and self.version == other.version:
                return True
        return False

    def __hash__(self):
        return hash((self.name, self.version))


