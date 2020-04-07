import random
from typing import List, Tuple
from datetime import datetime
from p_models import Tag, Author, Publication

TAGS = ('Fantasy', 'Sci-Fi', 'Mystery', 'Thriller', 'Romance', 'Westerns', 'Dystopian', 'Contemporary')
AUTHORS = (
    ('Conrad', 'Aiken'), ('James', 'Bowie'), ('Jim', 'Brown'), ('Erskine', 'Caldwell'), ('James', 'E.'),
    ('Ray', 'Charles'),
    ('Lucius', 'D.'), ('Ty', 'Cobb'), ('Charles', 'Coburn'), ('Ossie', 'Davis'), ('James', 'Dickey'),
    ('Mattiwilda', 'Dobbs'), ('Melvyn', 'Douglas'), ('Pete', 'Drake'), ('Rebecca', 'Latimer'),
    ('Lawrence', 'Fishburne'),
    ('Henry', 'W.'), ('Amy', 'Grant'), ('Oliver', 'Hardy'), ('Joel', 'Chandler'), ('Roland', 'Hayes'),
    ('Fletcher', 'Henderson'), ('Hulk', 'Hogan'), ('John', 'Henry'), ('Larry', 'Holmes'), ('Miriam', 'Hopkins'),
    ('Harry', 'James'), ('Jasper', 'Johns'), ('Bobby', 'Jones'), ('Stacy', 'Keach'), ('DeForest', 'Kelley'),
    ('Martin', 'Luther'), ('Gladys', 'Knight'), ('Joseph', 'R.'), ('Brenda', 'Lee'))

POSTS = (('Coronavirus Live Updates: U.S. Extends Social Curbs After Estimate of 200,000 Deaths\n',
          'Americans were told to avoid nonessential travel and gatherings of more than 10 people until at least '
          'April 30. Spain asked residents to go into “hibernation.” Prince Charles came out of isolation, '
          'while an adviser to Prime Minister Boris Johnson went into quarantine.\n'),
         ('President Trump, citing no specific data, says he expects new infections to peak by Easter.\n',
          'Two of the top doctors advising the White House on the coronavirus pandemic went together to the Oval '
          'Office with some sobering data to present to President Trump: Even with the aggressive measures in place '
          'in to slow the spread of the virus, as many as 200,000 Americans could die during the outbreak.\n'),
         ('Coronavirus Map: Tracking the Global Outbreak\n',
          'The coronavirus pandemic has sickened more than 729,100 people, according to official counts. As of Monday '
          'morning, at least 34,689 people have died, and the virus has been detected in at least 171 countries, '
          'as these maps show.\n'),
         ('China Created a Fail-Safe System to Track Contagions. It Failed.\n',
          'After SARS, Chinese health officials built an infectious disease reporting system to evade political '
          'meddling. But when the coronavirus emerged, so did fears of upsetting Beijing.\n'),
         ('Jobs Aren’t Being Destroyed This Fast Elsewhere. Why Is That?\n',
          'The coronavirus pandemic is laying bare structural deficiencies in America’s social programs. The relief '
          'package passed by Congress last week provides emergency fixes for some of these issues, but it also leaves '
          'critical problems untouched. To avoid a Great Depression, Congress must quickly design a more forceful '
          'response to the crisis.\n'),
         ('They Don’t Want to Risk Their Lives to Flip Your Burger\n',
          'Millions of white-collar workers are telecommuting from home to stay safe as the coronavirus extends its '
          'terrifying reach across America. But millions of other workers — supermarket cashiers, pharmacists, '
          'warehouse workers, bus drivers, meatpacking workers — still have to report to work each day, and many are '
          'furious that their employers are not doing enough to protect them against the pandemic.\n'),
         ('Nurses Die, Doctors Fall Sick and Panic Rises on Virus Front Lines\n',
          'A supervisor urged surgeons at Columbia University Irving Medical Center in Manhattan to volunteer for the '
          'front lines because half the intensive-care staff had already been sickened by coronavirus.\n'),
         ('N.Y.C.’s 911 System Is Overwhelmed. ‘I’m Terrified,’ a Paramedic Says.\n',
          '“I’m terrified,” said Mr. Suarez, who has been a paramedic in New York City for 26 years and had assisted '
          'in rescue efforts during the Sept. 11, 2001, terror attacks and later served in the Iraq war. “I honestly '
          'don’t know if I’m going to survive. I’m terrified of what I’ve already possibly brought home.”\n'),
         ('What Sept. 11 Taught Us About Confronting Catastrophe\n',
          'From careful planning and much drilling, medical workers knew without being told that they should roll a '
          'fleet of gurneys and wheelchairs onto the sidewalk outside St. Vincent’s Hospital in Greenwich Village on '
          'the morning of Sept. 11, 2001, New York’s last mortal catastrophe.')
         )


def add_tags():
    global TAGS
    total_len = len(TAGS)
    _len = 0
    for local_tag in TAGS:
        base_tag = Tag.objects.filter(name=local_tag)
        if base_tag:
            continue
        _len += 1
        Tag.objects.create(name=local_tag).save()
    print(f"Created {_len}/{total_len} tags")


def add_authors(max_number_of_authors_to_add=1000):
    global AUTHORS

    db_authors = Author.objects
    total_len = len(AUTHORS)
    _len = 0

    authors_to_add = max_number_of_authors_to_add - len(db_authors)
    authors_to_add = min(total_len, authors_to_add)

    if authors_to_add >= 0:
        for i in range(authors_to_add):
            name, surname = AUTHORS[i][0], AUTHORS[i][1]
            base_author = Author.objects.filter(name=name, surname=surname)
            if base_author:
                continue
            _len += 1
            Author.objects.create(name=name, surname=surname).save()
            if _len >= max_number_of_authors_to_add:
                break
    print(f"Created {_len}/{max_number_of_authors_to_add} authors")


def add_posts():
    global POSTS
    db_tags = Tag.objects
    db_authors = Author.objects
    # print(db_authors)
    for data in POSTS:
        author = db_authors[random.randint(0, len(db_authors) - 1)]
        # print(author)
        author.number_of_publications += 1
        author.save()

        tags_number = random.randint(1, 4)
        tags = []
        while tags_number > 0:
            tag = db_tags[random.randint(0, len(db_tags) - 1)]
            if tag not in tags:
                tags.append(tag)
                tags_number -= 1

        title = data[0]
        post = data[1]

        Publication.objects.create(title=title, post=post, date=datetime.now(), author=author, tags=tags).save()
    print(f"Created {len(POSTS)} posts")


if __name__ == '__main__':
    add_tags()
    add_authors(5)
    add_posts()
