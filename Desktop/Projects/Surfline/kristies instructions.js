// $ means you type everything EXCEPT the $ into the terminal, everything else is fake
// output I made up


// This means you're on master branch and we have the following branches locally
$ git branch
* master
  test-branch-A
  test-branch-B
  feature-for-all-branch

// What we're going to do is put a feature on feature-for-all-branch
// Make a pull request to merge it into master
// (basically you want the feature in master)
// and then update the branches

// This assumes you already created a "feature-for-all-branch". If you didn't already
// use `git checkout -b feature-for-all-branch` to create a new one
$ git checkout feature-for-all-branch

// We're now on feature for all branch
$ git branch
  master
  test-branch-A
  test-branch-B
* feature-for-all-branch

// WRITE SOME CODE NOW AND SAVE IT

$ git add .
$ git commit -m "Adding this new great feature"

// Now we have a feature that's on "feature-for-all-branch" but not on master.
// Let's push it to github so we can open a pull request
$ git push origin feature-for-all-branch

// NOW GO TO GITHUB and click on the "Create pull request" button when this
// feature branch shows up in a yellow box

// Now go to the PR (pull request) you created, and hit "Merge"
// This means that on Github, your REMOTE, you now merged that branch into master
// That means your feature on the feature-for-all-branch is now in master ON THE REMOTE.

// Now we go back to the terminal, and update the branches that are LOCAL with the
// new code that's REMOTE.

// Switch to master branch
$ git checkout master

// Pull in the new changes from Github on the master branch
$ git pull --rebase origin master

// Cool, now your master is updated. Let's go to the other branches and update them

// Rebase all of the changes on test-branch-A so that they are ON TOP of the 
// changes that Github master has
$ git checkout test-branch-A
$ git pull --rebase origin master

// Now, only test-branch-B is the one that doesn't have the feature for all
// Let's update that here

// Rebase all of the changes on test-branch-B so that they are ON TOP of the 
// changes that Github master has
$ git checkout test-branch-B
$ git pull --rebase origin master

// OK - now EVERY BRANCH has the feature for all.

// Let's delete the "feature-for-all-branch" since we merged it into master on github
// and it's no longer useful

$ git branch -D feature-for-all-branch

// We're done, we just made a new feature on a branch, made a pull request for that branch
// and then merged it into master. Then we updated all of our branches here to be updated
// with the latest version of master on Github. That means that the test branches we had
// pulled in the latest changes, and they now have THEIR changes plus the changes that
// went into master