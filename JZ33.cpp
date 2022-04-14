class Solution {
public:
    int GetUglyNumber_Solution(int index) {
        // 前6个正好是是1-6
        if(index<=6)    return index;
        // 我们没有必要维护三个队列，只需要记录三个指针显示到达哪一步
        int p2=0, p3=0, p5=0, ret=0;
        vector<int> v;
        v.push_back(1);
        while(v.size()<index)
        {
            ret = min(v[p2]*2, min(v[p3]*3, v[p5]*5));
            if(v[p2]*2==ret)    p2++;
            if(v[p3]*3==ret)    p3++;
            if(v[p5]*5==ret)    p5++;
            v.push_back(ret);
        }
        return ret;
    }
};