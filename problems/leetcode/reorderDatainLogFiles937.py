"""
_________________________937. Reorder Data in Log Files_________________________
Difficulty: Easy		Likes: 414		Dislikes: 1281		Solution: Available
Total Accepted: 79.6K		Total Submission: 148.3K		Acceptance Rate: 53.6%
Tags:  String


You have an array of logs.  Each log is a space delimited string of words.
For each log, the first word in each log is an alphanumeric identifier. 
Then, either:  Each word after the identifier will consist only of
lowercase letters, or; Each word after the identifier will consist only
of digits.  We will call these two varieties of logs letter-logs and
digit-logs.  It is guaranteed that each log has at least one word after its
identifier. Reorder the logs so that all of the letter-logs come before
any digit-log.  The letter-logs are ordered lexicographically ignoring
identifier, with the identifier used in case of ties.  The digit-logs should
be put in their original order. Return the final order of the logs.   


Example 1:Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 0 <= logs.length <= 1003 <= logs[i].length <= 100logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""


def reorderLogFiles(logs):
	import itertools
	temp=[i.split(' ') for i in logs]
	return [" ".join(i) for i in iter(sorted([i for i in temp if i[1].isalpha()], key=lambda x: "".join(itertools.islice(x,1,len(x)))))]+[" ".join(i) for i in temp if i[1].isdigit()]





if __name__ == "__main__":
	logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
	print(reorderLogFiles(logs,))


"""
"""
