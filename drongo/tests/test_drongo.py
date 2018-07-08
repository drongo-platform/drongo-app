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

    def test_match_by_method(self):
        def sample1(ctx):
            return 'Hello, World!'


        def sample2(ctx):
            return 'World, Hello!'

        self.app.add_url('/', 'GET', sample1)
        self.app.add_url('/', 'POST', sample2)

        sample_env = dict(
            REQUEST_METHOD='GET',
            GET='',
            PATH_INFO='/'
        )

        resp = self.app(sample_env, self.start_response)
        self.assertIn(b'Hello, World!', resp)

        self.app.add_url('/', None, sample1)
        self.app.add_url('/test', ['POST', 'PUT'], sample2)

        sample_env = dict(
            REQUEST_METHOD='POST',
            GET='',
            PATH_INFO='/test'
        )

        resp = self.app(sample_env, self.start_response)
        self.assertIn(b'World, Hello!', resp)

        sample_env = dict(
            REQUEST_METHOD='PUT',
            GET='',
            PATH_INFO='/test'
        )

        resp = self.app(sample_env, self.start_response)
        self.assertIn(b'World, Hello!', resp)

    def test_middleware_basic(self):
        class Middleware(object):
            def before(slf, ctx):
                self.before_called = True

            def after(slf, ctx):
                self.after_called = True

        self.app.add_middleware(Middleware())

        def sample(ctx):
            return 'Hello, World!'

        self.app.add_url('/', 'GET', sample)

        sample_env = dict(
            REQUEST_METHOD='GET',
            GET='',
            PATH_INFO='/'
        )

        self.app(sample_env, self.start_response)
        self.assertTrue(self.before_called)
        self.assertTrue(self.after_called)

    def test_middleware_exception(self):
        class Middleware(object):
            def exception(slf, ctx, exc):
                self.exception_called = True

        self.app.add_middleware(Middleware())

        def sample(ctx):
            raise Exception('Bug')

        self.app.add_url('/', 'GET', sample)

        sample_env = dict(
            REQUEST_METHOD='GET',
            GET='',
            PATH_INFO='/'
        )

        self.app(sample_env, self.start_response)
        self.assertTrue(self.exception_called)
