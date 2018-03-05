# Given a array with +ve and -ve integer , find the maximum sum such that you are not allowed to skip 2 contiguous elements ( i.e you have to select at least one of them to move forward).

Solution:

Used Dynamic-programming algorithm to find the maximum sum.

If arr is the given array and n is number of items in the array.
For any index i < n, 
if i == 0,  dp[i] = arr[i] 
if i == 1,  dp[i] = max(dp[0] + arr[1], arr[1])
if i >= 2,  dp[i] = max(dp[i-1] + arr[i], dp[i-2] + arr[i])

To ensure that we don't skip 2 contiguous elements, each element at index i will be either included with maximum sum 
encountered including the element at i-1 or with the maximum sum encountered including element at index i - 2.

Solution would be maximum of (dp[n-2], dp[n-1]).

Time Complexity of algorithm is O(n)
Space Complexity of algorithm is O(n)
           
