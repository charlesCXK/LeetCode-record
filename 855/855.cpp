/*
Runtime: 56 ms, faster than 32.14% of C++ online submissions 

Use a set to sovle the question.
Traverse this set, calculate the distance from the midpoint of the two adjacent elements in the set
to its both sides, and record the maximum distance.
Also, the begin and the end of the seats should be considered.
*/

class ExamRoom {
public:
    int n;
    set<int> s;
    
    ExamRoom(int N) {
        n = N;
    }
    
    int seat() {
        // first action
        if(s.size() == 0)
        {
            s.insert(0);
            return 0;
        }
        
        int max_distance = -999999, target = -1;
        set<int>::iterator it = s.begin();
        int prev = *it;
        it++;
        
        // if person sitting on seat 0 has left.
        // small index should come first !
        if(*(s.begin())-0 > max_distance)
        {
            max_distance = *(s.begin());
            target = 0;
        }
        
        while(it != s.end())
        {
            int index = (prev+*it)/2;
            // 'min': distance to each side should be considered
            if(min(*it-index, index-prev) > max_distance)
            {
                max_distance = min(*it-index, index-prev);
                target = index;
            }
            prev = *it;
            it++;
        }
        
        // To see if he can sit on the last seat.
        if(n-1-prev > max_distance)
        {
            max_distance = n-1-prev;
            target = n-1;
        }

        
        s.insert(target);       // sit down
        return target;
    }
    
    void leave(int p) {
        s.erase(p);
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */