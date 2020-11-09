.PHONY: main clean FORCE

main: cs102-week-one.pdf cs102-week-two.pdf cs102-week-three.pdf cs102-week-four.pdf cs102-week-five.pdf cs102-week-six.pdf cs102-week-seven.pdf cs102-week-eight.pdf cs102-week-nine.pdf cs102-week-ten.pdf cs102-week-eleven.pdf

%.pdf: FORCE
	latexmk -pdflatex='lualatex -interaction nonstopmode --shell-escape' -pdf $(patsubst %.pdf,%.tex,$@)

clean:
	latexmk -pdf -C
