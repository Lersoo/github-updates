# What's github-updates ?

Github's notifications system is pretty bad, in my opinion.

Where do developers work (most of the time) ? In their terminal. So why not display those notifications there ?

### How I plan to do it

Call Github's API, store the response _somewhere_, and compare new calls to this response to determine what's to display as a change or not.

### Which languages ?

I plan to use bash (obviously) and probably Python, Ruby or Javascript. It might be a good exercise to rewrite this program in another language in the future, though.
