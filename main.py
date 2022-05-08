# Elo Rating System

import math

K = int(input("Enter K-factor: "))
d = float(input("Loss, draw or win for ratingA (0, 0.5 or 1): "))
rating_a = float(input("Enter RatingA: "))
rating_b = float(input("Enter RatingB: "))


def probability(rating_a, rating_b):
    return 1 / (1 + math.pow(10, ((rating_a - rating_b) / 400)))   # Algorithm


def elo(rating_a, rating_b, K, d):
    Pro_b = probability(rating_a, rating_b)
    Pro_a = probability(rating_b, rating_a)

    if d == 1:
       rating_a = rating_a + K * (1 - Pro_a)
       rating_b = rating_b + K * (0 - Pro_b)

    if d == 0:
       rating_a = rating_a + K * (0 - Pro_a)
       rating_b = rating_b + K * (1 - Pro_b)


    if d == 0.5:
        rating_a = rating_a + K * (0.5 - Pro_a)
        rating_b = rating_b + K * (0.5 - Pro_b)


    print("New Elo:")
    print("Rating A =", round(rating_a, 6), " Rating B =", round(rating_b, 6))


if __name__ == "__main__":
   elo(rating_a, rating_b, K, d)


