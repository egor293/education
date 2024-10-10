class Solution:
    def maximumNumberOfStringPairs(self, words):
        result=0
        for i in range(len(words)):
            words[i]=''.join(sorted(words[i]))
        for i in words:
            if words.count(i)==2:
                result+=1
                words.remove(i)
        return result
task=Solution()
print(task.maximumNumberOfStringPairs(["ku","dd","gu","uk"]))

