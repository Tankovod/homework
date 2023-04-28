# ------------- LESSON 5, EXERCISE 7 -------------------
# In witcher's world there are coins of denomination 1, 5, 10, 25
# Write the program that defines minimal amount of coins to pay to the witcher

sum_of_gold = 0
while sum_of_gold == 0:
    try:
        sum_of_gold = int(input('How much gold should be given to the witcher?> '))
    except ValueError:
        print('Exception ! Try any whole number !')

# ----- 1st way -----
extra_coins = sum_of_gold % 25
coin25 = (sum_of_gold - extra_coins) / 25
coin10 = (extra_coins - extra_coins % 10) / 10
extra_coins = extra_coins - coin10 * 10
coin5 = (extra_coins - extra_coins % 5) / 5
extra_coins = extra_coins - coin5 * 5
coin1 = (extra_coins - extra_coins % 1) / 1

print(f'~~~ You need {int(coin25)} coins with value 25, {int(coin10)} with value 10,'
      f' {int(coin5)} with value 5 and {int(coin1)} with value 1.~~~')


# ----- 1st way -----

# ----- 2nd way -----
def coin_plus(coins, all_gold, coin_number):
    coin_count, result_coins = 0, coins
    while coin_number and coin_number * (coin_count + 1) <= all_gold - coins:
        result_coins += coin_number
        coin_count += 1
    return result_coins, coin_count


final_coins = 0

final_coins, coin25 = coin_plus(final_coins, sum_of_gold, 25)
final_coins, coin10 = coin_plus(final_coins, sum_of_gold, 10)
final_coins, coin5 = coin_plus(final_coins, sum_of_gold, 5)
final_coins, coin1 = coin_plus(final_coins, sum_of_gold, 1)

print(f'~~~ You need {coin25} coins with value 25, {coin10} with value 10,'
      f' {coin5} with value 5 and {coin1} with value 1.~~~')
# ----- 2nd way -----

# ----- 3rd way -----
coin1, coin5, coin10, coin25 = 0, 0, 0, 0

while 25 * (coin25 + 1) <= sum_of_gold:
    coin25 += 1
while 10 * (coin10 + 1) <= sum_of_gold - coin25 * 25:
    coin10 += 1
while 5 * (coin5 + 1) <= sum_of_gold - coin25 * 25 - coin10 * 10:
    coin5 += 1
while 1 and coin1 < sum_of_gold - coin25 * 25 - coin10 * 10 - coin5 * 5:
    coin1 += 1

print(f'~~~ You need {coin25} coins with value 25, {coin10} with value 10,'
      f' {coin5} with value 5 and {coin1} with value 1.~~~')
# ----- 3rd way -----

# ----- 4th way -----
coin25 = sum_of_gold // 25
coin10 = (sum_of_gold - coin25 * 25) // 10
coin5 = (sum_of_gold - coin25 * 25 - coin10 * 10) // 5
coin1 = (sum_of_gold - coin25 * 25 - coin10 * 10 - coin5 * 5) // 1

print(f'~~~ You need {coin25} coins with value 25, {coin10} with value 10,'
      f' {coin5} with value 5 and {coin1} with value 1.~~~')
# ----- 4th way -----

# ----- 5th way -----
coin_list, some_gold = [], sum_of_gold
for numb in [25, 10, 5, 1]:
    coin_list.append(coin := some_gold // numb)
    some_gold -= coin * numb

print(f'~~~ You need {coin_list[0]} coins with value 25, {coin_list[1]} with value 10,'
      f' {coin_list[2]} with value 5 and {coin_list[3]} with value 1.~~~')
# ----- 5th way -----

