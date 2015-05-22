# Blackhat Challenge: Report
## Ken Weaver

This is my report detailing what I did for the blackhat challenge. 

## Methods Details

### Substitution Cipher

This is the only cipher that I did by hand. It seemed easier to just
take the letter frequencies and try different combinations, obviously
with letters more common in English more likely to be common letters
in my cipher. 

### Vigenere Cipher

 To identify this cipher, I calculated a vigenere score, which is
 basicallly just the lowest score where I guessed a keyword length
 between 6-9, tried every possible shift with that keyword length, 
 and calculated the distances (for each subtext, chi squared) from 
 english letter frequencies. It was pretty obvious which one was 
 vigenere from this, and it also told me the length of the key. 
 Once you know that, cracking it is just solving several shift 
 ciphers, which is trivial. 

 ### Column Transposition Cipher

 This cipher took me a few days to crack. Initially my plan was to 
 look for a common word with not so common letters ('be', 'the', etc.)
 for difference number of columns, noting that if the columns are 
 the same length the letters will appear in the same position within
 the columns. Unfortunately, the columns are not the same length and
 trying to write a search algorithm taking this into account led to 
 more problems, so I abondoned this approach. 

 I then moved onto other techniques. Because of the way the column
 transposition cipher works, portions of plaintext can be revealed
 if you only have part of the key right. At first I thought to leverage
 this and try a genetic algorithm, but the implementation proved 
 nontrivial, so I moved on to simulated annealing. After a few bugs, the
 last required breakthrough was to use a quadragram scoring statistic
 with a python dictionary for fast score lookups. Once I did this, the 
 algorithm found a solution with a test ciphertext encoded with a length
 20 key in a matter of a minute or two. Once I knew this, it was just a 
 matter of trying it on every possible key length, and I found an answer
 with a length 11 key. 

 If you're curious, to take a step in simulated annealing, I shifted a random
 number of columns a random number of places left or right. This has the 
 intended result of being able to keep chunks of columns together, unlike
 swapping. This was also a minor breakthrough, as I had been using swapping 
 for a while. 

 ### Hill Cipher

 This one was a bit of a let down after column transposition. I literally
 just brute forced it, trying all invertible matrices. It only took a minute 
 or two to crack this after I'd written the code. 

 ### Playfair Cipher

 As of writing this, I haven't gotten the time to crack playfair. When I do 
 (and I do intend on doing it just for completeness sake) I think I'll probably
 do it again by simulated annealing, for the same reasons that I used SA for 
 the column transposition cipher. I'll use swapping instead of shifting and digram
 instead of quadragram statistics, because playfair is entirely a digram 
 substitution method. 

 ## Plaintexts