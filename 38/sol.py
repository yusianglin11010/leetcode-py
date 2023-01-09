def countAndSay(n):
    def say(target):
        left, step = 0, 1
        res = ""
        n = len(target)
        while left < n:
            while left + step < n and target[left] == target[left+step]:
                step += 1
            res += str(step) + target[left]
            left += step
            step = 1
        return res
    say_word = "1"
    for _ in range(1,n):
        say_word = say(say_word)
    return say_word