from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    tags = soup.find('h1')
    # print(tags)

    listTags = soup.find_all('li')
    #print(listTags)

    soup = BeautifulSoup(content, 'lxml')
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        # print(course_name)
        # print(course_price)

        print(f'{course_name} costs {course_price}')