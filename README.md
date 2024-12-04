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
