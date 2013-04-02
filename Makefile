all: bootstrap

bootstrap:
	./bootstrap.py
	./bin/pip install -r requirements.txt

