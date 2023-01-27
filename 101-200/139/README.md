# 139. Word Break

Review1: January 27, 2023
Tags: DFS, DP
URL: https://leetcode.com/problems/word-break/description/

## Question

---

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note** that the same word in the dictionary may be reused multiple times in the segmentation.

**Example 1:**

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

```

**Example 2:**

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

```

**Example 3:**

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

```

**Constraints:**

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

## Idea

---

- dfs + memorization
    - do partition for the given string
    - check if `prefix` and `suffix` in `wordDict`
    - we check `suffix` in `wordDict` by DFS search
    - use memorization to record if a substring has been check
- dp
    - initialize a dp array to record if `s[i+1]` could be break
    - for the given string `s` with `n`, we need to check if `s[:i]` could be break and `s[i:n]`
