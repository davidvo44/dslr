# Makefile for the dslr project
.PHONY: describe histogram scatter_plot pair_plot logreg_train logreg_predict

PYTHON = python3

describe:
	$(PYTHON) describe.py

histogram:
	$(PYTHON) histogram.py

scatter_plot:
	$(PYTHON) scatter_plot.py

pair_plot:
	$(PYTHON) pair_plot.py

logreg_train:
	$(PYTHON) logreg_train.py

logreg_predict:
	$(PYTHON) logreg_predict.py

clean:
	rm -rf histograms scatter_plots pair_plots