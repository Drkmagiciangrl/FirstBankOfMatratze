# FirstBankOfMatratze
Python Class Graded Exercise

Running the program: python3 ashleys_mattress.py

Background

UMBC instructors are paid using bags of spare change.  The preferred method 
of saving for retirement is to stuff all these bags under a mattress.

Write a program that allows the user to enter in a number of different types
of US Coinage, which are contained in a number of bags or sacks.  Each bag is
stuffed under a mattress.  For undisclosed purposes, one bag should be labeled 
as a "Bugout-Bag", ready to go at a moment's notice.  One option of the program
is to bug out, which quits the program.

The bags have a few important behaviors.

It is possible to deposit or withdraw a bag from under the mattress.
Given two bags, it is possible to transfer the entire contents of one bag into 
the other.  Bags have an optional label on the front that may be stitched on 
once when the bag is made (and then never changed after that).
When interacting with the mattress, it should always be possible to find the 
total value stuffed under it in all bags.  It should also be possible to view
a list of all bags, sorted by value.

Requirements

Whenever money is removed, via withdrawal or bugging out, the number and type 
of each coin should be printed.
Plural and singular nouns must be infected properly: "2 pennies" vs. "1 penny".
When listing bags, sort them by value, except for the bag named "Bugout-Bag",
which should always be listed first.
A bag without a name should get a unique number assigned to it.  Two different
bags should never have the same number, and bag numbers must not be reused.
Omit any mentions of "0 coins".
Line up monetary amounts in bag listings by decimal point.
Respond intelligently to invalid commands or inputs.

Challenges

Store all data entered during the program to disk.  This way, it should be
possible to exit the program, then start it again, and still work with the
data entered in the previous session.  There must now be an option to quit
without "bugging out", and bugging out should remove any extant accounts 
from disk.

Support a subset of your choice of different types of currency.  It should
be possible to get the value of the entire mattress' contents converted to
a single currency (pick a conversion rate and hard-code it; you do not need
to query the internet for the most current exchange rate!).
