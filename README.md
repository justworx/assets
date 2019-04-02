
# locale data asset package demo

This is a demo of locale_data json files, that will (hopefully) allow
access to use of data from more than one locale on MS Windows (which 
doesn't natively support use of any but the one locale set in the
preferences control pannel) and on *nix systems that have trouble with
use of multiple locales in threaded apps.

NOTE: This is ONLY A DEMO! It does work as intended, but fewer than 
      half the number of available locales are currently included.
      It's here mostly as a backup, but comments are welcome.


###### Instructions for creating locale_json tar (or zip!) files:

The following has been tested on several Linux systems. It almost 
certainly will not work on MS Windows.

First, place the assets directory in the same directory as trix. Eg.,

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

It took me about 17 seconds for the process to complete, but I was
generating both tar and zip files. The lines for generating a zip
archive containing the locale json members have been commented, as 
zip was much larger than the tar, but if you prefer to comment tar  
and use zip, it's very easy to see in the `locale_import` script how 
to do that (or how to get both!) if you know any python at all.




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
   to create a tar file with ALL locales (as json dict of format 
   strings).
 
 * unicode_data:
   An sqlite3 database to replace the `udata.query()` functionality.
   I'd really like to run queries on the UDB using SQL! Wouldn't you?
 
 * world factbook:
   A database containing WFB data. This will be the hardest one - I've
   been struggling, off and on, for quite a while to find the right 
   database structure. I hope I'm up to the task!
 
 * web interface:
   A local http user interface to trix functionality.
 
 * trix language files:
   Language files for all error and informational messages generated
   by trix. (I'll do the english version and accept contributions
   for other language translations.)




###### ...maybe.

Just because they're listed here doesn't mean all (or any) of these
ideas will ever come to fruition. They're just ideas.

:)

