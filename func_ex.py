import random
from time import process_time

# def game(min_bet, max_bet, balance):
#     counter = 0
#     current_bet = min_bet
#     current_balance = balance
#
#     while current_balance > 0:
#         counter += 1
#         current_balance -= current_bet
#         rand_choice = random.randint(0, 1)
#
#         if rand_choice == 1:
#             current_balance += current_bet * 2
#             current_bet = min_bet
#         else:
#             current_bet *= 2
#             if current_bet > max_bet:
#                 current_bet = max_bet
#             if current_bet > current_balance:
#                 current_bet = current_balance
#
#     print(f"Количестов шагов = {counter}")
#     return counter
#
# game(1, 10, 100)

def house(flat_number, floors, entrances):
    flats_in_one_entrance = floors * 4
    total_flats = flats_in_one_entrance * entrances
    if flat_number < 1 or flat_number > total_flats:
        print("Такой квартиры нет в доме")

    entrance_number = (flat_number - 1) // flats_in_one_entrance + 1  # номер подъезда
    print(f"Номер подъезда {entrance_number}")

    floor_number = (flat_number - 1) % 20 // 4 + 1
    print(f"Этаж {floor_number}")

    return entrance_number, floor_number

house(13, 9, 5)

