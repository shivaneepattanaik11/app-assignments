#10. Unique Paths Problem
#Develop a Python program to determine the number of unique paths from the top-left corner to the bottom-right corner of a grid.
#Requirements
#Accept the number of rows and columns.
#Use Dynamic Programming.
#Display the total number of unique paths.

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

dp = [[0] * c for i in range(r)]

for i in range(r):
    dp[i][0] = 1

for j in range(c):
    dp[0][j] = 1

for i in range(1, r):
    for j in range(1, c):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print("Total number of unique paths:", dp[r-1][c-1])


#7. Longest Common Subsequence
#Develop a Python program to determine the length of the Longest Common Subsequence (LCS) between two strings.
#Requirements
#Accept two strings.
#Use Dynamic Programming.
#Display the LCS length.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

m = len(s1)
n = len(s2)

dp = [[0] * (n + 1) for i in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print("Length of LCS:", dp[m][n])