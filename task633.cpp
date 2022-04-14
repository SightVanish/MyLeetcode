// Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <numeric>
using namespace std;


class Solution {
public:
    bool judgeSquareSum(int c) {
        long maxNumber = long(sqrt(c)+1); // note: here must be long, in case the number could be too big
        long p1=0, p2=maxNumber;
        while(p1<=p2){ // note: here should consider p1=p2
            if (p1*p1+p2*p2<c){
                p1++;
            }
            else if (p1*p1+p2*p2>c){
                p2--;
            }
            else{
                return true;
            }
        }
        return false;
        
    }
};
// 解释
// 看了官方题解的双指针算法，不免产生一个疑问，假设初始化时，左指针low = 0，右指针high = sqrt(c)。
// 为什么 low^2+high^2<clow要让low++而不是high++呢？
// 或者说为什么让low++可以保证不错过正确答案呢？
// 同理，为什么low^2+high^2>clow时，要让high--而不是low--呢？
// 或者说为什么让high--可以保证不错过正确答案呢？
// 其实我们可以把双指针的过程看成在一个矩阵中搜寻的过程。举个例子，c = 18，初始化low = 0，high = 4，那么看如下矩阵：
//   0 1 2 3 4
// 0 x x x x 16
// 1 x x x x x
// 2 x x x x x
// 3 x x x x x
// 4 x x x x 32
// 初始化时起点必定在矩阵的右上角。
// 每次比较 low^2+high^2和c可以排除矩阵的一行或一列。
// 推广
// 我们可以看到，二维矩阵实际上是枚举了所有可能的组合。本题中 c=a^2+b^2c=a 可以简单推广到 c=f(a,b)c=f(a,b)，
// 只要 f(a,b)f(a,b) 满足随 a, b递增，且要搜索的是一个有序序列，就可以使用这种双指针法，只要把二维矩阵中的元素换成 f(a,b)f(a,b) 就可以了
