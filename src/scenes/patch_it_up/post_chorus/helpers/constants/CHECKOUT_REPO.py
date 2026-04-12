from typing import Final

CHECKOUT_REPO: Final[list[str]] = [
    r"""> Run Checkout repo
                
Syncing repository: alextheman231/patch-it-up
Getting Git version info
  Working directory is '/home/runner/work/patch-it-up/patch-it-up'
  /usr/bin/git version
  git version 2.53.0""",
    r"""Temporarily overriding HOME='/home/runner/work/_temp/7d627cb9-8dca-48d7-90f9-c5248120845c' before making global git config changes
Adding repository directory to the temporary git global config as a safe directory
/usr/bin/git config --global --add safe.directory /home/runner/work/patch-it-up/patch-it-up
Deleting the contents of '/home/runner/work/patch-it-up/patch-it-up'""",
    r"""Initializing the repository
  /usr/bin/git init /home/runner/work/patch-it-up/patch-it-up
  hint: Using 'master' as the name for the initial branch. This default branch name
  hint: will change to "main" in Git 3.0. To configure the initial branch name
  hint: to use in all of your new repositories, which will suppress this warning,
  hint: call:
  hint:
  hint:     git config --global init.defaultBranch <name>
  hint:
  hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
  hint: 'development'. The just-created branch can be renamed via this command:
  hint:
  hint:     git branch -m <name>
  hint:
  hint: Disable this message with "git config set advice.defaultBranchName false"
  Initialized empty Git repository in /home/runner/work/patch-it-up/patch-it-up/.git/
  /usr/bin/git remote add origin https://github.com/alextheman231/patch-it-up""",
    r"""Disabling automatic garbage collection
  /usr/bin/git config --local gc.auto 0""",
    r"""Setting up auth
  Removing SSH command configuration
  /usr/bin/git config --local --name-only --get-regexp core\.sshCommand
  /usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand'
    && git config --local --unset-all 'core.sshCommand' || :"
  Removing HTTP extra header
  /usr/bin/git config --local --name-only --get-regexp http\\.https\:\/\/github\.com\/\.extraheader
  /usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only
    --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader'
    && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
  Removing includeIf entries pointing to credentials config files
  /usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
  /usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
  /usr/bin/git config --file /home/runner/work/_temp/git-credentials-5b294b3b-5768-4a4e-a4c4-621ad9751d56.config
  http.https://github.com/.extraheader AUTHORIZATION: basic ***
  /usr/bin/git config --local includeIf.gitdir:/home/runner/work/patch-it-up/patch-it-up/.git.path /home/runner/work/_temp/git-credentials-5b294b3b-5768-4a4e-a4c4-621ad9751d56.config
  /usr/bin/git config --local includeIf.gitdir:/home/runner/work/patch-it-up/patch-it-up/.git/worktrees/*.path /home/runner/work/_temp/git-credentials-5b294b3b-5768-4a4e-a4c4-621ad9751d56.config
  /usr/bin/git config --local includeIf.gitdir:/github/workspace/.git.path /github/runner_temp/git-credentials-5b294b3b-5768-4a4e-a4c4-621ad9751d56.config
  /usr/bin/git config --local includeIf.gitdir:/github/workspace/.git/worktrees/*.path /github/runner_temp/git-credentials-5b294b3b-5768-4a4e-a4c4-621ad9751d56.config""",
    r"""Fetching the repository
  /usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1
  From https://github.com/alextheman231/patch-it-up
   * [new ref]         eef22957302a33d9a5d74691eea9775d2c826837 -> origin/main
  /usr/bin/git branch --list --remote origin/main
    origin/main
  /usr/bin/git rev-parse refs/remotes/origin/main
  eef22957302a33d9a5d74691eea9775d2c826837
Determining the checkout info
/usr/bin/git sparse-checkout disable
/usr/bin/git config --local --unset-all extensions.worktreeConfig
Checking out the ref
  /usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
  Switched to a new branch 'main'
  branch 'main' set up to track 'origin/main'.
/usr/bin/git log -1 --format=%H
eef22957302a33d9a5d74691eea9775d2c826837
""",
]
