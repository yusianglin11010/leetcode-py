from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.order_count = defaultdict(int)
        self.min_cnt = 0
        self.used = 0


    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        val = self.d[key][0]
        cnt = self.d[key][1]
        del self.order_count[cnt][key]
        self.d[key][1] += 1
        self.updateCacheCount(key, val, cnt+1)
        if self.min_cnt == cnt and len(self.order_count[cnt]) == 0:
            self.min_cnt = cnt + 1
        return self.d[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.d:
            self.d[key][0] = value
            cnt = self.d[key][1]
            self.d[key][1] += 1
            del self.order_count[cnt][key]
            self.updateCacheCount(key, value, cnt+1)
            if self.min_cnt == cnt and len(self.order_count[cnt]) == 0:
                self.min_cnt = cnt + 1
        else:
            if self.used < self.capacity:
                self.d[key] = [value, 1]
                self.updateCacheCount(key, value, 1)
                self.used += 1
                self.min_cnt = 1
            else:
                rm_key, _ = self.order_count[self.min_cnt].popitem(0)
                del self.d[rm_key]
                self.d[key] = [value, 1]
                self.updateCacheCount(key, value, 1)
                self.min_cnt = 1
                
    def updateCacheCount(self, key, val, new_cnt):
        if new_cnt not in self.order_count:
            self.order_count[new_cnt] = OrderedDict()
        self.order_count[new_cnt][key] = val
        self.order_count[new_cnt].move_to_end(key)