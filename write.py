from generator import *

Version(2, 0, 0, 11, DEV, 3)
Date(26, 7, 2019)
Type(INTERNAL_RELEASE)

Add(NEW_FEATURE, 1, "main point")
Add(NEW_FEATURE, 2, "sub point")
Add(NEW_FEATURE, 3, "Sub-sub point.")

Add(CHANGE, 1, "main point")
Add(CHANGE, 2, "sub point")
Add(CHANGE, 3, "Sub-sub point.")

Add(KNOWN_ISSUE, 1, "main point")
Add(KNOWN_ISSUE, 2, "sub point")
Add(KNOWN_ISSUE, 3, "Sub-sub point.")

Add(BUG_FIX, 1, "main point")
Add(BUG_FIX, 2, "sub point")
Add(BUG_FIX, 3, "Sub-sub point.")

Add(NOTE, 1, "main point")
Add(NOTE, 2, "sub point")
Add(NOTE, 3, "Sub-sub point.")

print(Compile())

Export('release-notes', 'txt')
