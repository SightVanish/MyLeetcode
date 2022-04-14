//
//  main.cpp
//  task680
//
//  Created by 李戊辰 on 2021/8/5.
//
//Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <numeric>
using namespace std;

class Solution {
public:
    bool isValid(string s, int p1, int p2)
    {
        while(p1 < p2)
        {
            if (s[p1] != s[p2])   return false;
            p1++; p2--;
        }
        return true;
    };
    bool validPalindrome(string s) {
        int p1 = 0;
        int p2 = s.size()-1;
        
        while(p1 < p2)
        {
            if (s[p1] != s[p2])
            {
                return (isValid(s, p1+1, p2) || isValid(s, p1, p2-1)); // note: we can only delete one char
            }
            p1++; p2--;
        }
        return true;
    }
};

int main()
{
    auto a = "abc";
    Solution s;
    cout<<s.validPalindrome(a)<<endl;
    return 0;
}
