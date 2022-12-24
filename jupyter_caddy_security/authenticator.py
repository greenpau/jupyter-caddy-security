# coding: utf-8

import json
import base64
from typing import Union
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.auth import IdentityProvider, User


class CaddySecurityAuthenticator(IdentityProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = None
        self.server = None
        self.tokens = {}
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

    @staticmethod
    def base64_decode(s: str, altchars=b'+/') -> str:
        pad = len(s) % 4
        if pad:
            s += '=' * (4 - pad)
        return base64.b64decode(s, altchars)

    def get_user(self, handler: JupyterHandler) -> Union[User, None]:
        # self.log.info("received get_user request.")
        username = "anonymous"
        name = "Anonymous"
        if handler.request:
            if 'access_token' in handler.request.cookies:
                token = handler.request.cookies['access_token'].value
                if token in self.tokens:
                    return self.tokens[token]['user']
                encoded_payload = token.split('.')[1]
                decoded_payload = self.base64_decode(encoded_payload)
                d = json.loads(decoded_payload)
                if 'sub' in d:
                    username = d['sub']
                if 'name' in d:
                    name = d['name']
                # self.log.info("access_token: %s", decoded_payload)
                usr = User(username, name)
                self.tokens[token] = {
                    'user': usr,
                    'payload': d,
                }
                self.log.info("logged in user: %s", d)
        usr = User(username, name)
        return usr

    def identity_model(self, user: User) -> dict:
        return {
            "username": user.username,
            "name": user.name,
        }
