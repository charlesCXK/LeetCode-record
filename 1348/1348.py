class TweetCounts:

    def __init__(self):
        self.tweetDict = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweetDict:
            self.tweetDict[tweetName].append(time)
        else:
            self.tweetDict[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 3600
        else:
            delta = 86400
        
        startIdxs = range(startTime, endTime+1, delta)
        ret = [0 for i in range(len(startIdxs))]
        timeList = self.tweetDict[tweetName]
        
        for thisTime in timeList:
            if thisTime<startTime or thisTime>endTime:
                continue
            idx = (thisTime-startTime) // delta
            if idx < len(ret):
                ret[idx] += 1
        return ret


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)