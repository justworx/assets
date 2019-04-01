
from trix import *

#
# On *nix systems, the command "locale -a" returns a list of all
# installed locale files.
#
# The trix.callx() method's text property splits the locale data
# lines into individual list items.
#
loc_list = trix.callx("locale -a").text.lines()


#
# Create an archive to store each locale file
#	
#zfile = trix.path("locale_json.zip", affirm='touch').wrapper()
tfile = trix.path("locale_json.tar.gz", affirm='touch').wrapper()


# -------------------------------------------------------------------
# Loop through each item, creating a JSON file named for the 
# locale.
# -------------------------------------------------------------------

for loc in loc_list[1:]:
	
	# get locale data by calling the trix "loc" cline process
	locdata = trix.callx(cline='loc -c %s' % loc).text()
	member = loc
	
	# add locale to zip and tar files
	#zfile.write(loc, locdata)
	tfile.write(loc, locdata)


#zfile.flush()
tfile.flush()
