import hashlib
class Codec:
    dict_url = {}
    def encode(self, longUrl):
        if not longUrl:
            return None
        shortUrl = "http://tinyurl.com/" + hashlib.sha224(longUrl).hexdigest()[-6:]
        if shortUrl not in self.dict_url:
            self.dict_url[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        if shortUrl in self.dict_url:
            return self.dict_url[shortUrl]
        return None