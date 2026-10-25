from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from projetopy.app import app
from projetopy.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    # cria uma conexao com o banco de dados

    table_registry.metadata.create_all(engine)
    # a tabela ja tem os metadados e com esses metadados ele cria a tabela
    with Session(engine) as session:
        # abre uma sessao de troca de informacoes entre o codigo e o banco
        yield session

    table_registry.metadata.drop_all(engine)
    # limpa o banco de dados pra cada teste


@contextmanager
def _mock_db_time(*, model, time=datetime(2026, 10, 25)):
    # asterisco obriga passar um model
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, 'created_at'):
            # hasattr devolve True se o objeto tem o atributo 'created_at'
            # protege caso o model nao tenha esse campo
            target.created_at = time
            # troca o created_at pelo horario fixo antes do INSERT

    event.listen(model, 'before_insert', fake_time_hook)
    # registra o hook pra ser chamado antes de cada INSERT do model
    yield time
    # entrega o horario fixo  pra quem usou a funcao
    event.remove(model, 'before_insert', fake_time_hook)
    # desregistra o hook pra que nao afete os outros testes


@pytest.fixture
def mock_db_time():
    return _mock_db_time
