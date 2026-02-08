class Hashset:
    def __init__(self):
        self.hashset = {}

    def add(self,key):
        try:
            if key not in self.hashset:
                self.hashset[key] = key
        except:
            raise KeyError("Key alreaady exist")
    
    def remove(self,key):
        try:
            if key in self.hashset:
                del self.hashset[key]
        except:
            raise KeyError("Key doesn't exists")
        
    def contains(self,key):
        return key in self.hashset
    
hash_obj = Hashset()
print(hash_obj.add(3))
print(hash_obj.add(3))
# hash_obj.remove(2)
# print(hash_obj.contains(2))