from generator import *

Version(2, 0, 0, 11, DEV, 3)
Date(26, 7, 2019)
Type(INTERNAL_RELEASE)

Add(NEW_FEATURE, 1, "main point")
Add(NEW_FEATURE, 2, "sub point")
Add(NEW_FEATURE, 3, "sub-sub point.")

Add(CHANGE, 1, "main point")
Add(CHANGE, 2, "sub point")
Add(CHANGE, 4, "sub-sub-sub point.")

Add(KNOWN_ISSUE, 5, "sub-sub-sub-sub point")

Add(BUG_FIX, 6, "sub-sub-sub-sub-sub point")

Add(NOTE, 7, "sub-sub-sub-sub-sub-sub point")
Add(NOTE, 1, "main point")

print(Compile())

Export('release-notes', 'txt')
