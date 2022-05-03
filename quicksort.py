def partition(nums, l, r):
  pivot = nums[l]
  i, j = l, r
  while i < j:
    # find the first element smaller than pivot
    while i < j and nums[j] >= pivot:
      j -= 1
    nums[i] = nums[j] # put the smaller one to the left
    # find the first element larger than pivot
    while i < j and nums[i] <= pivot:
      i += 1
    nums[j] = nums[i] # put the larger one to the right
  # i == j, nums[i]=nums[j]>pivot
  nums[i] = pivot
  
  return i

def quicksort(nums, l, r):
  if l < r:
    mid = partition(nums, l, r)
    quicksort(nums, l, mid - 1)
    quicksort(nums, mid + 1, r)


arr = [1,3,4,2,2,0]
quicksort(arr, 0, len(arr)-1)
print(arr)