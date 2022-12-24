# coding: utf-8

from typing import Any
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.auth import Authorizer


class CaddySecurityAuthorizer(Authorizer):
    """Class for authorizing access to resources in Jupyter Server with
    Caddy Security.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = None
        self.server = None
        # The identity_provider is being inherited from Authorizer.
        #self.identity_provider = None
        for key, value in kwargs.items():
            if key == 'log':
                self.log = value
            elif key == 'parent':
                self.server = value
        if self.identity_provider is None:
            raise Exception("identity_provider not found")
        if self.log is None:
            raise Exception("logger not found")
        if self.server is None:
            raise Exception("server not found")
        self.log.info("jupyter_caddy_security | authorizer initialized.")

    def is_authorized(self, handler: JupyterHandler, user: Any, action: str, resource: str) -> bool:
        if not user:
            return False
        if user.username == 'anonymous':
            return False
        return True
