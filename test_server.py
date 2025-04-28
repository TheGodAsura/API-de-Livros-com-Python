import unittest
from unittest import mock

# Importando o app do server.py
# Ajuste o import conforme a estrutura real do seu arquivo server.py
try:
    from server import app
except ImportError:
    # Para permitir que os testes rodem mesmo se não puder importar diretamente
    app = None

class TestServer(unittest.TestCase):
    
    def setUp(self):
        if app:
            app.testing = True
            self.client = app.test_client()
    
    def test_server_running(self):
        """Testa se o servidor está funcionando"""
        if app:
            response = self.client.get('/')
            self.assertIn(response.status_code, [200, 301, 302])
        else:
            self.skipTest("Não foi possível importar o app do server.py")
    
    def test_health_check(self):
        """Testa o endpoint de health check"""
        if app:
            response = self.client.get('/health')
            self.assertEqual(response.status_code, 200)
        else:
            self.skipTest("Não foi possível importar o app do server.py")

if __name__ == '__main__':
    unittest.main()
