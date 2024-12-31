from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a knight or a knave (but not both)
    Or(AKnight, AKnave),
    # A cannot be both a knight and a knave at the same time
    Not(And(AKnight, AKnave)),
    # If A is a knight, then A's statement "I am both a knight and a knave" must be true
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a knight or a knave, Same applies for B
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # A cannot be both Knight and Knave, Same applies for B
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    # If A is a knight, statement is truen(both are knaves)
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Basic Rules:
    # A is either a knight or a knave, Same applies for B
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    # A cannot be both Knight and Knave, Same applies for B
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    # If A is a knight, their statement must be true
    # "Same kind" means either both knights or both knaves
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, their statement must be false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # If B is a knight, their statement must be true
    # "Different kind" means either A is knight/knave or B is knight/knave
    Implication(BKnight, Or(And(AKnight, BKnave), And(BKnight, AKnave))),
    # If B is a Knave, their statement must be false.
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(BKnight, AKnave))))
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Basic rules
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # B's first statement: "A said 'I am a knave'"
    Implication(BKnight, 
        Or(
            # If A is knight, must have said "I am a knight" (true)
            And(AKnight, AKnight),
            # If A is knave, must have said "I am a knight" (false)
            And(AKnave, Not(AKnight))
        )
    ),
    Implication(BKnave, 
        Not(Or(
            And(AKnight, AKnight),
            And(AKnave, Not(AKnight))
        ))
    ),

    # B's second statement: "C is a knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C's statement: "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
