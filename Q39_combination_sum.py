class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]
        elements=[]
                                    
        def search(elements:List[int],target:int):
            if target <= 0:
               if target == 0:
                  for result in results:
                      if sorted(result) == sorted(elements)                                                                                                     return
                                                                                                                                                       results.append(elements[:])
                                                                                                                                                    return 
                                                                                                                                                                                                            
                                                                                                                                                  for candidate in candidates:
                 elements.append(candidate)                                                                                                           search(elements,target-candidate)
                 elements.pop()
                                                                                                                                                                                                                                                                                       search(elements,target)                                                                                                                                                                                                                                                 return results
