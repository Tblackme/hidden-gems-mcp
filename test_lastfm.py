from hidden_gems.services.multi_seed import discover

artists = discover([
    "Josiah Queen",
    "Benjamin William Hastings",
    "Chris Renzema",
])

print()

print("=" * 70)
print(" Hidden Gems ".center(70, "="))
print("=" * 70)

for artist in artists:

    print(
        f"{artist.score:>6} | "
        f"{artist.matches} seeds | "
        f"{artist.listeners:>8,} listeners | "
        f"{artist.name}"
    )