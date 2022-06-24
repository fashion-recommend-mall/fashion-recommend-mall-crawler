typehint: 
	mypy ./ --ignore-missing-imports

lint: 
	pylint \
	--disable=R0801 \
	--disable=R0903 \
	--disable=C0325 \
	./src

checklist: typehint lint

.PHONY:	typehint lint checklist