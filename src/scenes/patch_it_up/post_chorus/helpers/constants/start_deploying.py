from typing import Final

START_DEPLOYING: Final[list[str]] = [
    r"""> Run Start deploying

pnpm publish --access public

> github-actions@2.2.4 prepare /home/runner/work/github-actions/github-actions
> husky
""",
    r"""
npm notice
npm notice github-actions@2.2.4
npm notice Tarball Contents
npm notice 1.1kB LICENSE
npm notice 4.9kB README.md
npm notice 4.6kB dist/configs/index.cjs
npm notice 6.5kB dist/configs/index.d.cts
npm notice 6.5kB dist/configs/index.d.ts
npm notice 2.7kB dist/configs/index.js
npm notice 1.5kB dist/configs/internal/index.cjs
npm notice 4.9kB dist/configs/internal/index.d.cts
npm notice 4.9kB dist/configs/internal/index.d.ts
npm notice 1.3kB dist/configs/internal/index.js
npm notice 76.6kB dist/index.cjs
npm notice 11B dist/index.d.cts
npm notice 11B dist/index.d.ts
npm notice 70.0kB dist/index.js
npm notice 5.1kB package.json
npm notice 213B templates/outdated/table.html
npm notice 109B templates/outdated/tableRow.html
npm notice 1.6kB templates/pullRequest/general/base.md
npm notice 311B templates/pullRequest/general/breaking_change.md
npm notice 272B templates/pullRequest/general/bug_fix.md
npm notice 343B templates/pullRequest/general/documentation_change.md
npm notice 404B templates/pullRequest/general/internal_change.md
npm notice 275B templates/pullRequest/general/miscellaneous.md
npm notice 275B templates/pullRequest/general/new_feature.md
npm notice 358B templates/pullRequest/general/refactor.md
npm notice 343B templates/pullRequest/general/tooling_change.md
npm notice 1.8kB templates/pullRequest/infrastructure/base.md
npm notice 277B templates/pullRequest/infrastructure/bug_fix.md
npm notice 331B templates/pullRequest/infrastructure/documentation_change.md
npm notice 705B templates/pullRequest/infrastructure/irreversible_destruction.md
npm notice 501B templates/pullRequest/infrastructure/manual_change.md
npm notice 282B templates/pullRequest/infrastructure/miscellaneous.md
npm notice 303B templates/pullRequest/infrastructure/new_feature.md
npm notice 331B templates/pullRequest/infrastructure/refactor.md
npm notice 401B templates/pullRequest/infrastructure/resource_update.md
npm notice 334B templates/pullRequest/infrastructure/tooling_change.md
npm notice 150B templates/releases/editableSection.md
npm notice 212B templates/releases/editableSectionMajor.md
npm notice 684B templates/releases/major.md
npm notice 653B templates/releases/minor.md
npm notice 612B templates/releases/patch.md
""",
    r"""
npm notice Tarball Details
npm notice name: github-actions
npm notice version: 2.2.4
npm notice filename: github-actions-2.2.4.tgz
npm notice package size: 45.9 kB
npm notice unpacked size: 202.7 kB
npm notice shasum: 76731468d3edeb987f119095fe01f7bc67d092b1
npm notice integrity: sha512-3Ay8vlxdwAhvn[...]sofbhjawkKNsQ==
npm notice total files: 41
npm notice""",
    r"""npm notice Publishing to https://registry.npmjs.org/ with tag latest and public access
npm notice publish Signed provenance statement with source and build information from GitHub Actions
npm notice publish Provenance statement published to transparency log: https://search.sigstore.dev/?logIndex=1099757115
+ github-actions@2.2.4
""",
]
