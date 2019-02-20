/*
Runtime: 1444 ms, faster than 36.59% of C++ online submissions 
*/

class Solution {
public:
    bool flag;
    
    // calculate the sum of the vector
    int computeSum(vector<int> v) {
        int ret = 0, length = v.size();
        for(int i=0;i<length;i++) {
            ret += v[i];
        }
        return ret;
    }
    
    void dfs(vector<int> sbsum, int width, vector<int> lst, int index) {
        if(index == lst.size()) {
            flag = true;
            return;
        }
        if(flag)
            return;
        
        for(int i=0;i<4;i++) {
            if(sbsum[i]+lst[index] <= width) {
                sbsum[i] += lst[index];
                dfs(sbsum, width, lst, index+1);
                sbsum[i] -= lst[index];
            }
        }
    }
    
    bool makesquare(vector<int>& nums) {
        flag = false;
        int length = nums.size();
        int totsum = computeSum(nums);
        
        if(totsum<=0 || totsum%4!=0)
            return false;
        int width = totsum / 4;
        vector<int> sbsum = {0, 0, 0, 0};
        // sort the list. 
        // rbegin(): the first element from the end.
        sort(nums.rbegin(), nums.rend());
        dfs(sbsum, width, nums, 0);
        return flag;
    }
};