Life
====

This is something that I've wanted to build for a long time. It's a **timeline of important events** in my life, visualized in a way my mind always imagine it. There was something called [**Lifepath.me**](http://dcurt.is/facebook-timelines-and-lifepath-me-4) but now it's gone. How about Facebook timeline? Meh.

So, this is it. Have a look at [cheeaun.life](http://cheeaun.life/).

Features
--------

- Super simple
- No fancy formatting
- No fancy setup
- No fancy effects
- Flexible datetimes because sometimes you don't remember the exact date of an event

How to contribute
-----------------

1. Fork this project.
2. Write code.
3. Make pull requests.

How to setup your own *Life*
----------------------------

1. Fork this project.
2. `git checkout -b gh-pages` (or any branch name you like)
3. Make a copy of `life.example.md`, rename it to `life.md`.
4. Add your life events into `life.md`.
5. Preview it on a local server. Use [`python -m http.server`](https://docs.python.org/3/library/http.server.html) or [`http-server`](https://github.com/nodeapps/http-server).
6. Commit `life.md` (not in `master` branch).
7. `git push origin gh-pages -f` and publish to [GitHub Pages](http://pages.github.com/).
8. Update the website link in your GitHub repo description.
9. Tell the world about your Life.
10. Add your Life to the [Lives](https://github.com/cheeaun/life/wiki/Lives) page.

How to upgrade your *Life*
--------------------------

1. `git checkout master`
2. `git remote add cheeaun https://github.com/cheeaun/life.git`
3. `git fetch cheeaun` and `git merge cheeaun/master` to upgrade to latest Life.
4. `git checkout gh-pages` and `git merge master` to sync changes back to GitHub Pages.

[Learn more](https://help.github.com/articles/fork-a-repo).

For those who forked the earlier version of Life, these are the steps that I would recommend (requires some Git-fu):

1. Backup your `life.md`.
2. Reset (hard) your fork to this repo's `master` branch.
3. Clean up your `gh-pages`.
4. Re-commit your `life.md` there.
5. Make sure your `master` branch is untouched so that future updates work.

How to configure your *Life*
----------------------------

1. Make a copy of `config.example.json`, rename it to `config.json`.
2. Only commit it in `gh-pages` branch.

The configuration:

- `customStylesheetURL` - (*string*, default to `null`) Path to a custom stylesheet file, for those who doesn't like the default *theme*.
- `yearLength` - (*number*, default to `120`) The width of the year grids, in pixels.
- `hideAge` - (*boolean*, default to `false`) Option to hide age from year axis.

Datetime "syntax"
-----------------

- `2000` - event that happen in that year
- `01/2000` - event that happen in that month/year
- `01/01/2000` - event that happen exactly in that day/month/year
- `2001-2005`, `10/2001-02/03/2005` - event that happen within the two dates
- `~2005` - event that happen around the time in that year
- `2005-~` - event that happen from that year and beyond (now).

Other people's Lives
--------------------

Here's [a compilation of Lives from the people who have forked Life](https://github.com/cheeaun/life/wiki/Lives).

License
-------

[MIT](http://cheeaun.mit-license.org/)
