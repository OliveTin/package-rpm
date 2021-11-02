VERSION = $(shell ls SOURCES/OliveTin*.tar.gz | sed 's/SOURCES\/OliveTin-\([a-z0-9]*\)\-linux-amd64.tar.gz/\1/')

build:
	rpmbuild -ba --define '_topdir .' --clean --define 'version $(VERSION)' OliveTin.spec
