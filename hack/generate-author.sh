#!/usr/bin/env bash

set -e

set -x

cat > "../AUTHORS" <<- EOF
	# This file lists all contributors to the repository.
	# See hack/generate-authors.sh to make modifications.

	$(git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
