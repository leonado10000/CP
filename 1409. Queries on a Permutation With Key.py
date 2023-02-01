#1409. Queries on a Permutation With Key
import collections


def processQueries(self, queries: list[int], m: int) -> list[int]:
    ordered = collections.OrderedDict.fromkeys(range(1, m + 1))
    result = []
    for query in queries:
        idx = 0
        for key in ordered:
            print(key,"\tquery",query,"\tidx ==>",idx)
            if key == query: break
            idx += 1
        ordered.move_to_end(query, last=False)
        result.append(idx)
    return result

"""    p = list(range(1,m+1))
    ans = []
    for i in range(0,len(queries)):
        for j in range(0,len(p)):
            if p[j] == queries[i] :
                ans.append(j)
                s = p[j]
                del p[j]
                p = [s] + p
    return ans"""
    
    
print(processQueries(5,[3,1,2,1],5))