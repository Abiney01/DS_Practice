class Hashmap:
    def __init__(self):
        self.hashmap = {}

    def put(self,key,value):
        self.hashmap[key] = value

    def get(self,key):
        if key in self.hashmap:
            return self.hashmap[key]
        return - 1
    
    def remove(self,key):
        try:
            if key in self.hashmap:
                del self.hashmap[key]
        except:
            raise KeyError("Key doesn't exists")
hashmap_obj = Hashmap()
print(hashmap_obj.put(1,1))
print(hashmap_obj.put(2,2))
print(hashmap_obj.get(1))
print(hashmap_obj.get(3))
print(hashmap_obj.put(2,1))
print(hashmap_obj.get(2))
print(hashmap_obj.remove(2))
print(hashmap_obj.get(2))