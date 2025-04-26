prodRules = {
    "Sentence": ["Subject+Predicate"],
    "Subject": ["Article+Noun", "he", "she", "it"],
    "Predicate": ["Verb+Object"],
    "Object": ["Article+Noun", "him", "her", "it"],
    "Article": ["a", "the"],
    "Noun": ["boy","ball", "rock", "pumpkin", "girl"],
    "Verb": ["hit", "threw", "ate"],
}

terminSym = [
    "he",
    "she",
    "it",
    "him",
    "her",
    "a",
    "the",
    "boy",
    "ball",
    "rock",
    "pumpkin",
    "girl",
    "hit",
    "threw",
    "ate"
]

def evaluate(s : str, d: int, i: int):

    if i > d:
        # print("[-] Depth reached!")
        return

    # Checking if the input contains all terminal nodes
    allTerminal = True
    for node in s.split("+"):
        if node not in terminSym:
            allTerminal = False
            break

    # Printing if all terminal nodes
    if allTerminal:
        s = s.replace("+", " ")
        s = s[0].upper() + s[1:] + "."
        print(s)
        return


    for symbol in s.split("+"):

        if symbol in terminSym:
            pass
        
        else:
            possibleEvaluations = prodRules[symbol]

            for evaluation in possibleEvaluations:
                newS = s.replace(symbol, evaluation, 1)
                evaluate(newS, d, i + 1)


def main():
    depth = 6
    print(evaluate("Sentence", depth, 0))





if __name__ == "__main__":
    main()