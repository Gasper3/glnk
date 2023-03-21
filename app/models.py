from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Url(Base):
    __tablename__ = 'urls'

    url: Mapped[str]
    short_url: Mapped[str] = mapped_column(nullable=False)
    ip_address: Mapped[str]
    user_agent: Mapped[str]

    visits: Mapped[list['UrlVisits']] = relationship(back_populates='url')


class UrlVisits(Base):
    __tablename__ = 'urlvisits'

    ip_address: Mapped[str]
    user_agent: Mapped[str]
    url_id: Mapped[int] = mapped_column(ForeignKey('urls.id'))

    url: Mapped[Url] = relationship(back_populates='visits')
