class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def __init__(self):
            pass

        result = []
        p1 = 0
        p2 = 0
        while(p1 < m and p2 < n):
            if (nums1[p1] <= nums2[p2]):
                result.append(nums1[p1])
                p1+=1
            else:
                result.append(nums2[p2])
                p2+=1

        while(p1 < m):
            result.append(nums1[p1])
            p1+=1

        while(p2 < n):
            result.append(nums2[p2])
            p2+=1

        nums1 = result
        print(nums1)

if __name__ == "__main__":

    obj = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    obj.merge(nums1, m, nums2, n)
