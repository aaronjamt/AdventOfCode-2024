# AdventOfCode-2024

My solutions to the Advent of Code challenge for 2024. I didn't think about publishing these until after Day 4, so most of the code is very much spaghetti just-make-it-work code. I also don't think I'll be reusing most of what I've written (at least, not as of Day 4), so I'm not too worried about keeping that clean and readable. I was also rushing to get them done as fast as possible since I was already nearly 4 days behind. Going forward I'll try to make it more readable, especially since I know I won't be able to be competitive with my late start.

## Warning: Spoilers! Don't read below or look at the code in this repo unless you've already completed the challenge(s) (or aren't going to)!
I won't be pushing updates until the day after each challenge, although I will commit my changes immediately, so don't think you can just watch this repo to steal my code (although I'm not sure you'd want to, anyways...)

## Day 1:
  Day 1 was fairly simple, which makes sense as it's just getting started. Part one just needs to sort the numbers, then iterate over and compare the differences, then output the sums. Part two just needed to take the number in the first list, count the number of times it appears in the second, and then multiple the value with the number of times it appears in the second, then sum all of those up.

## Day 2:
  Day 2, part one, was checking each line of the input against a set of rules and counting how many passed all of them. Part two was the same thing, except also checking if each line *could* be safe, if you removed one datapoint from the line. I wound up just iterating over each datapoint and testing if the line, minus that datapoint, was safe.

## Day 3:
  Day 3 was regex, baby! Oh boy do I love regex... Part one was just looking for `mul(X,Y)` in the input string, where X and Y are just integers, so that's a pretty simple `mul\(\d,\d\)`. Add a capture group and boom, `mul\((\d+,\d_)\)` which just returns `"X,Y"` strings, which is pretty easy to parse with `int()` and `str.split()`. Part two extended that, now also looking for `do()` and `don't()`, so I wound up adding a non-capture group around the `mul()` part (wrapping it with `(?:)`) so I could use the "OR" operator `|` to check for `do()` and `don't()` as well. That resulted in the final mess that is `(?:mul\((\d+,\d+)\))|(do(?:n't)?\(\))`. That was pretty simple in terms of the actual Python processing, most of the work was just the regex.

## Day 4:
  Day 4 was the first one I started on-time. It was quite interesting, although a bit of a pain. I opted to speedrun it and not bother documenting, commenting, or splitting things into functions until absolutely necessary, which wound up costing me in the end, since debugging was a pain. At [line 111](https://github.com/aaronjamt/AdventOfCode-2024/blob/main/day-4.py#L111), I had copied the `row, col, oppdir = dir` into the triple-nested `for` loops from an older version/idea I'd been working on, then spent probably 5-10 minutes tracking down why my outer `for` loop was breaking. Turns out, I was reassigning `row` and `col`. I just added `d` (for `diag`, short for `diagonal`) in front of the inner variables to prevent them from overwriting the outer ones, which fixed it, but had I been following best practices I wouldn't have had that issue. The code for part two is a complete mess and probably one of the worse ways to solve it, but it does technically work, and that's (mostly) all that matters.

## Day 5:
  Day 5 was farily easy, in my opinion. The first part was taking a list of items and checking it against a list of rules, which I figured out in 6 and a half minutes, according to the AoC website. The method you see in the file is the first (and final) method I went with. For part two, I copied the `is_valid()` function and initially just tried to swap the invalid pair when one was detected, and loop until complete, but it just sat in a loop for longer than I figured it should so I canceled it. I quickly realized that, since all the inputs must be able to be sorted into a valid order, I should be able to just add each item to a list one-at-a-time, checking each rule to find any constraints on its position in the list, until it makes it through all items, which feels like a far better solution than just "check if it's valid and try changing something if not" until it works. I did hold to my promise of writing more readable code, so far, and it's definitely worked out in my favor, so I'll try to keep that up going forward.

## Day 6:
  I started Day 6 about 10 minutes late, which I was sad about, but it wound up not mattering. I finished part one pretty quickly and even made a cool visualizer to show the guard movement (inspired by u/naclmolecule over on r/AdventOfCode). However, well, my implementation was not optimal. I wound up running it on two separate machines at once (changing the range for `all_positions` at the end) and even found an example on StackOverflow of how to use multiprocessing, but now I'm sitting here writing this with my CPU usage on both machines pinned to 100%. One of them has been running for 20 minutes and the other for 10 as I write this, yet they're only around halfway through finding all the possible object locations. Oh well!

## Day 7:
  After being late starting day 6, I set an alarm on my phone to hopefully prevent that going forward, and it worked today. In part one, since there were only two operators, I used the Python builtin `bin()` method to convert an int to a string of bits, then used `string.replace()` to convert to '*' and '+' operators. Actually performing the calculation was pretty easy, it just needed to iterate over each operator and digit and perform that operation to what was in the already-calculated part (or first digit, if at the beginning), so that was fairly simple to implement. However, part two added a third operator, making it trinary, rather than binary, which meant I had to implement int-to-trinary-string conversion myself. I added the '||' operator to the existing `try_equation()` method from part one (well, I shortened it to just '|' since that method was just iterating over a string. I could have used a list instead but it was easier to just do it that way). Fortunately, since I made the `try_equation()` method so simple and "generic", I was able to just reuse it for part two, just by making a wrapper method to convert from int to trinary, then passing the resulting string instead of passing the raw int.

## Day 8:
  In my math class, my professor recently reviewed "rise/run", which I think was the main reason I was able to solve this challenge fairly quickly and elegantly. Finding the rise and run between each pair of points is fairly simple, just subtract one from the other, and then I was able to add that to each existing antenna's position to find the antinodes for a given pair. For part two, I wound up just commenting out lines [33](https://github.com/aaronjamt/AdventOfCode-2024/blob/main/day-8.py#L33) and [34](https://github.com/aaronjamt/AdventOfCode-2024/blob/main/day-8.py#L34) and moving them into an inner function, which I then called with the harmonic number. Since harmonics are just repeated jumps further from the source, in this case, I multiply the rise and run by the harmonic number. For part one, then, it just calls that method with harmonic number=1, and for part two, it calls it over and over with increasingly large harmonics until both of them are outside the bounds of the map. The last issue I had to deal with was the fact that harmonic number=0 is also valid for the purposes of part two, so I wound up appending all existing antenna locations to that list, although writing this out I now realize I could have just changed [line 55](https://github.com/aaronjamt/AdventOfCode-2024/blob/main/day-8.py#L55) to start at 0, which would have solved the problem in the "proper" manner, and would have been faster and easier to do. Oh well, that's what I wound up using to solve the challenge, and that's what worked, so I'm not going to modify it before uploading it here.

## Minor update
  After Day 8, I decided that copy+pasting the beginning of the file from the previous day each time was getting rather tedious, so I instead wrote a small library that uses the filename of the program to determine the name for the input file, as well as reading the command line arguments to switch between example and main input. This allows me to just run `import input` at the top of each day's code to read in the corresponding input file, since that part of the code is consistent across challenges. It does abuse Python's module system a bit, by replacing itself in `sys.modules` with the actual input from the file, but this means that the single line `import input` now means that the rest of the program can just access `input` directly without having to call a function or assign it to a variable. In case future challenges don't rely on multiple lines in the file, or need to be handled in a different way, I decided not to have that module split the input by line, so that doesn't become a problem in the future.

## Day 9:
  This one stumped me for quite a bit, 46 minutes to be exact. I initially thought I was supposed to be solving the problem that turned out to be part two, but when I realized what the actual goal was, I was able to start making progress. The part that took the longest was optimizing it to take a reasonable amount of time to run. My first idea to make it faster was, instead of recalculating the list of occupied blocks every time, to do so once, and then swap its items at the same time as the main layout's items. That helped a lot and sped it up drastically, but then I decided to also shrink the search window as it went, since there's never a need to check for free space to the left of where we found it last time, nor to check for occupied space to the right. I tried to make it work without `new_` variables, by doing math instead, but spent probably 5-10 minutes fighting with that before I gave up and just used `new_` variables anyways. Even after that point, getting the exact logic down with which variables to add or subtract, and in what order, still took quite a while. One I solved part one and read part two, I was rather amused to find my initial interpretation of the problem staring my right back in my face. However, thanks to solving part one already, I was able to start down a different path than I initially had, which wound up being far more elegant than my original thought. Thankfully, that turned out to be significantly easier, since I could just use the Python builtin `.index()` method to find the start of that file, and then just count from there until the end of it. Come to think of it, I probably could have used the initial input somehow, since it directly provides the length of each file, rather than having to count its length by walking through the blocks. I also initially misinterpreted part two as well, and searched for the last file on disk rather than the last file _by id_, which was another example of me making my life harder for no reason... Anyways, final time was 46:09 for part one, 1:06:33 for part two.

## Day 10:
  Yay, double digits! This one felt fairly intuitive and I decided to start by writing the method to find the next increasing number for the trail, since I knew I would need that. From there, it was fairly simple to just try each direction to see if it can increase, recurse until reaching a 9 or a deadend, and then just return back up the chain to get the final result. Because of this, I got very lucky and was able to solve part two in a minute and 18 seconds, which was very nice.

## Day 11:
  I learned about `functools.cache()` and can't believe I've gone this long without knowing about it. After about 45 minutes struggling with part two, I decided to check the subreddit to see if I could find any hints, and saw [a meme mentioning it](https://www.reddit.com/r/adventofcode/comments/1hbmcoc/2024_day_11_part_2_when_in_doubt_reach_for_old/), which led me to read up on it with the Python docs. Turns out, it's the perfect solution to the problem and, after rewriting the entire program, it works far better, faster, and runs in a reasonable amount of time (near-instant!) for both parts. I left my original method in `day-11.bruteforce.py` which I used to solve part one.
