from typing import Dict, Iterable, List

from map_reduce.reduce import Grouping, Reduce

from .models import Article, Catalog


class CatalogReduce(Reduce[Grouping[Grouping[Dict[str, str]]], List[Catalog]]):
    """Reduces grouped objects to a list of Catalogs."""

    def reduce(
        self, inputs: Iterable[Grouping[Grouping[Dict[str, str]]]]
    ) -> List[Catalog]:
        return [
            Catalog(
                brand_group.key,
                [
                    Article(articles_group.key, articles_group.values)
                    for articles_group in brand_group.values
                ],
            )
            for brand_group in inputs
        ]
