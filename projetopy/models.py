from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    # o int faz que nao precisamos cuidar de ficar passando o id toda vez
    # ele ja eh cuidado pelo sql, e ele eh a chave primaria da tabela
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    # func.now faz que quando uma linha for inserida sem valor pra crated_at
    # deve ser preenchido com o horario atual do servidor
