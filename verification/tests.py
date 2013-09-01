"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "1.Simple": [
        {
            "input": "Http://Www.Checkio.org",
            "answer": "http://www.checkio.org"

        },
        {
            "input": "http://www.checkio.org/%cc%b1bac",
            "answer": "http://www.checkio.org/%CC%B1bac"
        },
        {
            "input": "http://www.checkio.org/task%5F%31",
            "answer": "http://www.checkio.org/task_1"
        },
        {
            "input": "http://www.checkio.org:80/home/",
            "answer": "http://www.checkio.org/home/"
        },
        {
            "input": "http://www.checkio.org/task/./1/../2/././name",
            "answer": "http://www.checkio.org/task/2/name"
        }

    ],
    "2.Complex": [
        {
            "input": "HTTP://EXAMPLE.COM:80",
            "answer": "http://example.com",
            "explanation": [
                "HTTP://EXAMPLE.COM"
            ]
        },
        {
            "input": "http://Example.com:80/%48%6f%6d%45",
            "answer": "http://example.com/home",
            "explanation": [
                "http://Example.com/%48%6f%6d%45",
                "http://Example.com/HomE",
            ]
        },
        {
            "input": "http://example.com/%31%30%2D%2f%2E%1f%5F%7E",
            "answer": "http://example.com/10-%2F.%1F_~",
            "explanation": [
                "http://example.com/10-%2f.%1f_~",
            ]
        },
        {
            "input": "http://example.com:80/HOME/../././Guest/1/../2/..",
            "answer": "http://example.com/guest",
            "explanation": [
                "http://example.com:80/Guest",
                "http://example.com:/Guest"
            ]
        }

    ],
    "3. All together.": [
        {
            "input": "http://Www.Checkio.org:80/ta%73K%2d/1/../2/./%3f%3e",
            "answer": "http://www.checkio.org/task-/2/%3F%3E",
            "explanation": [
                "http://Www.Checkio.org:80/ta%73K%2d/2/%3f%3e",
                "http://Www.Checkio.org:80/tasK-/2/%3f%3e",
                "http://Www.Checkio.org/tasK-/2/%3f%3e",
                "http://Www.Checkio.org/tasK-/2/%3F%3E"
            ]
        }
    ]
}
