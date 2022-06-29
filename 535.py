class Codec:
    def __init__(self):
        self.database = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        self.id += 1
        self.database[self.id] = longUrl
        return "http://tinyurl.com/" + str(self.id)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind('/')
        id = int(shortUrl[i + 1:])
        return self.database[id]
