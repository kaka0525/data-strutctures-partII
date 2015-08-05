from __future__ import unicode_literals


class HashTable:
    def __init__(self, bucket_num):
        self.buckets = [{}] * bucket_num
        self.bucket_num = bucket_num

    def _hash_alg(self, key):
        key_ord = 0
        for l in key:
            key_ord += ord(l)
        return key_ord % self.bucket_num

    def set(self, key, val):
        if not isinstance(key, basestring):
            raise TypeError
        bucket = self._hash_alg(key)
        self.buckets[bucket][key] = val

    def get(self, key):
        bucket = self._hash_alg(key)
        return self.buckets[bucket][key]

    def hash(self, key):
        self.set(key, None)
