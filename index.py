# Number of members in each role
DISTRIBUTION = [
    ("Verified", 46349),
    ("Magnitude 1.0", 996),
    ("Magnitude 2.0", 32),
    ("Magnitude 3.0", 1),
    ("Magnitude 4.0", 0),
    ("Magnitude 5.0", 0),
    ("Magnitude 6.0", 0),
    ("Magnitude 7.0", 0),
    ("Magnitude 8.0", 0),
    ("Magnitude 9.0", 0),
]

# Assembly of leaders and mods
N_ASSEMBLY = 7

# Number of weeks before we converge to our target distribution
N_WEEKS_TOTAL = 24

# Number of weeks that have passed since March 17th, 2025
N_WEEKS_PASSED = 0


def calculate_nominations(n_verified, n_current, i, n_assembly):
    inertia = max(N_WEEKS_TOTAL - N_WEEKS_PASSED, 0)
    dropoff = 2 + 0.2 * inertia
    target = int(n_verified // dropoff**i)
    total_nominations = target - n_current
    nominations = total_nominations // n_assembly
    return target, nominations


def main():
    print(f"\n{'='*50}")
    print(f"WEEK {N_WEEKS_PASSED} NOMINATIONS".center(50))
    print('='*50)
    
    # Print header
    print(f"{'Role':<15} {'Target':>8} {'Current':>8} {'Nominations':>12}")
    print('-'*50)
    
    # Print each row
    for i in range(1, len(DISTRIBUTION)):
        name = DISTRIBUTION[i][0]
        n_verified = DISTRIBUTION[0][1]
        n_current = DISTRIBUTION[i][1]
        target, nominations = calculate_nominations(
            n_verified, n_current, i, N_ASSEMBLY)
        
        print(f"{name:<15} {target:>8,d} {n_current:>8,d} {nominations:>12,d}")
    
    print('='*50 + '\n')


if __name__ == "__main__":
    main()
