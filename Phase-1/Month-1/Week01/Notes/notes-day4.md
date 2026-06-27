# اليوم 4 — 26/06/2026

## Phase 0 · Warm-Up - W01

## **Git and Github**

### What's Git
     It is a Distributed Version Control System. 
     It is a very powerfull tool to keep track of changes in your files
     It tracks what changed? when changed? and where changed?

### What's Github
     It's a clould server where you and your team can push their files.
     Making it easier for everyone to see, track, edit and shares the changes of your files.

### What's a Repository

     It is a place where all your versions and their entire history are stored in.

### Git Architecture: Local vs. Remote

#### How the local part works?
  - **Local** : Means the files and the changes you made are all stored in your machine.

  - The local part consists of 3 important stages:

    - 1. **Working directory** : It is the folder where are you working in your files.

    - 2. **Staged** : Means that your modified or new files have been marked and prepared to be included in your next commit snapshot

    - 3. **Commit** : Saving your staged files into your local repo.

#### When to use remote?
  - **Remote**: Means the files and the changes you made are all stored in the cloud. You push or uplod your local files on the cloud.
  - We push the files into the cloud 'Github' when we want to share it with others, access it from anywhere else and collaborate with others.

### Learning Git & Github commands
- **'git clone'** : It downloads a full copy of an existing Git repository to your local machine.

- #### Initializing a Repository locally and remotely
     - 'git init' : It initialize a new local repository and start tracking the changes of this folder.

     - To create a remote repository you go to [Github](https://github.com) them choose new repo and create it and add your files.

- 'git status' : This cmd tells you what changed, modefied and deleted from your previous snapshot in your wroking directory.

- #### 'git add' combinations

     - **'git add --all' or 'git add -A'**: It saves your changes **in the entire project** to the staging area to be ready for the next commit.

     - **' git add . '**: It saves your changes **in the current working directory and subdirectories inside it only** to the staging area to be ready for the next commit.

     - **' git add * '**: It saves all your **visible changes except for deleted files** to the staging area to be ready for the next commit.

- #### **'git commit' combinations**

     - **'git commit -m "WRITE UR MESSAGE"** : It saves the changes that was at the staging area as well as making a new commit.

- #### **'git reset' combinations**
     - **'git reset'** : It removes all the staged changes back to working directory.

     - **'git reset HEAD~'** : It rolls back to the previous version **without the deleted files** before the last commit.  

     - **'git reset --hard'** : It returns **changes and deleted files** into your working directory. Must the files not be commited.

- #### **'git rm'** combinations:
     - **'git rm file.txt'** : It removes the file from the working directory and add it to the staging area.
     - #### **This works only if the file you trying to delete has modifications**
          -  **'git rm -f file.txt'** : It **force delete** the file depsite having modifications and add it to the staging area.

          - **'git rm --cached file.txt'** :  It **only removes the file from the staging area** depsite having modifications and add it the **deleted one** to the staging area.

          - **'git rm -r <Folder>'** :  It **removes the folder and its contents** recursively and add them to the staging area   . 

- #### **'git log' combinations**

     - **'git log'** : To see full history about your commits

     - **'git log --oneline '** : To see full history about your commits. (Nicer and prettier way)

- #### *Git Branching*

     - ***What's *Git Branching****

           Git branching is the practice of creating an isolated workspace within a repository
           to develop new features, fix bugs, or experiment without affecting the main source code.

     - **'git branch < branch name >'** : To create a new branch. It makes a copy of the current working branch you are in.

     - **'git checkout < branch name >'** : It switches to "branch name".

     - **'git checkout < commit id >'** : It switches to that "commit". Files and changes of that commit will be seen.

     - **'git merge < branch name > -m "MESSAGE"'** : Adds the changes from branch-name into the current branch.

     - ***What's *Merging conflict****
             
           A merge conflict happens when different branches modify the same line in a file.
           Version control systems like Git can't automatically decide which changes to keep,
           requiring a human to manually resolve the competing edits before the merge can proceed.
                               ---------------------------------------------------------
           To fix it you need to manually edit the file to choose which changes to keep and delete
           the conflict markers.

     - **'git diff '** : It compares different states of your repository to show exactly what lines of code have been added, modified, or deleted.

- ### Fetch, Pull and Push Explained
     - **'git push origin < branch name > '** : Uploads your local repository commits to a remote repository server like GitHub.

     - **'git fetch'** : Downloads commits, files, and references from a remote repository into your local repository without merging them into your working files.

     - **'git pull'** : Downloads changes from a remote repository and immediately integrates them into your current local working branch. git pull fetches updates from a remote repository and immediately integrates them into your current local branch. It serves as a shortcut that combines two separate commands into a single step: git fetch followed by git merge.

-  **'git restore < file >'** : Discards uncommitted local changes in your **working directory** and overwrites the specified file with its last committed version.

-  **'git restore < folder >'** :  To discard uncommitted local changes and reset the **directory's contents** to your last committed state.

-  **'git restore --staged < file or folder >'** :  The git restore --staged command is used to unstage files, effectively undoing a git add before you make a commit. So there is no files need to be add to staging area.

- #### **'git stash' combinations**

     - **' git stash '** : The git stash command temporarily shelves (saves) uncommitted changes in your working directory so you can switch contexts or branches without committing half-done work. It reverts your local project files back to a clean state matching the latest HEAD commit.

     - **'git stash pop'** : It restores your most recently stashed changes to your current working directory and permanently removes them from your stash history stack.

     - **'git stash apply'** : It restores previously saved changes from your Git stash back to your current working directory without removing them from the stash list. This makes it a safer alternative to git stash pop, which deletes the stashed data immediately after applying it.

- #### **'git reset' vs 'git revert'**
      The primary difference is that git revert safely creates a new commit that records the inverse
      changes of a targeted commit, while git reset rewrites history
      by moving your current branch pointer backward to an earlier commit.

     - **'git revert < commit id > '** : It undoes changes from a specific commit by creating a brand-new commit with the inverse changes.

- **'git rebase < branch name >'** :  It is a Git utility that reapplies a sequence of commits from your current branch onto the tip of another base branch. It physically rewrites your project's commit history by replacing your original commits with brand-new ones. Developers primarily use it to keep a perfectly linear, clean project history and to stay up to date with a main branch without cluttering the log with unnecessary merge commits.