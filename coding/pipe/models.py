from collections import defaultdict
from dataclasses import dataclass, field, Field, fields, make_dataclass
from typing import Dict, List, Tuple

Variation = Dict[str, str]


class FieldMeta:
    def __init__(self, key: str, type: type, default: Field):
        self.key = key
        self.type = type
        self.default = default

    def __eq__(self, o: object) -> bool:
        return getattr(o, "key", None) == self.key

    def __hash__(self) -> int:
        return hash(self.key)

    def __repr__(self) -> str:
        return f"{self.key}: {self.type} = {self.default.default}"  # pragma: no cover

    def to_tuple(self) -> Tuple[str, type, Field]:
        return self.key, self.type, self.default


@dataclass
class Article:
    article_number: str
    variations: List[Variation]

    def __post_init__(self):
        """**Note: This might be done in another Reduce, but is done here to demonstrate dataclass capabilities**

        Extract common fields from variations and create a new dataclass for them.
        This new dataclass only contains fields with distinct values.
        Note that the Article dataclass is also modified to include the common fields"""
        keys: Dict[Tuple[str, str], int] = defaultdict(int)
        n = 0

        for variation in self.variations:
            for k, v in variation.items():
                keys[(k, v)] += 1
            n += 1

        common_fields = set()
        common_field_names = set()
        other_fields = set()

        for k, v in keys.items():
            if v == n:
                common_field_names.add(k[0])
                common_fields.add(FieldMeta(k[0], str, field(init=False, default=k[1])))
            else:
                other_fields.add(FieldMeta(k[0], str, field(init=True, default=None)))

        self.__class__ = make_dataclass(
            "ArticleX", (f.to_tuple() for f in common_fields), bases=(Article,)
        )
        variation_class = make_dataclass(
            "Variation", (f.to_tuple() for f in other_fields)
        )

        variations = []
        for variation in self.variations:
            variations.append(
                variation_class(
                    **{
                        k: v
                        for k, v in variation.items()
                        if k not in common_field_names
                    }
                )
            )

        self.variations = variations


@dataclass
class Catalog:
    brand: str
    articles: List[Article]

    def __post_init__(self):
        """**Note: This might be done in another Reduce, but is done here to demonstrate dataclass capabilities**

        Extract common fields from articles and create a new dataclass for them.
        This new dataclass only contains fields with distinct values.
        Note that the Catalog dataclass is also modified to include the common fields"""
        keys: Dict[Tuple[str, str], int] = defaultdict(int)
        n = 0

        for article in self.articles:
            for k in fields(article):
                if k.name == "variations":
                    continue
                keys[(k.name, getattr(article, k.name))] += 1
            n += 1

        common_fields = set()
        common_field_names = set()
        other_fields = set()
        other_fields.add(
            FieldMeta("variations", List[Variation], field(default_factory=list))
        )

        for k, v in keys.items():
            if v == n:
                common_field_names.add(k[0])
                common_fields.add(FieldMeta(k[0], str, field(init=False, default=k[1])))
            else:
                other_fields.add(FieldMeta(k[0], str, field(init=True, default=None)))

        self.__class__ = make_dataclass(
            "CatalogX", (f.to_tuple() for f in common_fields), bases=(Catalog,)
        )
        article_class = make_dataclass("ArticleY", (f.to_tuple() for f in other_fields))

        articles = []
        for article in self.articles:
            article_new = article_class(
                **{
                    k.name: getattr(article, k.name)
                    for k in fields(article)
                    if k.name not in common_field_names
                }
            )
            article_new.variations = article.variations
            articles.append(article_new)

        self.articles = articles
