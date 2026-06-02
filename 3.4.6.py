from collections import defaultdict

votes = defaultdict(int)
spoiled = 0
total = 0

with open("votes.txt") as f:
    for token in f.read().split():
        try:
            v = int(token)
        except ValueError:
            spoiled += 1
            total += 1
            continue
        
        if v == -1:
            spoiled += 1
        elif 1 <= v <= 5:
            votes[v] += 1
        else:
            spoiled += 1
        total += 1

valid_total = sum(votes.values())

results = sorted(votes.items(), key=lambda x: x[1], reverse=True)

for rank, (party, count) in enumerate(results, 1):
    pct = count / total * 100
    print(f"{rank}. Партия №{party} | {count:>6} | {pct:.2f}%")

print(f"\nИспорченных бланков: {spoiled} ({spoiled/total*100:.2f}%)")