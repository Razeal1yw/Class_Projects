#!/usr/bin/python

# A House of Dust, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
# Original by Alison Knowles & James Tenney, 1967
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Updated 10 March 2015 to remove a duplicate value in "place".
# Updated 17 November 2015 to remove a near-duplicate value in "inhabitants".
# Updated 31 May 2018 to add compatibility with Python 3 (Python 2 still works)

from random import choice

material = ['Gravel', 'Granite', 'Wood', 'Steel', 'Glass', 'Grass', 'Breeze Bloc', 'Water', 'Soap', 'Cardboard', 'Silk', 'Cotton', 'Coke', 'Balls', 'Rubber', 'Candy', 'Plastic']

location = ['In a, beautiful field', 'In a major city', 'Near the ocean', 'Close to a creepy lake', 'In a sandy desert', 'In an amazing forest', 'In Detroit', 'A large village', 'Downtown', 'Near the University', 'ON AN ISLAND', 'IN A COLD, WINDY CLIMATE', 'IN A PLACE WITH BOTH HEAVY RAIN AND BRIGHT SUN', 'IN A DESERTED AIRPORT', 'IN A HOT CLIMATE', 'INSIDE A MOUNTAIN', 'ON THE SEA', 'IN MICHIGAN', 'IN HEAVY JUNGLE UNDERGROWTH', 'BY A RIVER', 'AMONG OTHER HOUSES', 'IN A DESERTED CHURCH', 'IN A METROPOLIS', 'UNDERWATER']

light_source = ['CANDLES', 'ALL AVAILABLE LIGHTING', 'ELECTRICITY', 'NATURAL LIGHT']

inhabitants = ['PEOPLE WHO SLEEP VERY LITTLE', 'VEGETARIANS', 'HORSES AND BIRDS', 'PEOPLE SPEAKING MANY LANGUAGES WEARING LITTLE OR NO CLOTHING', 'ALL RACES OF MEN REPRESENTED WEARING PREDOMINANTLY RED CLOTHING', 'CHILDREN AND OLD PEOPLE', 'VARIOUS BIRDS AND FISH', 'LOVERS', 'PEOPLE WHO ENJOY EATING TOGETHER', 'PEOPLE WHO EAT A GREAT DEAL', 'COLLECTORS OF ALL TYPES', 'FRIENDS AND ENEMIES', 'PEOPLE WHO SLEEP ALMOST ALL THE TIME', 'VERY TALL PEOPLE', 'AMERICAN INDIANS', 'LITTLE BOYS', 'PEOPLE FROM MANY WALKS OF LIFE', 'NEGROS WEARING ALL COLORS', 'FRIENDS', 'FRENCH AND GERMAN SPEAKING PEOPLE', 'FISHERMEN AND FAMILIES', 'PEOPLE WHO LOVE TO READ']

materialchosen = choice(material)

while materialchosen != 'Wood':

    materialchosen = choice(material)
    print('')
    print('A city of ' + materialchosen)
    print('      ' + choice(location))
    print('            USING ' + choice(light_source))
    print('                  INHABITED BY ' + choice(inhabitants))
    print('')
