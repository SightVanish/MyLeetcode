// There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

// You are giving candies to these children subjected to the following requirements:

// Each child must have at least one candy.
// Children with a higher rating get more candies than their neighbors.
// Return the minimum number of candies you need to have to distribute the candies to the children.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <unordered_map>
#include <numeric>
using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> result(ratings.size(),1);
        for (int i=0; i<ratings.size()-1; i++)
        {
            if (ratings[i+1]>ratings[i]){
                result[i+1]=result[i]+1;
            }
        }
        for (int i=ratings.size()-1; i>0; i--)
        {
            if (ratings[i-1]>ratings[i]){
                result[i-1]=max(result[i]+1, result[i-1]); // note: here must be max!!!
            }
        }
        
        return accumulate(result.begin(), result.end(), 0);
    }
};
