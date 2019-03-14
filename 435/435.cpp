/*
Greedy, whose end value is smaller comes first.
 */

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    static bool mycmp(Interval a, Interval b) {
        return a.end < b.end;
    }
    
    int eraseOverlapIntervals(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), mycmp);
        vector<Interval>::iterator it = intervals.begin();
        
        int nowRight = -999999, deleteCount = 0;
        while(it != intervals.end())
        {
            if((*it).start < nowRight)
                deleteCount++;
            else
                nowRight = (*it).end;
            it++;
        }
        return deleteCount;
    }
};