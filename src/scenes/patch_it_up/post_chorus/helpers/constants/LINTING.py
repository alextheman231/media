from typing import Final

LINTING: Final[list[str]] = [
    r"""> Run pnpm run lint

> github-actions@2.2.3 lint /home/runner/work/github-actions/github-actions
> pnpm run lint-package-json && pnpm run lint-zizmor && pnpm run lint-prettier


> github-actions@2.2.3 lint-package-json /home/runner/work/github-actions/github-actions
> eslint package.json
""",
    r"""
> github-actions@2.2.3 lint-zizmor /home/runner/work/github-actions/github-actions
> zizmor .

 zizmor v1.23.1
 INFO audit: zizmor:  completed ./.github/actions/commit-changes/action.yml
 INFO audit: zizmor:  completed ./.github/workflows/_ci.yml
 INFO audit: zizmor:  completed ./.github/workflows/_comment-outdated.yml
 INFO audit: zizmor:  completed ./.github/workflows/_commit-version-change.yml
 INFO audit: zizmor:  completed ./.github/workflows/_create-github-release.yml
 INFO audit: zizmor:  completed ./.github/workflows/_create-pull-request-templates.yml
 INFO audit: zizmor:  completed ./.github/workflows/_restrict-alex-up-bot-branches.yml
 INFO audit: zizmor:  completed ./.github/workflows/_update-dependencies.yml
 INFO audit: zizmor:  completed ./.github/workflows/actions-ci.yml
 INFO audit: zizmor:  completed ./.github/workflows/comment-outdated.yml
 INFO audit: zizmor:  completed ./.github/workflows/commit-version-change.yml
 INFO audit: zizmor:  completed ./.github/workflows/create-feature-docs.yml
 INFO audit: zizmor:  completed ./.github/workflows/create-github-release.yml
 INFO audit: zizmor:  completed ./.github/workflows/create-pull-request-templates.yml
 INFO audit: zizmor:  completed ./.github/workflows/npm-registry-publish.yml
 INFO audit: zizmor:  completed ./.github/workflows/package-ci.yml
 INFO audit: zizmor:  completed ./.github/workflows/restrict-alex-up-bot-branches.yml
 INFO audit: zizmor:  completed ./.github/workflows/update-dependencies.yml
 INFO audit: zizmor:  completed ./.github/workflows/version-change-ci.yml
No findings to report. Good job! (58 suppressed)

> github-actions@2.2.3 lint-prettier /home/runner/work/github-actions/github-actions
> prettier --check "./**/*.yml"

Checking formatting...
All matched files use Prettier code style!
""",
]
