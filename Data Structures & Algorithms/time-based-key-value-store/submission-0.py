class TimeMap:

    def __init__(self):
        self.t = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t:
            self.t[key] = []
        self.t[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t:
            return ""
        values = self.t[key]
        left = 0
        right= len(values)-1
        answer = ""
        while left<=right:
            med = (right+left)//2
            if values[med][0]<=timestamp:
                answer = values[med][1]
                left = med + 1
            else:
                right = med-1
        return answer
