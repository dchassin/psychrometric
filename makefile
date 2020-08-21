
all: docs install

install:
	@(cd source; python3 setup.py install -q)

docs: docs/Psychrometric.md

docs/Psychrometric.md: source/psychrometric.py makefile
	@echo "~~~" > $@ ; (cd source ; python3 -c "import psychrometric; help('psychrometric')") >> $@ ; echo "~~~" >> $@