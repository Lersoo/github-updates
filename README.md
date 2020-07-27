# What's github-updates ?

It's nothing yet, but it will soon be.
Github's notifications system is pretty bad in my opinion.
I just want a simple, human-readable overview of everything that happened on every repo I'm a contributor of, when I'm launching my terminal or when entering a command. Simple !

### How I plan to do it

Call Github's API, store the response _somewhere_, and compare new calls to this response to determine what's to display as a change or not.

### Which languages ?

I plan to use bash (obviously) and probably Python, Ruby or Javascript. It might be a good exercise to rewrite this program in another language in the future, though.