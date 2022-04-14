/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/
#include <iostream>
#include <ctime>
#include <random>
#include <math.h>
using namespace std;
class Solution {
public:
    int reverse(int x) {
        // deal with boundary
        if(x == 0) return 0;
        // 2^31-1 = 2,147,483,647
        // - 2^31 = -2,147,483,648
        // boundary = 2,147,447,412
        // first we need to check whether x is positive or negative
        int p = x > 0 ? 1:-1;
        int result = 0;
        int k = abs(x);
        while(k > 0){
            int i = k%10;
            if(long test = (long)result * 10 > 2147483647) return 0;
            result = result*10 + i;
            k = k/10;
        }
        return p*result;
    }
};

int main(){
    // srand((unsigned)time(0));
    // int i = rand()%1000 - 500;
    int i = 1534236469;
    // 1,534,236,469 -> 
    Solution s;
    int result = s.reverse(i);
    cout << "Original input = " << i << "; Reversal = " << result << endl;
    return 0;
}