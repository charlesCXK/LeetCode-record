class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        int deltax1 = points[1][0] - points[0][0];
        int deltax2 = points[2][0] - points[1][0];
        int deltay1 = points[1][1] - points[0][1];
        int deltay2 = points[2][1] - points[1][1];
        
        if(deltax1==0 && deltax2==0 && deltay1==0 && deltay2==0)
            return false;
        if(deltax1*deltay2 == deltax2*deltay1)
            return false;
        return true;
        
    }
};