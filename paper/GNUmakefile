all:
	./bin/latexrun p.tex

clean:
	./bin/latexrun --clean-all p.tex

ASPELL_CMDS=\
	--add-tex-command="autoref p" \
	--add-tex-command='begin pp' \
	--add-tex-command='bibliography p' \
	--add-tex-command='bibliographystyle p' \
	--add-tex-command='cc p' \
	--add-tex-command='citeauthor p' \
	--add-tex-command='color p' \
	--add-tex-command='definecolor ppp' \
	--add-tex-command='eqref p' \
	--add-tex-command='fvset p' \
	--add-tex-command='hypersetup p' \
	--add-tex-command='lstset p' \
	--add-tex-command='mathit p' \
	--add-tex-command='mathrm p' \
	--add-tex-command='newcommand pp' \
	--add-tex-command='renewcommand pp' \
	--add-tex-command='usetikzlibrary p' \
	--add-tex-command='DeclareMathOperator pp' \
	--add-tex-command='VerbatimInput p' \

SPELLTEX := $(shell ./bin/get-tex-files.sh p.tex) latex.out/p.bbl
spell:
	@ for i in $(SPELLTEX); do aspell -t $(ASPELL_CMDS) -p ./aspell.words -c $$i; done
	@ for i in $(SPELLTEX); do scripts/double.pl $$i; done
	@ for i in $(SPELLTEX); do scripts/abbrv.pl  $$i; done
	@ bash scripts/hyphens.sh $(SPELLTEX)
	@ ( head -1 aspell.words ; tail -n +2 aspell.words | LC_ALL=C sort ) > aspell.words~
	@ mv aspell.words~ aspell.words
