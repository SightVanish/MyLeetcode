/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
*/
#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
    string convert(string s, int numRows) {
        // dealing with boundary
        if(s == "") return s;
        if(numRows == 1) return s;
        int chunck = 2*numRows-2;
        string result[chunck];
        for(int i = 0; i < s.length(); i++){
            int k = i%chunck;
            if(k < numRows)
                result[k].push_back(s[i]);
            else
                result[chunck-k].push_back(s[i]);
        }
        string out;
        for(int i = 0; i < 2*numRows-2; i++){
            out += result[i];
        }
        return out;
    }
};

int main(){
    // int length;
    // cin >> length;
    string s = "A";
    // for(int i = 0; i < length; i++){
    //     s = s + (char)('A'+rand()%26);
    // }
    int numRows;
    cin >> numRows;
    Solution result;
    string p = result.convert(s, numRows);
    cout << p << endl;



    return 0;
}