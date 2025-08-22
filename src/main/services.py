import logging

from django.db.models import QuerySet

from . import db_queries


def get_input_list() -> QuerySet:
    """Get input list"""

    query = db_queries.get_input_list()
    logging.info(f"Count elems: {len(query)}")
    return query


def create_input(data: str) -> None:
    """Create input"""

    db_queries.create_input({"name": data})
    logging.info(f"The entry {data} is added!")
    