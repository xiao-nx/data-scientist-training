from typing import List, Dict

# https://leetcode.com/problems/accounts-merge/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 滑动窗口左右指针
        left, right = 0, 0
        n = len(nums)
        # 乘积
        prod = 1
        # 结果总数
        count = 0
        while right < n:
            # 每次计算以 right 为最右边元素的，乘积小于 k 的连续子序列，左边是 left
            # 先将 right 乘到 prod 中，因为必须包含 right
            prod *= nums[right]
            while prod >= k and left <= right:
                # 如果 prod 大于等于 k，就向右移动左指针 left，直到 prod < k
                # 每次移动 left，就将 left 从 prod 除掉，因为不再包含 left 的值
                prod /= nums[left]
                left += 1
            # 现在求出一个以 right 为右边界的连续子序列，其乘积小于 k
            # 因为这个子序列整体乘积都小于 k，那么其中每个子序列的乘积也小于 k
            # 因此以 right 为右边界的乘积小于 k 的连续子序列的个数就是这个序列的长度 right-left + 1
            # 将结果累加到 count 上
            count += right - left + 1
            # 每次向右移动 right 指针
            right += 1
        return count

s = Solution()

test = [1, 2, 3]
k = 0 

print(s.numSubarrayProductLessThanK(test, k))
