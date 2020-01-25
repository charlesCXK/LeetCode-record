class Solution {
public:
    int maximum69Number (int num) {
        int n;
        bool first = false;
        vector<int> v;
        vector<int>::iterator it;
        
        while(num > 0)
        {
            n = num%10;
            num /= 10;
            v.push_back(n);
        }
        
        int len_num = v.size();
        int res = 0;
        for(int it=len_num-1;it>=0;it--)
        {
            if(v[it]==6 && first==false)
            {
                first = true;
                res += 9*pow(10, it);
            }
            else
                res += v[it]*pow(10, it);
        }
        
        return res;
    }
};