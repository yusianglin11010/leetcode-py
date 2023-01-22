# https://leetcode.com/problems/restore-ip-addresses/description/
def restoreIpAddresses(s: str):
    ans = []
    def dfs(self, s, idx, path):
        if idx > 4:
            return 
        if idx == 4 and not s:
            ans.append(path[:-1])
        for i in range(1, len(s)+1):
            if s[:i] == "0" or (s[0] != "0" and int(s[:i]) < 256):
                dfs(s[i:], idx+1, path + s[:i] + ".")
    dfs(s, 0, "")
    return ans