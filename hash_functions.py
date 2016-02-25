from binary_search import COUNTRIES


def HASH_FUNCTION(s):
    """Simple but not ideal hash function."""
    return sum(ord(c) for c in s)

def create_empty_array(length):
    return [None] * length

class HashTable:

    def __init__(self, bucket_count, hash_function):
        self.bucket_count = bucket_count
        self.hash_function = hash_function
        self.buckets = create_empty_array(bucket_count)
        self.element_count = 0

    def load_factor(self):
        return float(self.element_count) / self.bucket_count

    # key is a string
    def add(self, key, value):
        bucket_index = self.hash_function(key) % self.bucket_count
        bucket = self.buckets[bucket_index]
        if bucket is None:
            self.buckets[bucket_index] = bucket = []

        for k, v in bucket:
            if key == k:
                raise ValueError(key + " already exists")

        bucket.append((key, value,))
        self.element_count += 1

        if self.load_factor() > 5:
            print "Load factor is ", self.load_factor(), "at", self.element_count,"elements -- resizing to", 2 * self.bucket_count, "buckets"
            temp = HashTable(2 * self.bucket_count, self.hash_function)
            for bucket in self.buckets:
                if bucket is not None:
                    for k, v in bucket:
                        temp.add(k, v)

            self.buckets = temp.buckets
            self.bucket_count = temp.bucket_count



    # if there is no element with the given key, this
    # raises a KeyError
    def get(self, key):
        bucket_index = self.hash_function(key) % self.bucket_count
        bucket = self.buckets[bucket_index]

        if bucket is None:
            raise KeyError(key)

        for k, v in bucket:
            if key == k:
                return v

        raise KeyError(key)


t = HashTable(16, HASH_FUNCTION)


for country, population in COUNTRIES:
    t.add(country, population)

for i, bucket in enumerate(t.buckets):
    print "Bucket", i, ": ", (0 if bucket is None else len(bucket)), "Elements"


print "Population of Brazil: ", t.get("Brazil")
print "Load factor:", t.load_factor()
