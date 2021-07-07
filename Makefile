PYTHON       = /usr/bin/env python3
.DEFAULT_GOAL = help

#help: List available tasks on this project
help:
	@grep -E '^#[a-zA-Z\.\-]+:.*$$' $(MAKEFILE_LIST) | tr -d '#' | awk 'BEGIN {FS = ": "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


#clean: Remove old build artifacts and installed packages
clean:
	${PYTHON} -m pip uninstall -y -r requirements.txt

#install: Install application along with required development packages
install:
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install -r requirements.txt
	${PYTHON} -m pip install .

run:
    echo "Running queries"
    ${PYTHON} main.py

publish:
    echo "not implemented"
