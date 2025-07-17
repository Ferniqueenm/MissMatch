all: decoder copy-final

PDK_ROOT ?= ~/.ciel
PDK ?= ihp-sg13g2

RUN_TAG = $(shell ls runs/ -1 | tail -n 1)
TOP = decoder

decoder:
	PDK_ROOT=$(PDK_ROOT) PDK=$(PDK) librelane config.yaml --manual-pdk
.phony: decoder

copy-final:
	rm -rf final/
	cp -r runs/${RUN_TAG}/final final/
.phony: copy-final

view:
	PDK_ROOT=$(PDK_ROOT) PDK=$(PDK) librelane config.yaml --manual-pdk --last-run --flow OpenInOpenROAD
.phony: view
