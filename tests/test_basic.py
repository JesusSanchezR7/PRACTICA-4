from app import app

def test_ruta_principal():
    cliente = app.test_client()
    respuesta = cliente.get('/')

    assert respuesta.status_code == 200
    assert b'Mi pipeline de DevOps funciona correctamente' in respuesta.data
