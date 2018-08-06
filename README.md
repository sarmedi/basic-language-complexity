# basic-language-complexity
Basic Language Complexity Tool.


Uses helper module syllables.py that is used in the function find_num_syllables() to find the syllables in a word.


When given text from the User, program outputs:

  * ASL (average sentence length)

  * PHW (percent hard words [number of words with three or more syllabes that do not contain a hyphen or end in -es or-ed] )

  * All the words that qualify as 'hard words'

  * ASYL (average number of syllables)

  * GFRI (0.4*(ASL + PHW))

  * FKRI (206.835-1.015*(ASL-86.4)*ASYL)


GFRI and FKRI are slightly modifed versions of well-known readability measures named Gunnig-fog and Flesch Kincaid.  In Gunning-fog, the higher the value calculated the more difficult it is to read a text, while for Flesch Kincaid it is the opposite.
