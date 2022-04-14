/*
 * @Description: hard
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-05 19:32:53
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-05 20:02:15
 * @FilePath: /Leetcode/task726.cpp
 */

// Given a chemical formula (given as a string), return the count of each atom.

// The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

// One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

// Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

// A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

// Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <stack>
#include <numeric>
using namespace std;


class Solution {
public:
    string countOfAtoms(string formula) {
        int i = 0, n = formula.length();
        
        // 读取atom名字
        auto parseAtom = [&]() -> string {
            string atom;
            atom += formula[i++]; // 扫描首字母，然后i+=1
            // isalpha判断是否为字母，islower判断是否为小写-isupper
            while (i < n && islower(formula[i])) {
                atom += formula[i++]; // 扫描首字母后的小写字母
            }
            return atom; // 返回值为完整的atom名
        };

        // 读取数字大小
        auto parseNum = [&]() -> int {
            // 处理最后一个字符
            if (i == n || !isdigit(formula[i])) {
                return 1; // 不是数字，视作 1
            }
            int num = 0;
            // 此处要考虑多个字符的进位问题
            while (i < n && isdigit(formula[i])) {
                num = num * 10 + int(formula[i++] - '0'); // 扫描数字
            }
            return num;
        };


        stack<unordered_map<string, int>> stk;
        stk.push({}); // push empty map

        while (i < n) {
            char ch = formula[i];
            // 遇到 () 就push map to stack--计算括号内部
            if (ch == '(') {
                i++;
                stk.push({}); // 将一个空的哈希表压入栈中，准备统计括号内的原子数量
            } else if (ch == ')') {
                // () 结束，计算个数
                i++;
                int num = parseNum(); // 括号右侧数字
                auto atomNum = stk.top(); // top为最后push的
                stk.pop(); // 弹出括号内的原子数量
                for (auto &[atom, v] : atomNum) {
                    stk.top()[atom] += v * num; // 将括号内的原子数量乘上 num，加到上一层的原子数量中
                } // 加入上一层中计数，最后总共加入总的最外层
            } else {
                // 无 () 就正常考虑atom
                string atom = parseAtom();
                int num = parseNum();
                stk.top()[atom] += num; // 统计原子数量
            }
        }

        auto &atomNum = stk.top(); // 此处top即为最外层
        vector<pair<string, int>> pairs;
        for (auto &[atom, v] : atomNum) {
            pairs.emplace_back(atom, v); // emplace_back 相当于 push_back，但是更高效
        }
        sort(pairs.begin(), pairs.end()); // 按照atom进行排序

        string ans;
        for (auto &p : pairs) {
            ans += p.first;
            if (p.second > 1) {
                ans += to_string(p.second);
            }
        }
        return ans;
    }
};


int main()
{
    string formula = "K4(ON(SO3)2)2";
    Solution s;
    cout<<s.countOfAtoms(formula);

    return 0;
}