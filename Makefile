VERSION = $(shell ls OliveTin*.tar.gz | sed 's/OliveTin-\([a-z0-9]*\)\-linux-amd64.tar.gz/\1/')

build:
	rpmbuild -ba --define '_topdir .' --clean --define 'version $(VERSION)' OliveTin.spec
