#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def is_winner(x: int, nums: list[int]) -> str | None:
  """x - rounds
  nums - numbers list
  """
  if x <= 0 or nums is None:
    return None
  if x != len(nums):
    return None

  # Create a sieve of Eratosthenes to store prime numbers.
  sieve = [True] * (max(nums) + 1)
  sieve[0] = sieve[1] = False
  for i in range(2, int(max(nums) ** 0.5) + 1):
    if sieve[i]:
      for j in range(i * i, max(nums) + 1, i):
        sieve[j] = False

  # Count the number of prime numbers up to each number in the list.
  prime_counts = [0] * len(nums)
  for i in range(len(nums)):
    for j in range(2, nums[i] + 1):
      if sieve[j]:
        prime_counts[i] += 1

  # Calculate the score for each player.
  ben_score = 0
  maria_score = 0
  for i in range(len(nums)):
    if prime_counts[i] % 2 == 0:
      ben_score += 1
    else:
      maria_score += 1

  # Determine the winner.
  if ben_score > maria_score:
    return "Ben"
  elif maria_score > ben_score:
    return "Maria"
  else:
    return None


def remove_multiples(ls: list[int], x: int) -> None:
  """removes multiple
  of primes
  """
  for i in range(2, int(len(ls) ** 0.5) + 1):
    if ls[i]:
      for j in range(i * i, len(ls), i):
        ls[j] = 0


if __name__ == "__main__":
  x = int(input("How many rounds? "))
  nums = list(map(int, input("Enter the numbers: ").split()))

  winner = is_winner(x, nums)
  if winner is not None:
    print(f"{winner} wins!")
  else:
    print("The game is a tie.")
