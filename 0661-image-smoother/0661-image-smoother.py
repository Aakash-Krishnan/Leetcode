class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                total = cnt = 0
                
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i < 0 or i == ROWS or j < 0 or j == COLS:
                            continue
                        total += img[i][j] % 256
                        cnt += 1
                
                img[r][c] = img[r][c] ^ (total//cnt) << 8
        
        for i in range(ROWS):
            for j in range(COLS):
                img[i][j] = img[i][j] >> 8
        
        return img