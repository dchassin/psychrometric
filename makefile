docs/Psychrometric.md: source/psychrometric.py makefile
	@( cd source ; python3 -c "import psychrometric; help('psychrometric')" > ../docs/Psychrometric.md )