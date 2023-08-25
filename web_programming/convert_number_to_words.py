import math


def convert(number: int) -> str:
    """
    Given a number return the number in words.

    >>> convert(123)
    'OneHundred,TwentyThree'
    """
    if number == 0:
        words = "Zero"
        return words
    else:
        digits = math.log10(number)
        digits = digits + 1
        singles = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        doubles = {
            0: "",
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        teens = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen",
        }
        placevalue = {2: "Hundred,", 3: "Thousand,", 5: "Lakh,"}
        placevalue[7] = "Crore,"

        temp_num = number
        words = ""
        counter = 0
        digits = int(digits)
        while counter < digits:
            current = temp_num % 10
            if counter % 2 == 0:
                addition = ""
                if counter in placevalue and current != 0:
                    addition = placevalue[counter]
                if (
                    counter != 2
                    and counter == 0
                    and ((temp_num % 100) // 10) == 1
                ):
                    words = teens[current] + addition + words
                    temp_num = temp_num // 10
                    counter += 1
                elif counter != 2 and counter == 0 or counter == 2:
                    words = singles[current] + addition + words

                else:
                    words = doubles[current] + addition + words

            else:
                if counter == 1:
                    if current == 1:
                        words = teens[number % 10] + words
                    else:
                        addition = ""
                        if counter in placevalue:
                            addition = placevalue[counter]
                        words = doubles[current] + addition + words
                else:
                    addition = ""
                    if counter in placevalue:
                        if current != 0 and ((temp_num % 100) // 10) != 0:
                            addition = placevalue[counter]
                    if ((temp_num % 100) // 10) == 1:
                        words = teens[current] + addition + words
                        temp_num = temp_num // 10
                        counter += 1
                    else:
                        words = singles[current] + addition + words
            counter += 1
            temp_num = temp_num // 10
    return words


if __name__ == "__main__":
    import doctest

    doctest.testmod()
