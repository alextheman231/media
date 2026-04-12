from typing import Final

FETCH_THE_DOCS: Final[list[str]] = [
    "> Run Fetch the docs",
    "",
    'VERSION=v$(jq -r ".version" package.json)',
    'NEXT_VERSION="$(alex-c-line version increment $VERSION $VERSION_TYPE)"',
    r"""
RELEASE_DOC_PATH="$(alex-c-line template release-note path $NEXT_VERSION)"
if [[ -f "$RELEASE_DOC_PATH" ]]; then
  echo "Release document found. Continuing..."
  echo "path=$RELEASE_DOC_PATH" >> $GITHUB_OUTPUT
  echo "should_change_version=true" >> $GITHUB_OUTPUT
else
  echo "No release document found. Skipping..."
  echo "should_change_version=false" >> $GITHUB_OUTPUT
fi

shell: /usr/bin/bash -e {0}
env:
  VERSION_TYPE: patch
  NEXT_VERSION: v2.2.4
""",
    "Release document found. Continuing...",
]
