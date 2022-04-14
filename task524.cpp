//
//  main.cpp
//  task524
//
//  Created by 李戊辰 on 2021/8/5.
//  Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.


#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <unordered_map>
#include <numeric>
using namespace std;

class Solution {
public:
    // dst can be derived by str
    bool isSubString(string str, string dst)
    {
        int p1 = 0, p2 = 0;
        for(;p1<str.size()&&p2<str.size();p1++)
        {
            if (str[p1]==dst[p2])
            {
                p2++;
            }
        }
        // if dst is derived, pointer will exceed
        return p2==dst.size();
    }
    string findLongestWord(string s, vector<string>& dictionary)
    {
        string tmp = ""; // initialize result
        for (string dst:dictionary)
        {
            if (isSubString(s, dst))
            {
                tmp = dst.size()>tmp.size()?dst:tmp;
                // handle special cases
                if(tmp.size() == dst.size())
                {
                    tmp = dst<tmp?dst:tmp; // compare two string directly by ascii codes
                }
            }
        }
        return tmp;
    }
};
int main()
{
    string a = "121lst";
    string b = "aasttt";
    
    return 0;
}
