import random

def generate_quiz(summary):

    # Split summary into sentences
    sentences = [
        s.strip()
        for s in summary.replace("\n", " ").split(".")
        if len(s.strip()) > 20
    ]

    quiz = ""

    # Create exactly 10 questions
    for i in range(10):

        if len(sentences) == 0:
            sentence = "Artificial Intelligence is an important technology."
        else:
            sentence = sentences[i % len(sentences)]

        words = sentence.split()

        # Find a keyword
        keyword = None

        for word in words:
            if len(word) > 5:
                keyword = word
                break

        if keyword is None:
            keyword = words[0]

        question = sentence.replace(keyword, "_____")

        options = [
            keyword,
            "Database",
            "Operating System",
            "Compiler"
        ]

        random.shuffle(options)

        answer = chr(65 + options.index(keyword))

        quiz += f"""
Question {i+1}

{question}

A. {options[0]}
B. {options[1]}
C. {options[2]}
D. {options[3]}

Answer: {answer}

--------------------------------------------------

"""

    return quiz