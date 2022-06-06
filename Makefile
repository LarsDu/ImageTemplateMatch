SHELL=/bin/bash

.PHONY install
install:
	conda env create --force -f environment.yml
