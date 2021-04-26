class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        total_num = len(nums)
        
        def search(idx:int,elements:List[int]):
            if idx == total_num:
                results.append(elements[:])
                return
            
            elements.append(nums[idx])
            search(idx+1,elements)
            elements.pop()
            search(idx+1,elements)
                
        search(0,[])
        
        return results
