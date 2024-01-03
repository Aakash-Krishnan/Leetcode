class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        result = 0
        prevFloor = 0
        
        for floor in bank:
            devices = floor.count("1")
            if prevFloor:
                result += (prevFloor * devices)
            
            if devices:
                prevFloor = devices
        return result