The grep command is a very powerful way to find documents on your computer. You can use grep to see if a file contains a word or use one of many forms of regular expression to search for a pattern instead. Grep can check the file that you specify or can search an entire tree of your filesystem recursively looking for matching files.

One of the most basic ways to use grep is shown below, looking for the lines of a file that match a pattern. I limit the search to only text files in the current directory *.txt and the -i option makes the search case-insensitive. As you can see, the only matches for the string "this" are the capitalized string "This".
 - grep -i this sample.txt


The -A, -B, and -C options to grep let you see a little bit more context than a single line that matched. These options let you specify the number of trailing, preceding, and both trailing and preceding lines to print, respectively. Matches are shown separated with a "---" line so you can clearly see the context for each match in the presented results. Notice that the last example using -C 1 to grab both the preceding line and trailing line shows four results in the last match. This is because there are two matches (the middle two lines) that share the same context.
 - grep -A 2 It sample.txt --> this would ouptut:
 "It contains a few lines of text
 that we can use to search for things.
 Samples of text"

 - grep -C 1 -i the sample.txt --> this would output:
 "This is the sample file.
 It contains a few lines of text
 --
 and seeking those samples
 there can be many matches
 but not all of them are fun
 so start searching for samples"

The -n option can be used to show the line number that is being presented. Below I grab one line before and one line after the match and see the line numbers, too.
 - grep -n -C 1 -i tha sample.txt --> this will output:
 "2-It contains a few lines of text
 3:that we can use to search for things.
 4-Samples of text
 --
 8-so start searching for samples
 9:start looking for text that matches"


##### Digging through a bunch of files
You can get grep to recurse into a directory using the **-R** option. When you use this, the matching file name is shown on the output as well as the match itself. When you combine **-R** with **-n** the file name is first shown, then the line number, and then the matching line.

 sample .
 ./grep.MD: - grep -i this sample.txt
 ./grep.MD: - grep -A 2 It sample.txt --> this would ouptut:
 ./grep.MD: - grep -C 1 -i the sample.txt --> this would output:
 ./grep.MD: "This is the sample file.
 ./grep.MD: and seeking those samples
 ./grep.MD: so start searching for samples"
 ./grep.MD: - grep -n -C 1 -i tha sample.txt --> this will output:
 ./grep.MD: 8-so start searching for samples
 ./sample.txt:This is the sample file.
 ./sample.txt:and seeking those samples
 ./sample.txt:so start searching for samples

 myyahayhs@MYSMYYAHAYHS5 MINGW32 /d/Projects/StayingSharp/commands
 $ grep -n -R sample .
 ./grep.MD:4: - grep -i this sample.txt
 ./grep.MD:8: - grep -A 2 It sample.txt --> this would ouptut:
 ./grep.MD:13: - grep -C 1 -i the sample.txt --> this would output:
 ./grep.MD:14: "This is the sample file.
 ./grep.MD:17: and seeking those samples
 ./grep.MD:20: so start searching for samples"
 ./grep.MD:23: - grep -n -C 1 -i tha sample.txt --> this will output:
 ./grep.MD:28: 8-so start searching for samples
 ./sample.txt:1:This is the sample file.





