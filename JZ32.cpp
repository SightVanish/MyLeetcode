class Solution {
public:
    string PrintMinNumber(vector<int> numbers) {
        sort(numbers.begin(),numbers.end(), cmp);
        string ret="";
        for(auto i:numbers)
        {
            ret+=to_string(i);
        }
        return ret;
    }
    static bool cmp(int a, int b)
    {
        string A="";
        string B="";
        // A=a+b
        A+=to_string(a);
        A+=to_string(b);
        //B=b+a
        B+=to_string(b);
        B+=to_string(a);
        return A<B;
    }
};