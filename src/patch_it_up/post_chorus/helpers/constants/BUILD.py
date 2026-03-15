from typing import Final

BUILD: Final[list[str]] = [
    r"""> Run pnpm run build

> @alextheman/github-actions@2.2.3 build
> tsdown""",
    r"""
ℹ entry: src/index.ts
ℹ target: node22.0.0
ℹ tsconfig: tsconfig.json
ℹ Build start
ℹ Cleaning 6 files
ℹ [CJS] dist/index.cjs      21.32 kB │ gzip:  7.07 kB
ℹ [CJS] dist/index.cjs.map  84.02 kB │ gzip: 18.84 kB
ℹ [CJS] 2 files, total: 105.33 kB
ℹ [CJS] dist/index.d.cts  21.82 kB │ gzip: 4.53 kB
ℹ [CJS] 1 files, total: 21.82 kB
✔ Build complete in 1781ms""",
    r"""
ℹ [ESM] dist/index.js      17.93 kB │ gzip:  6.46 kB
ℹ [ESM] dist/index.js.map  80.25 kB │ gzip: 18.25 kB
ℹ [ESM] dist/index.d.ts    21.82 kB │ gzip:  4.53 kB
ℹ [ESM] 3 files, total: 120.00 kB
✔ Build complete in 1785ms
""",
]
