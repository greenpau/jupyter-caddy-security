# jupyter-caddy-security

Jupyter Identity Provider and Authorizer for Caddy Security

## Getting Started

Add `identity_provider_class` and `authorizer_class` to Jupyter Server
configuration file:

```py
import jupyter_caddy_security

c = get_config()
c.ServerApp.identity_provider_class = jupyter_caddy_security.CaddySecurityAuthenticator
c.ServerApp.authorizer_class = jupyter_caddy_security.CaddySecurityAuthorizer
```