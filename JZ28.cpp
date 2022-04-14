#include<iostream>
#include<vector>
#include<typeinfo>
#include<algorithm>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {
        unordered_map<int, float> map;
        for (auto i:numbers)
        {
            map[i]++;
        }
        float count=numbers.size()/2;
        for(auto i=map.begin(); i!=map.end(); i++)
        {
            if(i->second>count)
            {
                return i->first;
                break;
            }
        }
        return numbers[0];
    }
};

int main()
{
    // cout<<map[0]<<endl;
    return 0;
}