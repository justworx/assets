
# locale data asset package demo

This is a demo of locale_data json files, that will (hopefully) allow
access to use of data from more than one locale on MS Windows (which 
doesn't natively support use of any but the one locale set in the
preferences control pannel) and on *nix systems that have trouble with
use of multiple locales in threaded apps.

NOTE: This is only a demp, but it does work as intended, and most of 
      the locale data files for utf-8 are there. The exception is the
      Galacian, Spain language pack, which I've been unable to 
      successfully install.


#### Use

It's perfectly acceptable to download the `locale.json.tar.gz` file
and place it in a convenient location. Eventually I'll settle on a
location for the file - probably "~/.config/trix/assets", or possibly
"~/.assets".

```python3
from trix import *
f = trix.path("~/dev/locale_json.tar.gz").wrapper(encoding="utf8")

f.names.sorted.table(w=4)  # list avaialable language files
f.read("ber_MA.utf8")


```


#### Instructions for creating locale_json tar (or zip!) files:

The set of locale files is not complete - only those files that are
marked "utf-8" are in the resulting file (and, again, the "Galacian
Spain" set is missing due to my inability to download it.)

If you'd like to try importing your own set of language files, the 
following has been tested on several Linux systems. NOTE: It almost 
certainly will not work on any MS Windows system.


###### Import instructions:

First, place the assets directory in the same directory as trix.

    /dev
      /assets
      /trix

Then, in a terminal, cd to the directory containing both the trix and 
the assets packages, then...

    $ python3
    >>> import assets.locale_json.locale_import
    >>> 

This will create a tar file (or, potentially zip - see below) that
contains an archive member for each language file available to your 
*nix system. Each member consists of a json dict structure containing
locale formats.

The resulting file will, for now, have to be moved manually to the
~/.cache/trix/assets directory. If this turns out to be a project I
want to pursue, I'll eventually improve the instalation process.

It takes me about 20-30 seconds for the process to complete.

The lines for generating a zip archive containing the locale json 
members have been commented, as zip was much larger than the tar, but
if you prefer to comment tar and use zip, it's very easy to see in 
the `locale_import` script how to do that (or how to get both!) 
if you know any python at all.




#### important information

The assets module and trix module must be in the same directory in
order for the `locale_json` module to generate the locale assets file.

I'm developing assets in a separate project from trix, but the assets
project does require trix for generation of the data it contains. The
`locale_json` module (which generates the locale_json.tar.gz file) 
requires that the assets and trix modules be together in the same 
directory.

However, if you're only interested in using the resulting files, I 
guess assets can be anywhere you like.




#### possible additional asset packages

I have several more ideas for asset packages, including:

 * locale_json:
   The `locale_json` package is only a demo.
   
   This first `assets` module is not yet complete. It will take me a
   while to download and import all the various locale packages so as
   to create a tar file with at least one representation of each of 
   the locales (as json dict of format strings).
 
 * unicode_data:
   An sqlite3 database to replace the `udata.query()` functionality.
   I'd really like to run queries on the UDB using SQL! Wouldn't you?
 
 * world factbook:
   A database containing WFB data. This will be the hardest one - I've
   been struggling, off and on, for quite a while to find the right 
   database structure. I hope I'm up to the task!
 
 * web interface:
   A local http user interface to trix functionality.
 
 * trix-specific language files:
   Language files for all error and informational messages generated
   by trix. (I'll do the english version and accept contributions
   for other language translations.)




###### ...maybe.

Just because they're listed here doesn't mean all (or any) of these
ideas will ever come to fruition. They're just ideas.

:)

