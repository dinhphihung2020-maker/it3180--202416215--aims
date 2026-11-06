# Lab 02 – Discussion Answers

## 1. Why should we sync our feature branch with master before creating a Pull Request?

We should sync our feature branch with the latest master branch to ensure that our changes are compatible with the newest codebase.

This helps us:
- Detect and resolve merge conflicts early.
- Avoid integration problems when merging the Pull Request.
- Test our feature against the latest version of the project.

## 2. When should we avoid using rebase?

We should avoid rebasing branches that have already been shared with other developers, especially when others may have based their work on those commits.

Rebase rewrites commit history and creates new commit hashes. This can cause confusion and require other developers to synchronize their branches again.

In such cases, using merge is safer because it preserves the existing commit history.

## 3. What is the difference between feature/* and topic/* branches?

- **feature/***: Used to develop a new feature or functionality of the application, such as searching for DVDs or printing a shopping cart.
- **topic/***: Used for smaller, focused tasks related to the project, such as documentation updates, refactoring, or configuration changes.

Both types of branches are created from master and integrated through Pull Requests.

The main difference is their purpose: feature branches focus on application functionality, while topic branches focus on a specific task or change.