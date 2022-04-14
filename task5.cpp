/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
*/
#include<iostream>
#include<time.h>
#include<cstdlib>
#include<string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.size();
        string result;
        int result1 = 0, result2 = 0;//used for caluting the final result
        int iter1 = 0, iter2 = 0;
        int iter = 0;//the core of palindromic substrin we are testing
        for(iter = 0; iter < length; iter++){
            iter1 = iter; iter2 = iter;//set our two index iterators
            //we need test wheter the core is one or two element: 'bacab' or 'baccab' ('bacccab')
            //so we just check twice and get the longer one
            //first we check 'bacab' & 'bacccab'
            while(iter1 > 0 && iter2 < length-1 && s[iter1-1] == s[iter2+1] ){
                iter1--; iter2++;
            }
            if(iter2 - iter1 > result2 - result1){
                result1 = iter1;
                result2 = iter2;
            }
            iter1 = iter; iter2 = iter;
            //if it is 'baccab' it does nothing above, so we will check it
            if(s[iter] == s[iter+1]){
                iter2 = iter + 1;
            }
            //next we let iter1 goes left and iter2 goes right;
            while(iter1 > 0 && iter2 < length-1 && s[iter1-1] == s[iter2+1] ){
                iter1--; iter2++;
            }
            //next we update result iters;
            if(iter2 - iter1 > result2 - result1){
                result1 = iter1;
                result2 = iter2;
            }
        }
        //finally we need to return a string instead of two iters;
        for(int i = result1; i <= result2; i++){
            result.push_back(s[i]);
        }
        return result;
    }
};

int main(){
    srand(time(0));
    int length = 20;
    string s = "aaaaa";
    // for(int i = 0; i < length; i++){
    //     s = s + (char)('A'+rand()%6);
    // }
    cout << "string is: " << endl;
    for(int i = 0; i < s.length(); i++){
        cout << s[i] << ' ';
    }
    cout << endl;
    Solution result;
    cout << result.longestPalindrome(s);
    return 0;
}