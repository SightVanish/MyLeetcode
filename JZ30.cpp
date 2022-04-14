class Solution {
public:
    int FindGreatestSumOfSubArray(vector<int> array) {
        int ret = array[0];
        // 最大的子数组=自己+之前最大连续
        for(int i=1; i<array.size();i++)
        {
            array[i]+=array[i-1]>0?array[i-1]:0; // array[i]存储的即是到此为止的最大连续子数组
            ret = max(ret, array[i]);
        }
        return ret;
    }
};