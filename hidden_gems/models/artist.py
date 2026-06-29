from dataclasses import dataclass, field


@dataclass
class Artist:

    name: str

    listeners: int = 0

    playcount: int = 0

    similarity: float = 0.0

    matches: int = 0

    score: float = 0.0

    genres: list[str] = field(default_factory=list)

    albums: list[str] = field(default_factory=list)

    country: str = ""

    last_release: str = ""

    source: str = "Last.fm"