import requests
import bs4


def get_html(town, year, month, day):
    url = f"https://ua.sinoptik.ua/погода-{town}/{year}-{month}-{day}"
    response = requests.get(url)
    return response.text


def get_weather(page):
    soup = bs4.BeautifulSoup(page, features="html.parser")

    data = []

    trs = soup.find('table', attrs={"class": "weatherDetails"}).find_next("tbody").find_all_next("tr")

    trs.pop(3)
    trs.pop(1)

    for tr in trs:
        data.append([])
        for td in tr:
            if type(td) == bs4.element.Tag:
                div = td.find('div')
                if div:
                    direction = str(div.get("data-tooltip"))
                    direction = direction.lower()
                    direction = direction.replace("північно", "пн")
                    direction = direction.replace("південно", "пд")
                    direction = direction.replace("північний", "пн")
                    direction = direction.replace("південний", "пд")
                    direction = direction.replace("західний", "зх")
                    direction = direction.replace("східний", "сх")
                    direction = direction.capitalize()
                    data[-1].append(direction)
                else:
                    data[-1].append(td.get_text())

    for i in range(0, len(data[0])):
        data[0][i] = data[0][i].replace(" ", "")
        data[3][i] += "%"
        data[4][i] = data[4][i].replace(" ", "")
        data[5][i] += "%"

    print(f"Час:\t\t" + "\t".join(data[0]))
    print(f"Температура:\t" + "\t".join(data[1]))
    print(f"Тиск:\t\t" + "\t".join(data[2]))
    print(f"Вологість:\t" + "\t".join(data[3]))
    print(f"Вітер:\t\t" + "\t".join(i[-6:] for i in data[4]))
    print(f"Напрямок:\t" + "\t".join(i[:5] if i[2] == '-' else i[:2] for i in data[4]))
    print(f"Опади:\t\t" + "\t".join(data[5]))


town = input("Уведіть місто (натисність Enter щоб обрати Київ): ")
if not town:
    town = "Київ"
day = input("Уведіть день: ")
month = input("Уведіть місяць: ")
year = input("Уведіть рік: ")
get_weather(get_html(town, year, month, day))