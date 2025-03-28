<h2>Git and Github:</h2>

<h4>Create Git Bash Account:</h4>
<p>git --version </p>
<p>git config --global user.name "name" </p>
<p>git config --global user.email "email"</p>
<p>git config --list</p>
<p>git config --global color.ui auto (set automatic command line coloring for Git for easy reviewing)</p>
<p>cd folderName/</p>
<p>cd .. (to move outside of a folder)</p>
<p>pwd (current working directory)</p>
<p>ls (list files)</p>
<p>clear</p>

<h4>Git Commands:</h4>
<p>git clone url</p>
<p>git status</p>
<p>git add .</p>
<p>git commit -m "message"</p>
<p>git push origin main</p>

<h4>Commit History:</h4>
<p>git log (check all commits history)</p>
<p>git log -p file</p>
<p>git checkout (to copy/load the code of current file with last commit in editor) </p>
<p>git checkout -f to match all files code</p>

<h4>Local Changes:</h4>
<p>git init (to create a new local repository)</p>
<p>mkdir name (create new directory)</p>
<p>git remote add origin url</p>
<p>git remote -v (verify remote)</p>
<p>git pull origin main</p>

<h4>Branching:</h4>
<p>git branch (list and check current branch)</p>
<p>git branch -M name (rename branch)</p>
<p>git branch name (create new branch)</p>
<p>git checkout name(switch to another branch)</p>
<p>git merge name(merge specific branch with current)</p>
<p>git checkout -b newBranchName (create new branch and switch to it)</p>
<p>git branch -d name (delete branch)</p>
<p>git diff branchName (compare)</p>
<p>git log branchB..branchA (show the commits on branchA that are not on branchB)</p>
<p>git diff branchB...branchA (show the diff of what is in branchA that is not in branchB) </p>

<h4>Reset changes:</h4>
<p>git reset filename (reset added files)</p>
<p>git reset</p>
<p>git reset Head~1 (reset by 1 commit)</p>
<p>git reset commitHash (reset by commits , in GitHub)/p>
<p>git reset --hard commitHash (reset by commits , in vsCode)/p>
