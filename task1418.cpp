/*
 * @Description: medium
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-06 21:35:04
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-06 21:46:50
 * @FilePath: /Leetcode/task1418.cpp
 */

// Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

// Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <numeric>
using namespace std;

class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>> &orders) {
        // 从订单中获取餐品名称和桌号，统计每桌点餐数量
        unordered_set<string> nameSet;
        unordered_map<int, unordered_map<string, int>> foodsCnt; // 两层map
        for (auto &order : orders) {
            nameSet.insert(order[2]);
            // table id
            int id = stoi(order[1]); // stoi--turn char to int
            ++foodsCnt[id][order[2]]; // the order of table id
        }

        // 提取餐品名称，并按字母顺序排列
        int n = nameSet.size();
        vector<string> names;
        for (auto &name : nameSet) {
            names.push_back(name);
        }
        sort(names.begin(), names.end());

        // 提取桌号，并按餐桌桌号升序排列
        int m = foodsCnt.size();
        vector<int> ids;
        for (auto &[id, _] : foodsCnt) {
            ids.push_back(id);
        }
        sort(ids.begin(), ids.end());

        // 填写点菜展示表
        vector<vector<string>> table(m + 1, vector<string>(n + 1));
        table[0][0] = "Table";
        
        copy(names.begin(), names.end(), table[0].begin() + 1); // copy高级用法

        for (int i = 0; i < m; ++i) { 
            int id = ids[i];
            auto &cnt = foodsCnt[id];
            table[i + 1][0] = to_string(id);
            for (int j = 0; j < n; ++j) {
                table[i + 1][j + 1] = to_string(cnt[names[j]]);
            }
        }
        return table;
    }
};
