.PHONY: build license envvar package test
.PHONY: package_build package_clean package_zip package
.PHONY: release

PKG_NAME=jupyter-caddy-security
PKG_NAME_EGG:=$(subst -,_,$(PKG_NAME))
PKG_VERSION:=$(shell cat setup.py| grep "__version__ =" | cut -d"'" -f2 | head -1)
GIT_COMMIT:=$(shell git describe --dirty --always)
GIT_BRANCH:=$(shell git rev-parse --abbrev-ref HEAD -- | head -1)
BUILD_USER:=$(shell whoami)
BUILD_DATE:=$(shell date +"%Y-%m-%d")
VERBOSE:=-v

all: envvar build
	@echo "$@: complete"

envvar:
	@echo "Version: $(PKG_VERSION), Branch: $(GIT_BRANCH), Revision: $(GIT_COMMIT)"
	@echo "Build on $(BUILD_DATE) by $(BUILD_USER)"

build:
	@for f in `find ./ -type f -name '*.py'`; do autopep8 --in-place $$f; done
	@echo "$@: complete"

license:
	@#pip install autopep8 --user
	@versioned || go install github.com/greenpau/versioned/cmd/versioned@latest
	@#for f in `find ./ -type f -name '*.go'`; do versioned -addlicense -copyright="Paul Greenberg greenpau@outlook.com" -year=2022 -filepath=$$f; done
	@#for f in `find ./ -type f -name '*.go'`; do versioned -striplicense -filepath=$$f; done
	@echo "$@: complete"

test:
	@echo "$@: complete"

clean:
	@find . -name \*.pyc -delete
	@rm -rf dist/ build/ *.egg-info/

package_build:
	@python setup.py sdist
	@echo "$@: complete"

package_clean:
	@rm -rf ${PKG_NAME_EGG}.egg-info *.egg build/
	@find . -name \*.pyc -delete

package_zip:
	@tar -tvf dist/${PKG_NAME}-${PKG_VERSION}.tar.gz

package: package_clean package_build package_zip
	@rm -rf ${PKG_NAME_EGG}.egg-info *.egg build/
	@find . -name \*.pyc -delete
	@echo "$@: complete"