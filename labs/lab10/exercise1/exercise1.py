num_rounds = int(input())

final_score = 0

for rounds_processed in range (1, num_rounds + 1):
    score = int(input())

    if score > 100:
        score = score * 1.20

    final_score = final_score + score


print(f"{final_score:.1f}")
print(rounds_processed)
