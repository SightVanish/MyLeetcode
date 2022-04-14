/*给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。*/
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;//we need return a vector
        unordered_map<int,int> hash;//use hash map to speed up--find a element in hash O(1)
        /*
        hash table looks like
        {
            {A,1} {B,2} {C,3}...
        }
        */
        result.push_back(0); result.push_back(0);//init result
        int N = nums.size();
        unordered_map<int,int>::const_iterator got;//use iterator to find whether what we want is in hash
        for(int i = 0; i < N; i++){
            // whatever you need to go over the vector for at least once (worst case)
            int rest = target - nums[i];
            got = hash.find(rest);
            if(got != hash.end()){
            //if we find the target-nums[i] \
            (if unordered_map find fails, it returns hash.end();return type of find is iterator)
            result[0] = got->second;//second is the order of this element
            result[1] = i;
            cout << got->second << '\t' << i << endl;
            return result;
            }
            //if we do not find rest in hash, we put nums[i] into hash so that we only need to go through nums once
            hash[nums[i]] = i;//we map rest to i in hash table
        }
        
        return result;
    }
};

int main(){
    srand((unsigned)time(NULL)); 
    vector<int> nums;
    nums.push_back(2);nums.push_back(7);nums.push_back(14);nums.push_back(15);
    cout << endl; 
    int target = 9;
    Solution s;
    s.twoSum(nums,target);

}