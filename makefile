docs/Psychrometric.md: source/psychrometric.py makefile
	@echo "~~~" > $@ ; (cd source ; python3 -c "import psychrometric; help('psychrometric')") >> $@ ; echo "~~~" >> $@