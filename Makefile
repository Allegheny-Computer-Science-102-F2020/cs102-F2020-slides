.PHONY: main clean FORCE

main: cs102-week-one.pdf cs102-week-two.pdf cs102-week-three.pdf cs102-week-four.pdf

%.pdf: FORCE
	latexmk -pdflatex='lualatex -interaction nonstopmode --shell-escape' -pdf $(patsubst %.pdf,%.tex,$@)

clean:
	latexmk -pdf -C
