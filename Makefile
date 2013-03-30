all: bootstrap

bootstrap:
	[ -e bin/python ] || virtualenv .

install-deps:
	pip install -r requirements.txt
