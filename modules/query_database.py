
from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func

from modules.models import Author, Paper 
from treelib import Tree


def get_authors(session):
    """Get a list of author objects sorted by last name"""
    return session.query(Author).order_by(Author.last_name).all()

def get_author_by_lastname(session, lastname):
    return session.query(Author).filter_by(last_name=lastname).all()[0]

def get_papers_by_author(author):
    """Get list of all papers by given author

    Args:
        author: author object as defined in models
        ascending: direction to sort the results

    Returns:
        List: list of papers by that author
    """

    print(f"  Papers by {author.first_name} {author.last_name}:")
    for paper in author.papers:
        print("    ",paper.title)


def tree(authors):
    """
    Outputs the author/book/publisher information in
    a hierarchical manner

    :param authors:         the collection of root author objects
    :return:                None
    """
    authors_tree = Tree()
    authors_tree.create_node("Authors", "authors")
    for author in authors:
        author_id = f"{author.first_name} {author.last_name}"
        authors_tree.create_node(author_id, author_id, parent="authors")
        for paper in author.papers:
            paper_id = f"{author_id}:{paper.title}"
            authors_tree.create_node(paper.title, paper_id, parent=author_id)
    authors_tree.show()