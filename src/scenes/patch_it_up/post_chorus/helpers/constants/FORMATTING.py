from typing import Final

FORMATTING: Final[list[str]] = [
    r"""> Run pnpm run format

> github-actions@2.2.3 format /home/runner/work/github-actions/github-actions
> pnpm run format-package-json && pnpm run format-prettier
""",
    r"""
> github-actions@2.2.3 format-package-json /home/runner/work/github-actions/github-actions
> eslint --fix --suppress-all package.json && rm -f eslint-suppressions.json
""",
    r"""
> github-actions@2.2.3 format-prettier /home/runner/work/github-actions/github-actions
> prettier --write "./**/*.yml"

.github/actions/commit-changes/action.yml 16ms (unchanged)
.github/workflows/_ci.yml 4ms (unchanged)
.github/workflows/_comment-outdated.yml 1ms (unchanged)
.github/workflows/_commit-version-change.yml 2ms (unchanged)
.github/workflows/_create-github-release.yml 1ms (unchanged)
.github/workflows/_create-pull-request-templates.yml 1ms (unchanged)
.github/workflows/_restrict-alex-up-bot-branches.yml 1ms (unchanged)
.github/workflows/_update-dependencies.yml 1ms (unchanged)
.github/workflows/actions-ci.yml 1ms (unchanged)
.github/workflows/comment-outdated.yml 6ms (unchanged)
.github/workflows/commit-version-change.yml 9ms (unchanged)
.github/workflows/create-feature-docs.yml 2ms (unchanged)
.github/workflows/create-github-release.yml 2ms (unchanged)
.github/workflows/create-pull-request-templates.yml 2ms (unchanged)
.github/workflows/npm-registry-publish.yml 2ms (unchanged)
.github/workflows/package-ci.yml 2ms (unchanged)
.github/workflows/restrict-alex-up-bot-branches.yml 1ms (unchanged)
.github/workflows/update-dependencies.yml 3ms (unchanged)
.github/workflows/version-change-ci.yml 1ms (unchanged)
zizmor.yml 0ms (unchanged)
""",
]
