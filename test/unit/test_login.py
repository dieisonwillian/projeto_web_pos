from unittest import TestCase
from valida.login import validalogin

class TestLogin(TestCase):
    def test_login_ok(self):
        sucesso=validalogin('admin','123456')
        self.assertTrue(sucesso)

    def test_login_erro(self):
        sucesso=validalogin('usrerrado','7891011')
        self.assertFalse(sucesso)