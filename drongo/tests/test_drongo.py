import unittest


from drongo import Drongo


class BasicDrongoTest(unittest.TestCase):
    def setUp(self):
        self.app = Drongo()

    def start_response(self, status_code, headers):
        self.status_code = status_code
        self.headers = headers

    def test_basic_request(self):
        sample_env = dict(
            REQUEST_METHOD='GET',
            GET='',
            PATH_INFO='/'
        )

        self.app(sample_env, self.start_response)
        self.assertIn('404', self.status_code)

    def test_simple_url(self):
        sample_env = dict(
            REQUEST_METHOD='GET',
            GET='',
            PATH_INFO='/'
        )

        def sample(ctx):
            return 'Hello, World!'

        self.app.add_url('/', 'GET', sample)

        self.app(sample_env, self.start_response)
        self.assertIn('200', self.status_code)

    def test_exception_url(self):
        sample_env = dict(
            REQUEST_METHOD='GET',
            GET='',
            PATH_INFO='/'
        )

        def sample(ctx):
            raise Exception('I\'m a buggy endpoint!')

        self.app.add_url('/', 'GET', sample)

        self.app(sample_env, self.start_response)
        self.assertIn('500', self.status_code)
