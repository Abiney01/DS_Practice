import heapq
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
    def postTweet(self,userId,tweetId):
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1
    
    def getNewsFeed(self,userId):
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count,tweetId,followeeId,index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count,tweetId,followeeId,index-1])
        return res

    def follow(self,followerId,followedId):
        self.followMap[followerId].add(followedId)
    
    def unfolllow(self,followerId,followedId):
        if followedId in self.followMap[followerId]:
            self.followMap[followerId].remove(followedId)
       

twitter_obj = Twitter()
twitter_obj.postTweet(1,10)
twitter_obj.postTweet(2,20)
print(twitter_obj.getNewsFeed(1))
print(twitter_obj.getNewsFeed(2))
twitter_obj.follow(1,2)
print(twitter_obj.getNewsFeed(1))
print(twitter_obj.getNewsFeed(2))
twitter_obj.unfolllow(1,2)
twitter_obj.getNewsFeed(1)