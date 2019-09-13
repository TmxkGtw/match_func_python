from match.match import Ob, Fn, Case, Pattern, match

def main():
    # it must print "1 < 2" only.
    match({
        Case(1 == 2) : Fn(print, "1 == 2"),
        Case(1 <  2) : Fn(print, "1 < 2"),
        Case(1 <= 2) : Fn(print, "1 <= 2")
    })

    # it must print "C" only.
    result = match([
        Pattern(1 == 2, "A"),
        Pattern(1 > 2,  "B"),
        Pattern(1 < 2,  "C")
    ])
    print(result)

if __name__ == "__main__":
    main()