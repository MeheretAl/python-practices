class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.mapping1 = dict()
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenId = tokenId
        self.currentTime = currentTime
        self.mapping1[tokenId] = currentTime+self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for key in self.mapping1:
            if self.mapping1[key] > currentTime:
                count += 1
        
        return count

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.mapping1:
            if self.mapping1[tokenId] > currentTime:
                self.mapping1[tokenId] =  self.timeToLive + currentTime
