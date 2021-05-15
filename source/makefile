DOCFILES = $(shell ls *.py | sed 's/.py/.html/')
DOC_DIR = ../docs/docstrings

FORCE:

docs: $(DOCFILES)

%.html: %.py
	pydoc3 -w ./$<
	mv *.html $(DOC_DIR)