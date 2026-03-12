# Makefile for the dslr project
.PHONY: describe histogram scatter_plot pair_plot logreg_train logreg_predict all clean run re

VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

all: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
	rm -rf histograms
	rm -rf datasets/db.csv
	rm -rf datasets/normalization.csv
	rm -rf pair_plots
	rm -rf scatter_plot

re : clean all

describe:
	$(PYTHON) -m describe.describe

histogram:
	$(PYTHON) histogram.py 

scatter_plot:
	$(PYTHON) scatter_plot.py

pair_plot:
	$(PYTHON) pair_plot.py

logreg_train:
	$(PYTHON) -m logregTrain.logreg_train

logreg_predict:
	$(PYTHON) logreg_predict.py dataset_test.csv
