#!/bin/bash

# macos
if [[ "$OSTYPE" == "darwin"* ]]; then
python -m nuitka --module reflex_test --include-package=reflex_test

# windows
elif [[ "$OSTYPE" == "msys" ]]; then
python -m nuitka --module reflex_test --include-package=reflex_test

elif [[ "$OSTYPE" == "cygwin" ]]; then
python -m nuitka --module reflex_test --include-package=reflex_test

fi