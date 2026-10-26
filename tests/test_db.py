from dataclasses import asdict

from sqlalchemy import select

from projetopy.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        # o with chama mock_db_time e roda a funcao ate o yield registra o hook
        # o as time guarda em "time" o valor do yield (o datetime fixo)
        new_user = User(username='test', email='test@test', password='123')

        session.add(new_user)
        session.commit()
        # commit eh o que efetivamente envia o INSERT e grava no banco

        user = session.scalar(select(User).where(User.username == 'test'))
        # o select monta a consulta e ORM converte a linha do banco em User
        # o scalar devolve so o primeiro resultado (ou None se nao achar nada)
        assert asdict(user) == {
            'id': 1,
            'username': 'test',
            'email': 'test@test',
            'password': '123',
            'created_at': time,
            'updated_at': time,
        }
        # asdict transforma um objeto dataclass em dicionario
        # dataclass eh uma forma de gerar uma classe sem escrever
        # na mao os metodos repetitivos, init, repr, eq
