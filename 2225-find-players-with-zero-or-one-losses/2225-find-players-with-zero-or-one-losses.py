class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        win = Counter(matches[i][0] for i in range(len(matches)))
        loss = Counter(matches[i][1] for i in range(len(matches)))

        Wres, Lres = [], []
        for i in win.keys():
            if i not in loss:
                Wres.append(i)
        
        for i in loss.keys():
            if loss[i] == 1:
                Lres.append(i)
        
        return [sorted(Wres), sorted(Lres)]