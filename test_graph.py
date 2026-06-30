from hidden_gems.engines.graph_engine import GraphEngine

engine = GraphEngine()

graph = engine.discover(
    ["Josiah Queen"],
    depth=2,
    limit=10,
)

print()

for artist, similar in graph.items():

    print(artist)

    print(len(similar))