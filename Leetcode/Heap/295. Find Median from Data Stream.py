"""
링크 : https://leetcode.com/problems/find-median-from-data-stream/
솔루션 : https://leetcode.com/problems/find-median-from-data-stream/discuss/677080/Well-commented-python-code
Median 값을 구할 때 2개의 heap(minheap, maxheap)을 이용해서 중간값 구하기.
두개의 heap을 쓸 때 균형을 맞춰주기 위해서 값을 추가할 때 두 힙의 길이를 같게 보정해준다.
"""

import heapq
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo_heap = []
        self.hi_heap = []

    def addNum(self, num: int) -> None:
        if not self.lo_heap:
            return self.lo_heap.append(-num)
        if -self.lo_heap[0] > num:
            heapq.heappush(self.lo_heap, -num)
        else:
            heapq.heappush(self.hi_heap, num)

        if len(self.lo_heap) - 2 == len(self.hi_heap):
            heapq.heappush(self.hi_heap, -heapq.heappop(self.lo_heap))
        if len(self.hi_heap) - 2 == len(self.lo_heap):
            heapq.heappush(self.lo_heap, -heapq.heappop(self.hi_heap))

    def findMedian(self) -> float:
        if len(self.lo_heap) == len(self.hi_heap):
            return (-self.lo_heap[0] + self.hi_heap[0]) / 2.0
        elif len(self.lo_heap) > len(self.hi_heap):
            return -self.lo_heap[0]
        else:
            return self.hi_heap[0]
