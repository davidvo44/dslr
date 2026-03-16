# Makefile for the dslr project
.PHONY: describe histogram scatter_plot pair_plot logreg_train logreg_predict all clean run re

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

all: $(VENV)/bin/python

$(VENV)/bin/python: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	rm -rf histograms
	rm -rf datasets/db.csv
	rm -rf datasets/normalization.csv
	rm -rf pair_plots
	rm -rf scatter_plots
	rm -rf datasets/houses.csv

re : clean all

describe:
	$(PYTHON) -m describe.describe datasets/dataset_train.csv

histogram:
	$(PYTHON) -m histogram datasets/dataset_train.csv

scatter_plot:
	$(PYTHON) -m scatter_plot datasets/dataset_train.csv

pair_plot:
	$(PYTHON) -m pair_plot datasets/dataset_train.csv

logreg_train:
	$(PYTHON) -m logregTrain.logreg_train datasets/dataset_train.csv

logreg_predict:
	$(PYTHON) -m logreg_predict datasets/dataset_test.csv

stochastic_train:
	$(PYTHON) -m stochastic_train datasets/dataset_train.csv
