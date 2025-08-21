import logging

from . import db_queries


def create_input(input: str) -> None:
    """Create input"""

    db_queries.create_input({"name": input})
    logging.info(f"The entry {input} is added!")
    