# Branching, Sub-branching, Tagging & Merging — Step-by-step guide

Purpose
- Provide a clear, actionable branching strategy and release workflow for a GitHub-hosted project.
- Include naming conventions, commands, examples for feature work, sub-branches, release tagging, hotfixes, merge strategies, and conflict resolution.
- Allow easy automation with CI and predictable releases.

Table of contents
1. Overview & Goals
2. Branching model (main, develop, feature/*, release/*, hotfix/*)
3. Sub-branches (task/topic branches)
4. Naming conventions
5. Commit message conventions
6. Feature workflow (step-by-step)
7. Sub-branch workflow (examples)
8. Release workflow and tagging (step-by-step)
9. Hotfix workflow (step-by-step)
10. Merge strategies (merge commit, squash, rebase) — when and how
11. Handling conflicts, stash, and unrelated histories
12. PR checklist & branch protection
13. CI triggers & automation ideas
14. Useful commands and examples
15. Best practices & maintenance

---

1. Overview & Goals
- Keep `main` as the production-ready branch.
- Use `develop` (optional) for integration of features before release.
- Isolate work in short-lived feature branches; allow sub-branches for large features or tasks.
- Use tags for release points (annotated tags + semantic versions).
- Enforce code quality via PRs, CI, and protected branches.

2. Branching model
- main
  - Always deployable; only merged to after a PR that passes CI and reviews.
- develop (optional)
  - Integration branch for features; used if you prefer a two-branch flow.
- feature/<name>
  - Feature branches created from develop (or main if no develop).
- feature/<name>/task-<n> or feature/<name>/subtask
  - Sub-branches for complex feature work (see section 3).
- release/vX.Y.Z
  - Branches for release candidate stabilization and version bumps.
- hotfix/vX.Y.Z
  - Branches off main to patch urgent issues.

3. Sub-branches (topic/task branches)
- When a feature is large, create a top-level feature branch, then create sub-branches for parallel tasks:
  - feature/auth
    - feature/auth/login-form
    - feature/auth/oauth-integration
- Advantages:
  - Parallelize work safely.
  - Keep each PR small and reviewable.
- Merge sub-branches back into the top-level feature branch before merging the feature to develop/main.

4. Naming conventions
- Branches:
  - feature/<short-description> (e.g., feature/user-profile)
  - bugfix/<short-description> or fix/<short> (e.g., fix/date-parsing)
  - hotfix/vX.Y.Z (e.g., hotfix/v1.2.1)
  - release/vX.Y.Z (e.g., release/v1.3.0)
  - chore/<task> (e.g., chore/deps-update)
  - docs/<topic> (e.g., docs/README-updates)
- Tags:
  - vMAJOR.MINOR.PATCH (e.g., v1.2.0)
  - pre-release: v1.3.0-rc.1, v1.3.0-beta.1

5. Commit message conventions
- Use Conventional Commits for automated changelogs:
  - feat: add new API endpoint
  - fix: correct timezone handling
  - chore: bump dependencies
  - docs: update README
- Keep messages short, descriptive; include issue/PR references when relevant.

6. Feature workflow (step-by-step)
1. Update local main/develop:
   - git checkout develop        # or main
   - git pull origin develop     # or origin main
2. Create the feature branch:
   - git checkout -b feature/your-feature
3. Work locally, commit frequently:
   - git add .
   - git commit -m "feat: add X (small description)"
4. Push branch and open PR:
   - git push -u origin feature/your-feature
   - Open PR targeting develop (or main). Include description, testing notes.
5. Code review & CI:
   - Wait for CI to pass and at least one reviewer approval (per CONTRIBUTING rules).
6. Merge:
   - Merge according to policy (squash, merge commit, or rebase — see section 10).
   - Delete feature branch locally and remotely:
     - git branch -d feature/your-feature
     - git push origin --delete feature/your-feature

7. Sub-branch workflow (example)
- Suppose feature/large-work needs subtask branches:
  1. Create top-level:
     - git checkout -b feature/large-work
     - git push -u origin feature/large-work
  2. Create sub-branch from top-level:
     - git checkout -b feature/large-work/task-1
  3. Work, commit, push:
     - git push -u origin feature/large-work/task-1
  4. Open PR from feature/large-work/task-1 into feature/large-work
     - Use PR checks; merge subtask into top-level using merge commit or squash.
  5. After all subtasks merged into feature/large-work, open PR from feature/large-work into develop.

8. Release workflow & tagging (step-by-step)
- Use semantic versioning (MAJOR.MINOR.PATCH).
- Typical release flow (using develop):
  1. Prepare release branch from develop:
     - git checkout develop
     - git pull origin develop
     - git checkout -b release/v1.2.0
  2. Update version, CHANGELOG, run tests, fix any last-minute bugs.
  3. Commit changes:
     - git add .
     - git commit -m "chore(release): prepare v1.2.0"
  4. Merge release into main and develop:
     - git checkout main
     - git pull origin main
     - git merge --no-ff release/v1.2.0 -m "chore(release): merge release v1.2.0"
     - git push origin main
     - git checkout develop
     - git merge --no-ff release/v1.2.0 -m "chore(release): back-merge release v1.2.0 into develop"
     - git push origin develop
  5. Tag the release (annotated tag recommended):
     - git checkout main
     - git tag -a v1.2.0 -m "Release v1.2.0 — summary of changes"
     - git push origin v1.2.0
  6. Create GitHub Release:
     - Use the Releases UI or CLI:
       - gh release create v1.2.0 --title "v1.2.0" --notes-file CHANGELOG.md

Notes:
- If you don't use develop, create release branch from main.
- Use annotated tags (`git tag -a ...`) — they store author/date/message.

9. Hotfix workflow (step-by-step)
1. Create hotfix from main:
   - git checkout main
   - git pull origin main
   - git checkout -b hotfix/v1.2.1
2. Apply fix, update tests, bump version:
   - git add .
   - git commit -m "fix: critical bug in X"
3. Merge hotfix into main and develop:
   - git checkout main
   - git merge --no-ff hotfix/v1.2.1 -m "chore(hotfix): v1.2.1"
   - git push origin main
   - git checkout develop
   - git merge --no-ff hotfix/v1.2.1 -m "chore(hotfix): back-merge v1.2.1"
   - git push origin develop
4. Tag and release:
   - git tag -a v1.2.1 -m "Hotfix v1.2.1"
   - git push origin v1.2.1

10. Merge strategies — pros/cons and commands
- Merge commit (default merge):
  - Command (locally): git merge --no-ff feature/x
  - Pros: preserves full history, easy to see where branches merged.
  - Cons: more commits in history.
- Squash merge:
  - Command (locally): git merge --squash feature/x; git commit -m "feat: summary"
  - Or use GitHub "Squash and merge" button.
  - Pros: keeps history linear and concise (one commit per feature).
  - Cons: loses per-commit details unless included in commit message.
- Rebase (interactive):
  - Command: git checkout feature/x; git rebase -i develop
  - Pros: creates a linear history, useful before merging a small feature.
  - Cons: rewriting history is problematic for shared branches; avoid rebasing public branches.
- Recommended policy:
  - Use PR/Squash for small features to keep main clean.
  - Use merge commits for larger features needing history context.
  - Use rebase locally to tidy up before opening PR (only rewrites your local branch).

11. Handling conflicts, stash, and unrelated histories
- Conflicts during merge:
  1. Git will stop and mark conflicts in files.
  2. Open files, resolve conflicts (remove <<<<>>> markers).
  3. git add <resolved-files>
  4. git commit (complete the merge)
- Stash local changes temporarily:
  - git stash save "WIP: reason"
  - git stash list
  - git stash pop  # reapply latest stash (may cause conflicts)
- Unrelated histories when pulling remote with initial commit:
  - git pull origin main --allow-unrelated-histories
  - If local changes would be overwritten, first commit or stash them:
    - git add .
    - git commit -m "WIP: commit before merging unrelated histories"
    - git pull origin main --allow-unrelated-histories
- Force pushing (dangerous) — only when intentionally overwriting remote:
  - git push --force origin main
  - Avoid for shared/public repos.

12. PR checklist & branch protection
- PR checklist (place in CONTRIBUTING.md):
  - All tests pass in CI.
  - Linting and formatting checks passed.
  - At least one reviewer approved.
  - Changelog updated if needed.
  - Version bumped (if applicable).
- Protect `main` (and `develop`) on GitHub:
  - Require PR reviews before merge.
  - Require status checks (CI) to pass.
  - Require signed commits (optional).
  - Restrict force pushes and deletion.

13. CI triggers & automation ideas
- CI for PRs and branch pushes:
  - on: pull_request (target: main or develop)
  - on: push (branches: [main, develop, 'release/*'])
- Release automation:
  - Trigger on tag push: on: push: tags: ['v*.*.*']
  - Use an action to build artifacts and create a GitHub Release.
  - Use semantic-release or release-drafter to automate version selection and release notes from Conventional Commits.
- Example GitHub Actions triggers:
  - PR validation: runs on pull_request
  - Release publishing: runs on push tags

14. Useful commands and examples

Initial repo setup (local → remote)
- git init
- git add .
- git commit -m "chore: initial commit"
- git branch -M main
- git remote add origin https://github.com/USER/REPO.git
- git push -u origin main

Create feature, push, open PR
- git checkout -b feature/awesome
- ...work...
- git add .
- git commit -m "feat: add awesome feature"
- git push -u origin feature/awesome

Merge feature into develop (locally)
- git checkout develop
- git pull origin develop
- git merge --no-ff feature/awesome -m "chore: merge feature/awesome"
- git push origin develop

Tagging and pushing tag
- git tag -a v1.2.3 -m "Release v1.2.3"
- git push origin v1.2.3
- or push all tags:
  - git push origin --tags

List, show, delete tags
- git tag --list
- git show v1.2.3
- git tag -d v1.2.3             # delete local tag
- git push --delete origin v1.2.3  # delete remote tag

Rebase small feature onto develop (locally, before PR)
- git checkout feature/foo
- git fetch origin
- git rebase origin/develop
- # fix conflicts if any, then:
- git push --force-with-lease origin feature/foo  # safe-ish force

Resolve merge conflicts
- git status   # find conflicted files
- edit files and remove conflict markers
- git add <file>
- git commit   # complete merge commit
- git push

Stash and pop
- git stash push -m "WIP: X"
- git pull origin main
- git stash pop

15. Best practices & maintenance
- Keep branches short-lived (days to a few weeks).
- Prefer small PRs with focused changes.
- Automate checks in CI: lint, unit tests, security scanning.
- Use conventional commit messages to enable automated changelogs.
- Use annotated tags and sign tags when releases must be verifiable.
- Protect main and enforce required CI checks and review counts.
- Document the release policy in CONTRIBUTING.md (who can create releases, how versions increment).
- Regularly prune stale branches:
  - git remote prune origin
  - Delete merged branches on GitHub and locally.

Appendix — Example common flows

A) Small feature directly to main (no develop)
- git checkout main
- git pull origin main
- git checkout -b feature/short-fix
- work → git commit
- git push -u origin feature/short-fix
- Open PR → review → squash-and-merge into main
- git checkout main
- git pull origin main
- git tag -a vMAJOR.MINOR.PATCH -m "Release X"
- git push origin vMAJOR.MINOR.PATCH

B) Release candidate workflow
- After all changes merged into develop:
- git checkout -b release/v2.0.0 develop
- run tests, bump version, update CHANGELOG
- git commit -m "chore(release): prepare v2.0.0"
- open PR into main (or merge locally to main)
- merge → tag → create GitHub Release

---

Contributing snippet (important rules)
```markdown
- Create a PR for any non-trivial change. At least one reviewer should approve before merging.
- Run tests and linters in CI before merging.
```

Changelog automation ideas
- Use tools like conventional-changelog, auto-changelog, or semantic-release to generate CHANGELOG.md from commits automatically.
- Maintain a human-reviewed CHANGELOG.md for important notes; auto-generated changelogs for convenience.

Security and access control
- Use GitHub Teams & Roles to control who can merge or create releases.
- Use Dependabot or scheduled dependency checks.
- Consider signing tags with GPG for high-assurance releases.

---

Where to record this in the repo
- Add this file as `BRANCHING_AND_RELEASES.md` at repo root.
- Add a short “Release Policy” section in `CONTRIBUTING.md`.
- Keep `CHANGELOG.md` updated (automate where possible).

Quick reference — useful commands (condensed)
- New branch: git checkout -b feature/x
- Push branch: git push -u origin feature/x
- Merge locally: git merge --no-ff feature/x
- Squash locally: git merge --squash feature/x; git commit -m "..."
- Tag: git tag -a v1.2.3 -m "Release v1.2.3"; git push origin v1.2.3
- Delete remote branch: git push origin --delete feature/x
- Stash: git stash push -m "WIP"
- Force push (careful): git push --force-with-lease origin feature/x

---

This document is intended to be copy-pasted into your repository as a reference and adapted to your team’s preferences. Keep it near CONTRIBUTING.md and README for discoverability.