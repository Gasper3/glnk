from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

from app.types import RequestData


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class Url(Base):
    __tablename__ = 'urls'

    url: Mapped[str]
    short_url: Mapped[str | None]
    ip_address: Mapped[str | None]
    user_agent: Mapped[str | None]
    redirect: Mapped[bool] = mapped_column(default=False)

    visits: Mapped[list['UrlVisits']] = relationship(back_populates='url')

    def add_request_data(self, request_data: RequestData):
        self.user_agent = request_data.get('user_agent')
        self.ip_address = request_data.get('ip_address')
        return self


class UrlVisits(Base):
    __tablename__ = 'urlvisits'

    ip_address: Mapped[str]
    user_agent: Mapped[str]
    url_id: Mapped[int] = mapped_column(ForeignKey('urls.id'))

    url: Mapped[Url] = relationship(back_populates='visits')
