# coding: utf-8

from typing import Union
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.auth import IdentityProvider, User


class CaddySecurityAuthenticator(IdentityProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = None
        self.server = None
        for key, value in kwargs.items():
            if key == 'log':
                self.log = value
            elif key == 'parent':
                self.server = value
        if self.log is None:
            raise Exception("logger not found")
        if self.server is None:
            raise Exception("server not found")
        self.log.info("jupyter_caddy_security | identity provider initialized.")

    def get_user(self, handler: JupyterHandler) -> Union[User, None]:
        self.log.info("received get_user request.")
        return None

    def identity_model(self, user: User) -> dict:
        self.log.info("received identity_model for user '%s'.", str(user))
        return {}