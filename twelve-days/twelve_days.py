dict = {
    1:("one", "first", "a Partridge in a Pear Tree."),
    2:("two", "second", "Turtle Doves"),
    3:("three", "third", "French Hens"),
    4:("four", "fourth", "Calling Birds"),
    5:("five", "fifth", "Gold Rings"),
    6:("six", "sixth", "Geese-a-Laying"),
    7:("seven", "seventh", "Swans-a-Swimming"),
    8:("eight", "eighth", "Maids-a-Milking"),
    9:("nine", "ninth", "Ladies Dancing"),
    10:("ten", "tenth", "Lords-a-Leaping"),
    11:("eleven", "eleventh", "Pipers Piping"),
    12:("twelve", "twelfth", "Drummers Drumming")
    }

def recite(start_verse, end_verse):
    out = []
    for i in range(start_verse, end_verse + 1):
        first_part = second_part = str()
        for j in range(i, 1, -1):
            second_part += dict.get(j)[0] + " " + dict.get(j)[2] + ", "
        second_part += "and " + dict.get(1)[2] if i > 1 else dict.get(1)[2]
        first_part = f"On the {dict.get(i)[1]} day of Christmas my true love gave to me: "
        out.append(first_part + second_part)
    return out