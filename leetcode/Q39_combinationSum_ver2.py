class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def search(csum,idx,cpath):
            if csum < 0:
                return
            if csum == 0:
                results.append(cpath)
                return
            
            for i in range(idx,len(candidates)):
                search(csum-candidates[i],i,cpath+[candidates[i]])
                
        search(target,0,[])
        return results
