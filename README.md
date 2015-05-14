# Blackhat Challenge

This is a project for analyzing the blackhat challenge for MATH547 at the University of Delaware.
It will, with time, have code to assist in solving the Vigenere, Substitution, Hill, Playfair,
and Column Transposition ciphers.

## Usage
If you've stumbled onto this code, simply clone the directory and use the modules at will.
I'll have more info on exactly what they all do later. Contact me if you wish to be added as
a collaborator so I don't have as much work to do.

## Modules

### stringOps
Module for performing operations on strings. Currently has the following methods

       `shiftString(string, shift)`
       Shifts a `string` by `shift`. Not much else to say.

       `everyNth(string, start, n)`
       Takes every `n`th character starting with `start` of `string`

### matchFrequencies
Module for doing some frequency analysis. Has the following methods:

       `getFreq(fileName)`
       Gets frequency of letters from `fileName`

       `getString(fileName)`
       Gets the string from a file. NO NEWLINES ALLOWED.

       `getStrFreq(string)`
       Gets the letter frequency from a string.

       `matchFreq(fileName)`
       Don't worry about this, I'll deprecate it soon.

       `getVigenereDist(string)`
       Returns the lowest distance of a vigenere shifted string.

       `shiftedDist(string)`
       Calculates the minimum distance of a caesar shifted string.

       `englishDist(string)`
       Calculates the distance of a string from english letter frequencies. 