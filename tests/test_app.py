from http import HTTPStatus

from fastapi.testclient import TestClient

from projetopy.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 atapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUI)
    - A: Assert  - Garante que A é A
    """
    # arrange(carrega os dados que vamos precisar)
    client = TestClient(app)

    # act(faz a acao do teste)
    response = client.get('/')

    # assert(garante que esta certo )
    assert response.json() == {'message': 'Ola mundo!'}
    assert response.status_code == HTTPStatus.OK
