from typing import Final

SETUP_PACKAGE: Final[list[str]] = [
    r"""> Run Setup package
                
pnpm install
Lockfile is up to date, resolution step is skipped
Packages: +615
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""",
    r"""Progress: resolved 615, reused 613, downloaded 2, added 615, done
node_modules/.pnpm/esbuild@0.27.4/node_modules/esbuild: Running postinstall script, done in 819ms
node_modules/.pnpm/canvas@3.2.1/node_modules/canvas: Running install script, done in 655ms

dependencies:
+ dotenv 17.3.1
+ execa 9.6.1
+ zod 4.3.6

devDependencies:
+ @alextheman/github-actions 5.10.1
+ @types/node 25.5.0
+ alex-c-line 2.2.3
+ cross-env 10.1.0
+ dotenv-cli 11.0.0
+ eslint 10.0.3
+ globals 17.4.0
+ husky 9.1.7
+ jsdom 28.1.0
+ prettier 3.8.1
+ tempy 3.2.0
+ tsdown 0.21.2
+ tsx 4.21.0
+ typedoc 0.28.17
+ typescript 5.9.3
+ vite-tsconfig-paths 6.1.1
+ vitest 4.1.0

Done in 8.5s using pnpm v10.32.1
""",
]
