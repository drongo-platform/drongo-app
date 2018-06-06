import logging

from wing_database import Database

from wing_module import Module

from .validators import UsernameValidator, PasswordValidator


class Auth(Module):
    """Drongo module for authentication and authorization"""

    __default_config__ = {
        'api_base_url': '/api/auth',

        'create_admin_user': True,
        'admin_user': 'admin',
        'admin_password': 'admin',

        'active_on_register': False,

        'token_age': 7 * 24 * 60,  # A week (in minutes)

        # Validators
        'username_validator': UsernameValidator,
        'password_validator': PasswordValidator
    }

    logger = logging.getLogger('wing_auth')

    def init(self, config):
        self.logger.info('Initializing [auth] module.')

        self.app.context.modules.auth = self

        self.database = self.app.context.modules.database[config.database]

        if self.database.type == Database.MONGO:
            from .backends._mongo import services
            self.services = services

        else:
            raise NotImplementedError

        services.AuthServiceBase.init(module=self)

        if config.create_admin_user:
            try:
                services.UserCreateService(
                    username=config.admin_user,
                    password=config.admin_password,
                    active=True,
                    superuser=True
                ).call()
            except Exception as e:
                self.logger.info(str(e))

        self.init_api()

    def init_api(self):
        from .api import AuthAPI
        self.api = AuthAPI(
            app=self.app,
            module=self,
            base_url=self.config.api_base_url
        )

    def object_owner_set(self, object_type, object_id, username):
        return self.services.ObjectOwnerSetService(
            object_type, object_id, username
        ).call()

    def permission_check(self, permission_id, username):
        return self.services.PermissionCheckService(
            permission_id, username).call()

    def object_permission_check(self, object_type, object_id, permission_id,
                                username):
        return self.services.ObjectPermissionCheckService(
            object_type, object_id, permission_id, username).call()
