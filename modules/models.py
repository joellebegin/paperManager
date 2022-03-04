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

paper_tag = Table(
    "paper_tag",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("paper.paper_id")),
    Column("tag_id", Integer, ForeignKey("tag.tag_id")),
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
    year = Column(String)
    
    authors = relationship(
        "Author", secondary=author_paper, back_populates="papers"
    )

    tags = relationship(
        "Tag", secondary=paper_tag, back_populates="papers"
    )
    

class Tag(Base):
    __tablename__ = "tag"
    tag_id = Column(Integer, primary_key=True)
    tag = Column(String)
    papers = relationship(
        "Paper", secondary=paper_tag, back_populates="tags"
    )


