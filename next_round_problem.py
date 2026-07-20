line = input().split()

n = int(line[0])
k = int(line[1])

score_line = input().split()
scores = []

for i in range(n):
    scores.append(int(score_line[i]))

kth_score = scores[k - 1]
count = 0

for score in scores:
    if score >= kth_score and score > 0:
        count += 1

print(count)