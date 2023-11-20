class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        TG, TM, TP = 0, 0, 0
        travel.insert(0, 0)

        for i in range(len(garbage)):
            isTG, isTM, isTP = False, False, False

            for j in garbage[i]:
                if j == "M":
                    TM += 1
                    isTM = True
                elif j == "G":
                    TG += 1
                    isTG = True
                else:
                    TP += 1
                    isTP = True
            
            TG += travel[i]
            TM += travel[i]
            TP += travel[i]

            if isTG:
                ans += TG
                TG = 0
            
            if isTM:
                ans += TM
                TM = 0

            if isTP:
                ans += TP
                TP = 0
        return ans
