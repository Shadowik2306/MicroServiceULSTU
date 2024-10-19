from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class CustomModel(DeclarativeBase):
    pass


class BeautyWorkerModel(CustomModel):
    __tablename__ = 'worker'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]

    status: Mapped[str]




