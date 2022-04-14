#include<iostream>
#include<vector>
#include<typeinfo>
#include <algorithm>
using namespace std;

// 对字符串进行全排序
// void Permutation(string s, vector<string>& ans, int low) // s is the string we are tring to sort, ans is the return answer, low is the index we have already sorted
// {
//     if (low == s.size()-1)
//     {
//         ans.push_back(s);
//     }
//     else
//     {
//         for (int i=low; i<s.size(); i++)
//         {
//             swap(s[i], s[low]); // swap to continue
//             Permutation(s, ans, low+1);
//             swap(s[i], s[low]); // recover from swapping
//         }
//     }
// }

// vector<string> Permutation(string s)
// {
//     vector<string> ans;
//     sort(s.begin(), s.end());
//     do
//     {
//         ans.push_back(s);
//     } while (next_permutation(s.begin(), s.end())); // note: this function will reduce duplicated anwers
//     return ans;
// }


// int main()
// {
//     string s = "abc";
//     vector<string> ans;
//     ans = Permutation(s);
//     for (auto i:ans)
//     {
//         cout<<i<<endl;
//     }
//     return 0;
// }



// JZ27 ans
class Solution {
public:
    vector<string> Permutation(string str) {
        vector<string> ans;
        do
        {
            ans.push_back(str);
        }while(next_permutation(str.begin(), str.end()));
        sort(ans.begin(), ans.end());
        return ans;
    }
};