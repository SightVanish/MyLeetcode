// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
// eg.
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]

#include <iostream>
#include <vector>
#include <unordered_map>
#include <stdlib.h>
using namespace std;
class Solution {
public:
    vector< vector<int> > threeSum(vector<int>& nums) // the output is like [[-1,-1,2],[-1,0,1]]
    {
        int size = nums.size();
        if (size < 3)   return {};          // there must be no solution
        vector< vector<int> >res;            // 保存结果（所有不重复的三元组）
        sort(nums.begin(), nums.end()); // sort vector, increasing
        for (int i = 0; i < size; i++)      // 固定第一个数，转化为求两数之和
        {
            if (nums[i] > 0)    return res; // 第一个数大于 0，后面都是递增正数，不可能相加为零了
            // 去重：如果此数已经选取过，跳过
            if (i > 0 && nums[i] == nums[i-1])  continue;
            // 双指针在nums[i]后面的区间中寻找和为0-nums[i]的另外两个数
            int left = i + 1;
            int right = size - 1;
            while (left < right)
            {
                if (nums[left] + nums[right] > -nums[i])
                    right--;    // 两数之和太大，右指针左移
                else if (nums[left] + nums[right] < -nums[i])
                    left++;     // 两数之和太小，左指针右移
                else
                {
                    // 找到一个和为零的三元组，添加到结果中，左右指针内缩，继续寻找
                    vector<int> tmp = {nums[i], nums[left], nums[right]};
                    res.push_back(tmp);
                    left++;
                    right--;
                    // 去重：第二个数和第三个数也不重复选取
                    // 例如：[-4,1,1,1,2,3,3,3], i=0, left=1, right=5
                    while (left < right && nums[left] == nums[left-1])  left++;
                    while (left < right && nums[right] == nums[right+1])    right--;
                }
            }
        }
        return res;
    }
};
int main(){




    return 0;
}