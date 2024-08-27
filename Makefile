all: install integrate

install:
	pyinstaller --onefile taskit.py

integrate:
	grep -q '$(CURDIR)' ~/.zshrc || echo 'export PATH=$(CURDIR)/dist:$$PATH' >> ~/.zshrc
