/*
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
*/
#include<iostream>
#include<vector>
#include<climits>
using namespace std;
//we are supposed to use binary search here
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
        //for simplication, we make nusm1 the shorter one
        if (m > n)  return findMedianSortedArrays(nums2, nums1);
        //since we do not know whether m+n is even or odd
        if((m + n) % 2 == 0)
        {    
            (find_Kth_element(nums1, 0, nums2, 0, (m + n)/2));
            int j = (find_Kth_element(nums1, 0, nums2, 0, (m + n)/2 + 1));
            return (find_Kth_element(nums1, 0, nums2, 0, (m + n)/2) + find_Kth_element(nums1, 0, nums2, 0, (m + n)/2 + 1))/2.0;
        }
        else    return find_Kth_element(nums1, 0, nums2, 0, (m + n + 1)/2);
    }
    //use divide conquer to solve this problem--to find the Kth element in two sorted vectors
    int find_Kth_element(vector<int>& nums1, int begin1, vector<int>& nums2, int begin2, int K){
        //first we set cases to end this recursive
        int m = nums1.size();
        int n = nums2.size();
        // cout << "K = " << K <<endl;
        // cout << "nums1 = " << endl;
        // for(int i = begin1; i < m; i++){
        //     cout << nums1[i] << ' ';
        // }
        // cout << endl << "nums2 = " << endl;
        // for(int i = begin2; i < n; i++){
        //     cout << nums2[i] << ' ';
        // }
        // cout << endl;

        //we need to ensure m < n
        if(begin1 >= m && K > 0)  return nums2[begin2 + K - 1];//all elements in nums1 is thrown
        else if(begin2 >= n && K >0) return nums1[begin1 + K - 1];//all elements in nums2 is thrown
        else if(K == 1) return min(nums1[begin1],nums2[begin2]);//just for a little faster
        else{
            //we need to thrown out half of K each recusive, so we try to throw K/2(may be smaller than that for border cases) elements from nums1 or nums2
            int half = K/2;
            // cout << "half = " << half <<endl;
            int first_value1 = 0, first_value2 = 0;
            //first we need to check whether there are K-1 elements in each vector
            if(m - begin1 < half)  first_value1 = INT_MAX;
            else    first_value1 = nums1[half - 1 + begin1];
            first_value2 = nums2[half - 1 + begin2];
            // cout << "first_value1 = " << first_value1 << " first_value2 = " << first_value2 << endl;
            //we can throw half of nums1
            if(first_value1 < first_value2){
                //we throw half of nums1
                return find_Kth_element(nums1, half + begin1, nums2, begin2, K - half);
            }
            //we throw half of nums2
            else{
                if(m - begin1 < n - begin2 - half){
                    //we need to keep length of nums1 < nums2
                    return find_Kth_element(nums1, begin1, nums2, begin2 + half, K - half);
                }
                else{
                    return find_Kth_element(nums2, begin2 + half, nums1, begin1, K - half);
                }
            }
        }
    }
};

//solution reference--more precious
/*
class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int left = (m + n + 1) / 2;
        int right = (m + n + 2) / 2;
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right)) / 2.0;
    }
    //i: nums1的起始位置 j: nums2的起始位置
    public int findKth(int[] nums1, int i, int[] nums2, int j, int k){
        if( i >= nums1.length) return nums2[j + k - 1];//nums1为空数组
        if( j >= nums2.length) return nums1[i + k - 1];//nums2为空数组
        if(k == 1){
            return Math.min(nums1[i], nums2[j]);
        }
        int midVal1 = (i + k / 2 - 1 < nums1.length) ? nums1[i + k / 2 - 1] : Integer.MAX_VALUE;
        int midVal2 = (j + k / 2 - 1 < nums2.length) ? nums2[j + k / 2 - 1] : Integer.MAX_VALUE;
        if(midVal1 < midVal2){
            return findKth(nums1, i + k / 2, nums2, j , k - k / 2);
        }else{
            return findKth(nums1, i, nums2, j + k / 2 , k - k / 2);
        }        
    }
}
*/

class Solution1 {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int n = nums1.size();
		int m = nums2.size();
        //保证数组1一定最短
		if (n > m)  return findMedianSortedArrays(nums2, nums1);

		// Ci 为第i个数组的割,比如C1为2时表示第1个数组只有2个元素。LMaxi为第i个数组割后的左元素。RMini为第i个数组割后的右元素。
		int LMax1, LMax2, RMin1, RMin2, c1, c2, lo = 0, hi = 2 * n;  //我们目前是虚拟加了'#'所以数组1是2*n长度

		while (lo <= hi)   //二分
		{
			c1 = (lo + hi) / 2;  //c1是二分的结果
			c2 = m + n - c1;

			LMax1 = (c1 == 0) ? INT_MIN : nums1[(c1 - 1) / 2];
			RMin1 = (c1 == 2 * n) ? INT_MAX : nums1[c1 / 2];
			LMax2 = (c2 == 0) ? INT_MIN : nums2[(c2 - 1) / 2];
			RMin2 = (c2 == 2 * m) ? INT_MAX : nums2[c2 / 2];

			if (LMax1 > RMin2)
				hi = c1 - 1;
			else if (LMax2 > RMin1)
				lo = c1 + 1;
			else
				break;
		}
		return (max(LMax1, LMax2) + min(RMin1, RMin2)) / 2.0;
	}
};


int main(){
    vector<int> a {2};
    vector<int> b {1,3,4};
    Solution s;
    Solution1 s1;
    double answer;
    double answer1;
    answer = s.findMedianSortedArrays(a,b);
    answer1 = s1.findMedianSortedArrays(a,b);
    cout << "my median = " << answer << endl;
    cout << "real answer = " << answer1 << endl;
    return 0;
}
