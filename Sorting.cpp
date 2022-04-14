#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
void MaxHeapify(int arr[], int startIndex, int endIndex)
{
    int parentNode=startIndex;
    int childNode=2*startIndex+1;
    while(childNode<=endIndex)
    {
        // compare the two child nodes, and choose the larger one
        if (childNode+1<=endIndex && arr[childNode]<arr[childNode+1])  childNode++;
        if (arr[parentNode]<arr[childNode])
        {
            swap(arr[parentNode], arr[childNode]);
            parentNode=childNode;
            childNode=parentNode*2+1;
        }
        else
            return;
    }
}
void HeapSort(int arr[], int length)
{
    // create the heap--start from the last parent node
    for(int i=length/2-1; i>=0; i--)    MaxHeapify(arr, i, length-1);

    for(int i=length-1; i>=0; i--)
    {
        swap(arr[0], arr[i]); // put the largest element to the end of array
        MaxHeapify(arr, 0, i-1); // rebalance the tree
    }
}
int main()
{
    int a[10]={23,6,156,9,13,33,12,1,11,43};

    // sort(a, a+10);
    HeapSort(a, 10);
    for(auto i:a)
    {
        cout<<i<<" ";
    }
    // cout<<maxBit(a, 10)<<endl;

    
    cout<<endl;
}