import itertools
import json
import requests
import re
from bs4 import BeautifulSoup

BASE_COURSE_LANDPAGE_URL = (
    "https://engineering.calendar.utoronto.ca/search-courses?page="
)
BASE_COURSE_SPECIFIC_URL = "https://engineering.calendar.utoronto.ca/course/"
MAX_COURSES_PER_PAGE = 30
TOTAL_PAGES = 19
COURSE_REGEX = re.compile(r"[A-Z]{3}\d{3}[A-Z]\d\s-\s")
KEYWORD_REGEX = re.compile(
    r"Fixed Credit Value|Hours|Description|Prerequisite|Corequisite|Exclusion|Recommended Preparation|Total AUs|Program Tags|©\xa0Faculty of Applied Science & Engineering"
)
KEYWORD_REQUISITES_REGEX = re.compile(
    r"Prerequisite|Corequisite|Exclusion|Recommended Preparation"
)
courses = []
# NOTE: ESC499 is a special case where Recommended Preparation is malformed

for page_num in range(0, TOTAL_PAGES):

    page = requests.get(BASE_COURSE_LANDPAGE_URL + str(page_num))
    soup = BeautifulSoup(page.text, "html.parser")
    strings = list(soup.stripped_strings)

    titles = list(filter(COURSE_REGEX.match, strings))
    assert (
        len(titles) == MAX_COURSES_PER_PAGE or page_num == TOTAL_PAGES - 1
    ), f"Expected {MAX_COURSES_PER_PAGE} courses, but got {len(titles)}"
    courses.extend(
        [
            {"course_code": course_code, "course_name": course_name}
            for course_code, course_name in (title.split(" - ", 1) for title in titles)
        ]
    )


for course in courses:
    page = requests.get(BASE_COURSE_SPECIFIC_URL + course["course_code"])

    soup = BeautifulSoup(page.text, "html.parser")
    strings = [string for string in soup.stripped_strings]

    keyword_index_iterator_real, keyword_index_iterator_peek = itertools.tee(
        index for index, s in enumerate(strings) if re.match(KEYWORD_REGEX, s)
    )
    next(keyword_index_iterator_peek)

    for index in keyword_index_iterator_real:
        nextIndex = next(keyword_index_iterator_peek, -1)
        if nextIndex == -1:
            break
        key = strings[index].lower().replace(" ", "_")
        value = []
        for i in range(index + 1, nextIndex):
            value.append(strings[i])
        if re.match(KEYWORD_REQUISITES_REGEX, key):
            value = (
                " ".join(value)
                .replace(" . ", ". ")
                .replace(" , ", ", ")
                .replace(" / ", "/")
            )
        else:
            value = "".join(value)
        course[key] = value

with open("courses.json", "a+") as writer:
    writer.write(json.dumps(courses, indent=2))
