from pprint import pprint

from hidden_gems.services.discovery import hidden_gems

results = hidden_gems(
    "Josiah Queen",
    max_listeners=50000,
)

pprint(results)
