'''Recently, the Napster company has been forced to block all copyrighted MP3 files from being downloaded.
This can protect the copyright of the songs, but all Napster users are not happy about this.
Therefore, one of the users has made a program to rename MP3 files,
so that Napster cannot identify the songs that should be blocked and therefore they can be downloaded freely.
The program reverses the order of the characters in a filename in order to cheat Napster.
For example, aXbYc.mp3 is changed to cYbXa.mp3. However, it is not convenient for Napster
users to read those meaningless words. To view the original filenames of the songs,
you are going to write a program to decode the filenames.

Note that this method can no longer cheat Napster, and Napster has actually declared bankruptcy.
'''

import re
a = input()
b = a[::-1]
c = re.sub('3pm\.', '', b)
c += '.mp3'
print(c)
