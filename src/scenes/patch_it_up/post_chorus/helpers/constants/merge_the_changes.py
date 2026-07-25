from typing import Final

MERGE_THE_CHANGES: Final[list[str]] = [
    r"""> Run Merge the changes

remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (1/1), 944 bytes | 944.00 KiB/s, done.
From https://github.com/alextheman231/github-actions
 * branch            main       -> FETCH_HEAD
   581c9cb..2212a84  main       -> origin/main
""",
    r"""
From https://github.com/alextheman231/github-actions
 * branch            main       -> FETCH_HEAD
Updating 7a77998..2212a84
Fast-forward
Switched to branch 'main'
""",
    r"""
From https://github.com/alextheman231/github-actions
 * branch            main       -> FETCH_HEAD
Updating 581c9cb..2212a84
Fast-forward
 alex-c-line/scripts/release.yml    | 27 +++++++++++++++++++++++++++
 docs/releases/v2/v2.2/v2.2.3.md    | 23 +++++++++++++++++++++++
 package.json                       |  1 +
 3 files changed, 51 insertions(+)
 create mode 100644 alex-c-line/scripts/release.yml
 create mode 100644 docs/releases/v2/v2.2/v2.2.3.md
 """,
    r"""
From https://github.com/alextheman231/github-actions
 - [deleted]         (none)     -> origin/release-note-check-animation
Deleted branch release-note-check-animation (was 2212a84).
""",
]
