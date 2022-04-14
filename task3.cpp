/*Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
*/
#include<iostream>
#include<string>
#include<time.h>
#include<cstdlib>
#include<unordered_map>
using namespace std;

//my solution with hash map
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int result = 0;//the result we will return
        int begin = 0;//indicate where our string starts
        int i = 0;
        unordered_map<char,int> hash;//use hash table to decide whether we have repitition
        for(i = 0; i < s.length(); i++){
           unordered_map<char,int>::const_iterator iter = hash.find(s[i]);//first: find whether we have repeated entry
            if(iter != hash.end() && iter->second >= begin){//if the element is not found in current array(not include before the array we are testing)
                result = max(result,i - begin);//since i is the index now (s[i] has already repeated)
                begin = iter->second + 1;//let begin = the head of testing array
            }
            hash[s[i]] = i;//we hash this entry to hash table
        }
    return max(result,i - begin);
    }
};
//my solution has already been really fast--so the key point is Sliding Window (set an argument begin so that each time we only check part of out long long hash table)
//apparently, with unordered_map, it will be faster.
//if you want to save memory, you can use unordered_map.erase() to erase the entries before begin


int main(){
    srand(time(0));
    int length = 20;
    string s;
    for(int i = 0; i < length; i++){
        s = s + (char)('A'+rand()%5);
    }
    cout << "string is: " << endl;
    for(int i = 0; i < s.length(); i++){
        cout << s[i] << ' ';
    }
    cout << endl;
    Solution result;
    cout << result.lengthOfLongestSubstring(s);
    return 0;
}