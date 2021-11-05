# Keywords
# సంఖ్య, ఇన్పుట్, return - తిరిగి_ఇవ్వు
# ఒకవేల, అయితే, కాకపోతే, గాని, ఇంకా, అయ్యేవరకు

import re

transform_maps = [
    {
        "keyword": "if-then",
        "regex": r"(?m)^(\s*)ఒకవేల(\s*)(\(.*\))(\s*)అయితే(\s*):",
        "subst": "\\1if\\3:",
        "test_str_in": "	ఒకవేల  (నెల == 2)   అయితే:",
        "test_str_out": "   if(నెల == 2):"
    },
    {
        "keyword": "else",
        "regex": r"(?m)^(\s*)కాకపోతే(\s*):",
        "subst": "\\1else:",
        "test_str_in": "	కాకపోతే  :",
        "test_str_out": "	else:"
    },
    {
        "keyword": "while",
        "regex": r"(?m)^(\s*)(\(.*\))(\s*)అయ్యేవరకు(\s*):",
        "subst": "\\1while\\2:",
        "test_str_in": "    (సంఖ్య <= n)   అయ్యేవరకు     :\n",
        "test_str_out": "	while(సంఖ్య <= n):"
    },
    {
        "keyword": "or",
        "regex": r"(?m)\) గాని \(",
        "subst": ") or (",
        "test_str_in": "ఒకవేల ((నెల == 4) గాని (నెల == 9) గాని (నెల == 11)) అయితే:\n",
        "test_str_out": "if((నెల == 4) or (నెల == 9) or (నెల == 11)):\n"
    },
    {
        "keyword": "and",
        "regex": r"(?m)\) ఇంకా \(",
        "subst": ") and (",
        "test_str_in": "ఒకవేల ((నెల % 4 == 0) ఇంకా (నెల % 100 == 0)) అయితే:\n",
        "test_str_out": "ఒకవేల ((నెల % 4 == 0) and (నెల % 100 == 0)) అయితే:\n"
    },
    {
        "keyword": "print",
        "regex": r"(?m)^(\s*)చూపించు(\s*)\((.*)\)",
        "subst": "\\1print(\\3)",
        "test_str_in": "        చూపించు(\"28 లేద 29\")",
        "test_str_out": "        print(\"28 లేద 29\")"
    },
    {
        "keyword": "return",
        "regex": r"(?m)^(\s*)తిరిగి_ఇవ్వు(\s*)(\w*)",
        "subst": "\\1return \\3",
        "test_str_in": "	తిరిగి_ఇవ్వు  9\n",
        "test_str_out": "	return  9\n"
    },
    {
        "keyword": "int",
        "regex": r"(?m)^(\s*)(.*)సంఖ్య(\s*)\((.*)\)",
        "subst": "\\1\\2int(\\4)",
        "test_str_in": "నెల = సంఖ్య(input(\"నెల యొక్క నంబరు రాయుము: \"))\n",
        "test_str_out": "నెల = int(input(\"నెల యొక్క నంబరు రాయుము: \"))\n"
    },
    {
        "keyword": "input",
        "regex": r"(?m)^(\s*)(.*)ఇన్పుట్(\s*)\((.*)\)",
        "subst": "\\1\\2input(\\4)",
        "test_str_in": "నెల = సంఖ్య(ఇన్పుట్  (\"నెల యొక్క నంబరు రాయుము: \"))\n",
        "test_str_out": "నెల = సంఖ్య(input(\"నెల యొక్క నంబరు రాయుము: \"))\n"
    }
]


def transform_to_python(program_str):
    global transform_maps
    for t in transform_maps:
        program_str = re.sub(t["regex"], t["subst"], program_str, 0)
    return program_str


sample = """
def నెల_లో_రోజులు ():
    నెల = సంఖ్య(ఇన్పుట్("నెల యొక్క నంబరు రాయుము: "))

    ఒకవేల(నెల == 2) అయితే:
        చూపించు ("28 లేద 29")
    కాకపోతే:
        ఒకవేల((నెల == 4) గాని (నెల == 6) గాని (నెల == 9) గాని (నెల == 11)) అయితే:
            చూపించు ("30")
        కాకపోతే:
            చూపించు ("31")


నెల_లో_రోజులు()
"""

sample2 = """
def నెల_లో_రోజులు ():
    నెల = int(input("నెల యొక్క నంబరు రాయుము: "))

    ఒకవేల(నెల == 2) అయితే:
        చూపించు ("28 లేద 29")
    కాకపోతే:
        ఒకవేల((నెల == 4) గాని (నెల == 6) గాని (నెల == 9) గాని (నెల == 11)) అయితే:
            చూపించు ("30")
        కాకపోతే:
            చూపించు ("31")


నెల_లో_రోజులు()
"""

# TODO: how to avoid usage of keywords in code
sample3 = """
def వరకు_చూపించు(n):
    సంఖ్య = 1
    (సంఖ్య <= n) అయ్యేవరకు:
        చూపించు(సంఖ్య)
        సంఖ్య = సంఖ్య + 1

వరకు_చూపించు(5)
"""

sample4 = """
def వరకు_చూపించు(n):
    సంఖ్య = 1
    (సంఖ్య <= n) అయ్యేవరకు:
        చూపించు(సంఖ్య)
        సంఖ్య = సంఖ్య + 1
    తిరిగి_ఇవ్వు సంఖ్య
    
k = వరకు_చూపించు(5)
చూపించు(k)
"""

print(transform_to_python(sample4))
