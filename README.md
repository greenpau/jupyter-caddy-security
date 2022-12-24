# jupyter-caddy-security

Jupyter Identity Provider and Authorizer for Caddy Security

## Getting Started

Install `jupyter-caddy-security`:

```bash
git clone https://github.com/greenpau/jupyter-caddy-security.git
cd jupyter-caddy-security
make package
pip install dist/jupyter-caddy-security-1.0.0.tar.gz --user
```

Add `identity_provider_class` and `authorizer_class` to Jupyter Server
configuration file:

```py
import jupyter_caddy_security

c = get_config()
c.ServerApp.identity_provider_class = jupyter_caddy_security.CaddySecurityAuthenticator
c.ServerApp.authorizer_class = jupyter_caddy_security.CaddySecurityAuthorizer
```