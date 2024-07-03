import unittest
from flask import Flask
from flask_testing import TestCase
from admin import app, mysql, User

class TestAdminPages(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['MYSQL_DB'] = 'test_db'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'your_password'
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['SECRET_KEY'] = 'your_secret_key'
        return app

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        # Set up a test database and add a test user
        cur = mysql.connection.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100), password VARCHAR(100))")
        cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
        mysql.connection.commit()
        cur.close()

    def tearDown(self):
        # Drop the test database
        cur = mysql.connection.cursor()
        cur.execute("DROP TABLE users")
        mysql.connection.commit()
        cur.close()
        self.app_context.pop()

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login_success(self):
        response = self.app.post('/login', data=dict(username='admin', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ようこそ', response.data)

    def test_protected_page(self):
        self.app.post('/login', data=dict(username='admin', password='password'))
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'個別指導マッチングシステム 管理者用ページ', response.data)

    def test_info_page(self):
        self.app.post('/login', data=dict(username='admin', password='password'))
        response = self.app.get('/info')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'生徒情報・講師情報 一覧', response.data)

    def test_logout(self):
        self.app.post('/login', data=dict(username='admin', password='password'))
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

if __name__ == '__main__':
    unittest.main()
