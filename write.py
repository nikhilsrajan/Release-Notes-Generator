from generator import *

Version(2, 0, 0, 11, DEV, 3)
Date(26, 7, 2019)
Type(INTERNAL_RELEASE)

Add(NEW_FEATURE, 1, "Catia XML Files now supported.")
Add(NEW_FEATURE, 2, "JT Files version 9.5 to 10.0 now supported.")
Add(NEW_FEATURE, 3, "Matot checking enabled.")

Add(CHANGE, 1, "'General Info' panel does not show information with value 0.")
Add(CHANGE, 2, "Object type sub-group removed from Project Explorer.")

Add(KNOWN_ISSUE, 1, "File names and part hierarchy is not extracted during JT import.")

Add(BUG_FIX, 1, "gibberish.")

Add(NOTE, 1, "Yo mama sucks.")

print(Compile())

Export('release-notes', 'txt')