import { defineAlexCLineConfig } from "alex-c-line/configs";

export default defineAlexCLineConfig({
  template: {
    pullRequest: {
      category: "general",
      projectType: "repository",
    },
  },
  preCommit: {
    packageManager: "pnpm",
    steps: [
      async (stepRunner) => {
        await stepRunner`pdm run format`;
      },
      async (stepRunner) => {
        await stepRunner`pdm run lint`;
      },
    ],
  },
});
