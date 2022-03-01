from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


author_paper = Table(
    "author_paper",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("author.author_id")),
    Column("paper_id", Integer, ForeignKey("paper.paper_id")),
)


class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    papers = relationship(
        "Paper", secondary=author_paper, back_populates="authors"
    )


class Paper(Base):
    __tablename__ = "paper"
    paper_id = Column(Integer, primary_key=True)
    title = Column(String)
    authors = relationship(
        "Author", secondary=author_paper, back_populates="papers"
    )

