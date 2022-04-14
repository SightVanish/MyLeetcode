class Solution {
public:
    int FirstNotRepeatingChar(string str) {
        if (str.empty())    return -1;
        unordered_map<char, int> charMap;
        for(int i=0; i<str.size(); i++)
        {
            charMap[str[i]] ++;
        }
        for(int i=0; i<str.size(); i++)
        {
            if (charMap[str[i]]==1)
            {
                return i;
            }
        }
        return -1;
    }
};