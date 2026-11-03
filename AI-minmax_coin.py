
coins = [8, 15, 3, 7, 12]

def minimax(coins, left, right, player):

    if left > right:
        return 0

    if player == 1:  # AI turn
        take_left = coins[left] + minimax(coins, left + 1, right, 0)
        take_right = coins[right] + minimax(coins, left, right - 1, 0)

        return max(take_left, take_right)

    else:  # Human turn
        take_left = -coins[left] + minimax(coins, left + 1, right, 1)
        take_right = -coins[right] + minimax(coins, left, right - 1, 1)

        return min(take_left, take_right)


left = 0
right = len(coins) - 1

ai_score = 0
human_score = 0

print("Coin Game using Minimax")
print("Coins:", coins)

while left <= right:

    # AI turn
    if coins[left] >= coins[right]:
        coin = coins[left]
        left += 1
    else:
        coin = coins[right]
        right -= 1

    ai_score += coin
    print("AI takes:", coin)

    if left > right:
        break

    # Human turn
    choice = input("Choose L or R: ").upper()

    if choice == "L":
        coin = coins[left]
        left += 1
    else:
        coin = coins[right]
        right -= 1

    human_score += coin
    print("You take:", coin)

print("AI Score:", ai_score)
print("Human Score:", human_score)

if ai_score > human_score:
    print("AI Wins!")
elif human_score > ai_score:
    print("Human Wins!")
else:
    print("Draw!")
