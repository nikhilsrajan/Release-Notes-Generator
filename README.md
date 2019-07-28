Release-Notes-Generator
=======================
Python code to write release notes in a neat format

How to use.
-----------
``from generator import *`` and write your file using the following functions.

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


**Run your program to get in a text file** ``release-notes.txt``**:**

    ---------------------------------------------------------
    Version	:	2.0.0.11_dev3
    Date	:	26-07-19
    Type	:	Internal Release.
    ---------------------------------------------------------

        NEW FEATURES:
        * main point
          - sub point
            - Sub-sub point.

        CHANGES:
        * main point
          - sub point
            - Sub-sub point.

        KNOWN ISSUES:
        * main point
          - sub point
            - Sub-sub point.

        BUG FIXES:
        * main point
          - sub point
            - Sub-sub point.

        NOTES:
        * main point
          - sub point
            - Sub-sub point.



