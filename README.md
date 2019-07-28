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



**Run your program to get in a text file** ``release-notes.txt``**:**

    ---------------------------------------------------------
    Version	:	2.0.0.11_dev3
    Date	:	26-07-19
    Type	:	Internal Release.
    ---------------------------------------------------------

        NEW FEATURES:
        * main point
          - sub point
            - sub-sub point.

        CHANGES:
        * main point
          - sub point
              - sub-sub-sub point.

        KNOWN ISSUES:
                - sub-sub-sub-sub point

        BUG FIXES:
                  - sub-sub-sub-sub-sub point

        NOTES:
                    - sub-sub-sub-sub-sub-sub point
        * main point





