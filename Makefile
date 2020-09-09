.PHONY: main clean FORCE

main: cs102-week-one.pdf cs102-week-two.pdf

%.pdf: FORCE
	latexmk -pdflatex='lualatex -interaction nonstopmode --shell-escape' -pdf $(patsubst %.pdf,%.tex,$@)

clean:
	latexmk -pdf -C
