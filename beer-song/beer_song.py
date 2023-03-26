VERSES = {
   0:('No more bottles of beer on the wall, no more bottles of beer.',
      'Go to the store and buy some more, 99 bottles of beer on the wall.'),
   1:('1 bottle of beer on the wall, 1 bottle of beer.',
      'Take it down and pass it around, no more bottles of beer on the wall.'),
   2:('2 bottles of beer on the wall, 2 bottles of beer.',
      'Take one down and pass it around, 1 bottle of beer on the wall.'),
  -1:('{num} bottles of beer on the wall, {num} bottles of beer.',
      'Take one down and pass it around, {num} bottles of beer on the wall.')}

def recite(start, take=1):
    out = []
    for bottle in range(start, start - take, -1):
        verses = VERSES.get(bottle, VERSES.get(-1))
        out.append(verses[0].format(num = bottle))
        out.append(verses[1].format(num = bottle - 1))
        out.append("")
    return out[0:3*take-1]