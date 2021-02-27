#!/usr/bin/env python
# coding: utf-8

import sys
import xmlplain


HELP_MESSAGE = """
Usage:
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python {0} /path/to/file.xml /path/to/file.y[a]ml
"""


if len(sys.argv) != 3:
    sys.stderr.write(HELP_MESSAGE.format(sys.argv[0]))
    sys.exit(0)

source_file = sys.argv[1]
dest_file = sys.argv[2]

# Read to plain object
with open(source_file) as inf:
    root = xmlplain.xml_to_obj(inf, strip_space=True, fold_dict=True)

# Output plain YAML
with open(dest_file, "w") as outf:
    xmlplain.obj_to_yaml(root, outf)
