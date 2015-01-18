# radiosteuerung

A very simple web frontend to provide control for @crazycusti's daily
budgie entertainment.

## Dependencies

* [music on console](http://moc.daper.net/) audio player
* Python 3.x (should work without issues on 2.5+ too, replace the bytestrings
  with 8-bit strings)
* [bottle.py](https://github.com/bottlepy/bottle) micro web framework

## Installation
1. Install MOC and append your favorite internet radio station to its playlist.
2. Install your distribution's package for bottle.py for Python 3 (for example,
   `python3-bottle` on Ubuntu) or drop a copy of
   [the latest version](https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py)
   in the same directory.
3. Use your distribution's service manager to run radiosteuerung.py as the same
   user as MOC. A sample upstart job file is provided.
