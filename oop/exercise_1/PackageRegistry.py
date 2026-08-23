from collections import defaultdict


class PackageRegistry:
    def __init__(self):
        self.packages = []

    def add(self, package):
        if package not in self.packages:
            self.packages.append(package)

    def __len__(self):
        return int(len(self.packages))

    def __contains__(self, package):
        return package in self.packages

    def __iter__(self):
        self.index=0
        return self

    def __next__(self):
        if self.index>=len(self.packages):
            raise StopIteration
        package = self.packages[self.index]
        self.index+=1
        return package

    def names(self):
        return sorted({p.name for p in self.packages})

    def versions_by_name(self):
        versions = defaultdict(list)
        for p in self.packages:
            versions[p.name].append(p.version)
        return {name: sorted(v) for name, v in versions.items()}