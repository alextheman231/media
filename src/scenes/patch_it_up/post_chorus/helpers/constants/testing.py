from typing import Final

TESTING: Final[list[str]] = [
    r"""> Run pnpm test

> @alextheman/github-actions@2.2.3 test /home/runner/work/github-actions/github-actions
> vitest run
""",
    r"""
 RUN  v4.0.18 /home/runner/work/github-actions/github-actions

 ✓ tests/rules/no-isolated-tests.test.ts (5 tests) 52ms
 ✓ tests/rules/no-namespace-imports.test.ts (6 tests) 82ms
 ✓ tests/rules/use-normalized-imports.test.ts (9 tests) 101ms
 ✓ tests/rules/use-object-shorthand.test.ts (6 tests) 102ms
 ✓ tests/rules/no-relative-imports.test.ts (9 tests) 117ms
 ✓ tests/rules/consistent-test-function.test.ts (13 tests) 136ms
 ✓ tests/utility/flattenConfigs.test.ts (5 tests) 5ms
 ✓ tests/utility/fixOnCondition.test.ts (2 tests) 3ms
 ✓ tests/utility/combineRestrictedImports.test.ts (4 tests) 2ms
 ✓ tests/rules/has-standards.test.ts (2 tests) 36ms
 ✓ tests/rules/standardise-error-messages.test.ts (6 tests) 36ms
 ✓ tests/rules/no-skipped-test.test.ts (4 tests) 38ms
 ↓ tests/end-to-end/entrypoints.test.ts (3 tests)
 ✓ tests/rules/no-plugin-configs-access-from-src-configs.test.ts (4 tests) 548ms
       ✓ function myConfig(plugin: AlexPlugin) {
    return createBaseConfig(plugin);
}

export default myConfig;  532ms

 Test Files  13 passed | 1 skipped (14)
      Tests  75 passed (78)
   Start at  02:15:43
   Duration  1.63s (transform 709ms, setup 0ms, import 4.49s, tests 1.26s, environment 1ms)
""",
]
