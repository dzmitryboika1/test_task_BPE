"""There are gold coins in N baskets. The baskets are numbered from 1 to N.
In all baskets, except for one, the coins weigh w grams each.
In one basket, the coins are counterfeit and weigh w–d grams.
The wizard takes 1 coin from the first basket, 2 coins from the second basket,
and so on, and finally N-1 coins from the (N-1)th basket. He does not take anything from the Nth basket.
He weighs the coins he has taken and immediately points to the basket of counterfeit coins.
Write a program that can do this kind of magic.
Given: four integers: N, w, d and P - the total weight of the selected coins.
 Find the number of the basket with counterfeit coins."""

N, w, d, P = (int(i) for i in input().split()) # read input values

total = 0

for i in range(1, N):
    total += i * w

if total == P:
    print(N)
else:
    print(abs((P - total)) // d)
