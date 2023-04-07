#include <iostream>
#include <string>
using namespace std;
/*
Given an integer n, return a binary string representing its representation in base -2.
Note that the returned string should not have leading zeros unless the string is "0".
Example 1:

Input: n = 2
Output: "110"
Explantion: (-2)2 + (-2)1 = 2
Example 2:

Input: n = 3
Output: "111"
Explantion: (-2)2 + (-2)1 + (-2)0 = 3
Example 3:

Input: n = 4
Output: "100"
Explantion: (-2)2 = 4
*/
class Solution {
public:
    string baseNeg2(int n) {
        string res = "";
        while (n) {
            res = to_string(n & 1)  + res; // n & 1 is a way to extract remainder
            n = - (n >> 1); // n >> 1 is different from n / 2 if n is a negative numbers
        }
        return res == "" ? "0" : res;
    }
};



int main(){
    int n = 2;
    Solution S;
    // cout << S.baseNeg2(n) << endl;
    
    for(int i=1; i<=10; i++)
        cout << (-i >> 1) << " " << (i >> 1) << endl;
    return 0;
}

