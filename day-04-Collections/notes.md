# Day 4 Notes

## What I learned today

Today was about collections. This is how Python stores groups of data instead of just one value at a time.

Lists are ordered groups of items. You can have duplicates and you get items back by their position, starting from zero.

Dictionaries store data with labels. Instead of asking for "the third item", you ask for "the value under this name". I also learned that using .get() on a dictionary is safer than using square brackets, because it won't crash the program if the label doesn't exist.

Tuples are basically lists that can never be changed once created. I understood why that matters: sometimes you want to guarantee a value stays exactly as it was, like a coordinate or a fixed date.

Sets are groups of items where nothing repeats and order doesn't matter. What surprised me was how useful they are for checking if something is present, and how you can compare two sets directly using symbols like & for what they share, | for everything combined, and minus for what is only in one of them.

Comprehensions were the trickiest part. It's basically a shortcut for writing a loop that builds a new list in one line. It took me a bit to read them comfortably, but I understand now that they are just a shorter way to say the same thing a normal loop would do.

Nested data was the part that connected everything. Most real data isn't just one list or one dictionary, it's a mix, like a dictionary that contains a list, and that list contains more dictionaries inside it. That is exactly how data looks when it comes from a real file or a website.

## What I built

I built SentinelCLI. It's a small tool you run from the terminal, and you give it a file. If it's a CSV file it tells you how many rows and columns it has and what the headers are. If it's a JSON file it tells you if the data is a list or a dictionary and gives basic details about it. If it's a text or log file, it counts the lines and checks each one for suspicious words like error, failed, unauthorized, attack, and a few others, using a set to make that check fast.

## Breaking it on purpose

I tested it against an empty file and it gave a clear message instead of crashing.

I tested it against a broken JSON file with a missing character and it caught the problem and explained what went wrong instead of crashing the whole program.

I tested it against a very large file to see how it handled size.

I tested it against a file with no file extension at all.

What I actually saw when I ran each of these:
_(fill this part in yourself with the real output you saw)_

## Why this actually matters in real life

This is basically a tiny version of what real security and data tools do every day. Companies scan through huge log files looking for the same kind of warning signs I was looking for, just with way more rules and way more data. The set trick I used to catch suspicious words is the same basic idea behind real alert systems, because checking if something belongs to a group needs to be fast when you're dealing with millions of lines.

The part where I checked the shape of a file before trusting it, like counting columns or checking if something is a list or a dictionary, is something real systems do constantly before they process any data. If the shape looks wrong, they stop and flag it instead of blindly continuing.

The part where my program caught a broken file instead of crashing completely is a small preview of something bigger I'll learn soon, which is how real software handles bad input gracefully instead of just falling apart.

And honestly, the biggest thing this taught me is that a project only feels real once someone else could pick it up, read the readme, run one command, and understand what it does without me explaining anything. That's the actual standard I'm building toward.
