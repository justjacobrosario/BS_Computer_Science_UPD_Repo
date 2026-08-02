## 1. Version Control Systems (VCSs)

: a VCS is a system that records changes to a file or set of files to save, revert, and recover specific versions of the file/s.

### 1.1. Centralized Version Control Systems

: Every version and the complete history of revisions (version database) of a file/s is centralized to a specific server. 

: However, corruption or complete termination of the server risks the version database to be completely deleted.


### 1.2. Distributed Version Control Systems

: Instead of only centralizing to one place, the version database is saved to a certain server, and then mirrors it to each computer connected to the server. (e.g. Git)

: By database mirroring, complete deletion of the version control is mitigated by giving copies to every connected computer.


## 2. How Git Works

### 2.1. How most VCS works

: they are **delta-based version control systems**
(i.e. for every version, only the changes of each file is stored)

### 2.2. How Git works...

: Git takes **snapshots** or version of every file for every commit or saved state (if a file is not changed, Git just links to the previous identical file)

: Suppose files A, B, and C, such that we have changed file A. When saved a state in Git, that version stores every latest version of the file, such that it stores the new version of A, and just links the previous identical files B and C.

### 2.3. Git mostly works locally (fast and reliable even offline)

: Git can browse the history of the project locally, making it fast (unlike any other VCS that has latency due to their dependence to other computer networks).

### 2.4. Git has Integrity

: Files within a certain directory cannot be added, changed, or deleted without Git knowing.

: **Checksumming** is the process of converting file contents and other directory objects into hexadecimal string using a cryptographic hashing function. (i.e. it makes the data's fingerprint to let Git ALWAYS notice if something has changed)

### 2.5. Git  only accumulates data

: Git only adds versions or sections to the project history. It nearly prevents versions to be removed to prevent accidental data loss. (unlike other VCS where it is easy to remove a version, making it vulnerable for data losses)

### 2.6. The Three States in Git
: There are three states or places a file can be in Git
##### 1. Working Directory
: this is a particular version of the project (pulled from the Git Directory, later for more) that you are currently accessing to write and change files. 

##### 2. Staging Area
: it is a file that records what files are to be commited later

: when files are modified, you can **stage** or mark them to be committed later (i.e. **staged files** are files marked to be committed later)

: once you have staged all necessary files, you can now **commit** them to be saved as the new versions in your locally stored database. (i.e. **committed files** are files safely stored to the local database)

##### 3. Git Directory (aka Repository)
: this is where the project database is stored. This contains the versions and complete history of the project.

: by **pushing** (adding) the current version of the local database to the repository, all committed files will be virtually be saved to the repository for other people to see and access them.


### 2.7. The Basic Git Flow
: this will be the usual flow of version control in Git

1. You simply modify or change files in your working tree (i.e. the current version you are currently accessing and editing)
2. You stage the modified files that you want to be a part of your commit.
3. You commit, which saves the staged files to the local database 
4. You push, which stores the snapshot of the new version from the local database to the repository.

