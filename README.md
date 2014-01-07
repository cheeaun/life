Life
====

This is something that I've wanted to build for a long time. It's a **timeline of important events** in my life, visualized in a way my mind always imagine it. There was something called [**Lifepath.me**](http://dcurt.is/facebook-timelines-and-lifepath-me-4) but now it's gone. How about Facebook timeline? Meh.

So, this is it. Have a look at [cheeaun.github.io/life](http://cheeaun.github.io/life).

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
3. install [roots](http://roots.cx): `npm install roots -g`
4. Add your life events into `life.md`.
5. Preview your life by running `roots watch` from within the project directory.
6. When you like it, run `roots compile`.
7. `./public/index.html` is the resulting self-contained, compiled life. 
8. Commit `life.md` (not in `master` branch).
9. Use `roots deploy --gh-pages` to deploy your life to [GitHub Pages](http://pages.github.com/)
10. Update the website link in your GitHub repo description.
11. Tell the world about your Life.
12. Add your Life to the [Lives](https://github.com/cheeaun/life/wiki/Lives) page.

How to upgrade your *Life*
--------------------------

Fetch this repo and rebase your configuration on top of it.

[Learn more](https://help.github.com/articles/fork-a-repo).

For those who forked the earlier version of Life, these are the steps that I would recommend:

1. Backup your `life.md`.
2. Reset (hard) your fork to this repo's `master` branch.
3. Re-commit your `life.md`.

How to configure your *Life*
----------------------------

Edit `lifeConfig` in `app.coffee`.

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

Here's [a compilation of Lives from the people who has forked Life](https://github.com/cheeaun/life/wiki/Lives).

License
-------

[MIT](http://cheeaun.mit-license.org/)
