#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to n using the Sieve of Eratosthenes algorithm.

    Parameters:
    n (int): The upper limit to find prime numbers.

    Returns:
    List: A list of prime numbers up to n.
    """
    #Initialize a list to track prime status of numbers
    prime = [True] * (n + 1)
    p = 2   # Start with the first prime number

    # Mark non-prime numbers
    while (p *p <= n):
        if prime[p]: # If prime[p] is still True
            # Mark all multiples of p as False
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

  # Collect and return all prime numbers
    return [p for p in range(2, n + 1) if prime[p]]


def simulate_game(n):
    """
    Simulate a single round of the game between Maria and Ben.

    Parameters:
    n (int): The upper limit of the game (1 to n).

    Returns:
    str: The name of the winner ("Maria" or "Ben").
    """
    # Step 1: Find all primes up to n
    primes = sieve_of_eratosthenes(n)

    # Step 2: Initialize the game state
    available_numbers = set(range(1, n + 1))
    maria_wins = False

    # Step 3: Game loop
    turn = 0  # 0 for Maria, 1 for Ben
    while primes:
        # Determine the current player's chosen prime
        chosen_prime = primes[0]  # Both players pick the first available prime

        # Update the win status based on the current turn
        maria_wins = (turn == 0)

        # Remove chosen prime and its multiples from available numbers
        for multiple in range(chosen_prime, n + 1, chosen_prime):
            available_numbers.discard(multiple)

        # Update the list of primes based on available numbers
        primes = [p for p in primes if p in available_numbers]

        # Check if the next player can make a move
        if not primes:  # No primes left
            return "Maria" if maria_wins else "Ben"

        # Switch turns
        turn = 1 - turn  # Toggle between 0 and 1


def play_multiple_rounds(n, rounds):
    """
    Play multiple rounds of the game and determine the overall winner.

    Parameters:
    n (int): The upper limit of the game (1 to n).
    rounds (int): The number of rounds to play.

    Returns:
    None
    """
    maria_wins = 0
    ben_wins = 0

    # Play the specified number of rounds
    for _ in range(rounds):
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Display results
    print(f"Total rounds: {rounds}")
    print(f"Maria wins: {maria_wins}")
    print(f"Ben wins: {ben_wins}")

    # Determine the overall winner
    if maria_wins > ben_wins:
        overall_winner = "Maria"
    elif ben_wins > maria_wins:
        overall_winner = "Ben"
    else:
        overall_winner = "It's a tie!"

    print(f"Overall winner: {overall_winner}")

