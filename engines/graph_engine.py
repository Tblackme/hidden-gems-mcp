from collections import deque

from hidden_gems.services.lastfm import similar_artists


class GraphEngine:

    def discover(
        self,
        seed_artists,
        depth=2,
        limit=25,
    ):

        queue = deque(seed_artists)

        visited = set()

        graph = {}

        current_depth = 0

        while queue and current_depth < depth:

            level_size = len(queue)

            for _ in range(level_size):

                artist = queue.popleft()

                if artist in visited:
                    continue

                visited.add(artist)

                try:

                    similar = similar_artists(
                        artist,
                        limit=limit,
                    )

                except Exception:
                    continue

                graph[artist] = similar

                for item in similar:

                    if item.name not in visited:
                        queue.append(item.name)

            current_depth += 1

        return graph