from collections import defaultdict

votes = defaultdict(int)
spoiled = 0
total = 0

# votes.txt содержит намеренно испорченные данные для тестирования всех исключений:
# - "abc"  → не является числом → ValueError
# - "-1"   → явно испорченный бюллетень (маркер порчи)
# - "14", "10" → число вне допустимого диапазона 1–5

try:
    f = open("votes.txt")
except FileNotFoundError:
    print("Ошибка: файл 'votes.txt' не найден. Проверьте наличие файла с данными.")
    exit(1)

with f:
    for token in f.read().split():
        try:
            v = int(token)          # Исключение 1: ValueError — если токен не число (напр. "abc")
        except ValueError:
            # Токен не является целым числом → испорченный бюллетень
            spoiled += 1
            total += 1
            continue

        if v == -1:
            # Исключение 2: значение -1 — явный маркер испорченного бюллетеня
            spoiled += 1
        elif 1 <= v <= 5:
            # Корректный голос — номер партии от 1 до 5
            votes[v] += 1
        else:
            # Исключение 3: число вне диапазона 1–5 (напр. 10, 14) → испорченный
            spoiled += 1
        total += 1

valid_total = sum(votes.values())

results = sorted(votes.items(), key=lambda x: x[1], reverse=True)

print("=== Результаты голосования ===")
for rank, (party, count) in enumerate(results, 1):
    pct = count / total * 100
    print(f"{rank}. Партия №{party} | {count:>6} | {pct:.2f}%")

print(f"\nВсего бюллетеней:    {total}")
print(f"Действительных:      {valid_total} ({valid_total/total*100:.2f}%)")
print(f"Испорченных бланков: {spoiled} ({spoiled/total*100:.2f}%)")