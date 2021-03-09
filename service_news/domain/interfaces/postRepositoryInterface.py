class PostServiceInterfaces:
    def getListPost(self) -> list:
        pass
    def getPostById(self, id: str) -> dict:
        pass
    def deletePostById(self, id: str) -> dict:
        pass