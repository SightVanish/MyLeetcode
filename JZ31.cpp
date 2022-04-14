class Solution_naive {
public:
    int NumberOf1Between1AndN_Solution(int n) {
        int count=0;
        for(int i=1; i<=n; i++)
        {
            int j = i;
            while(j!=0)
            {
                int l = j%10;
                j=j/10;
                if (l==1)    count++;
            }
        }
        return count;
    }
};

