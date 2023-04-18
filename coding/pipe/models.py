from dataclasses import dataclass
from typing import Dict, Iterable

Variation = Dict[str, str]


@dataclass
class Article:
    article_number: str
    variations: Iterable[Variation]


@dataclass
class Catalog:
    brand: str
    articles: Iterable[Article]
