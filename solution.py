import re
import string

REPLACED_DICT = {}
REPLACED = string.ascii_letters + string.digits + "-.~_"
for s in REPLACED:
    REPLACED_DICT["%" + hex(ord(s))[2:]] = s
PORTS = {
    "http": ":80"
}


def lower(url):
    return str(url).lower()


def upper_percent(url):
    for el in re.findall(r"%\w\w", url):
        url = url.replace(el, el.upper())
    return url


def replace_percent(url):
    for el in re.findall(r"%\w\w", url):
        if el in REPLACED_DICT.keys():
            url = url.replace(el, REPLACED_DICT[el])
    return url


def remove_port(url):
    for prot, port in PORTS.items():
        if re.match(prot + r".+" + port, url):
            url = url.replace(port, "")
    return url


def remove_dots(url):
    els = url.split("/")
    res = []
    for el in els:
        if el == '.':
            continue
        elif el == '..':
            res = res[:-1]
        else:
            res.append(el)
    return "/".join(res)


def checkio(url):
    url = lower(url)
    url = remove_port(url)
    url = replace_percent(url)
    url = lower(url)
    url = remove_dots(url)
    url = upper_percent(url)
    return url

print(checkio("Http://Www.Checkio.org"))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Http://Www.Checkio.org") == \
        "http://www.checkio.org", "1st rule"
    assert checkio("http://www.checkio.org/%cc%b1bac") == \
        "http://www.checkio.org/%CC%B1bac", "2nd rule"
    assert checkio("http://www.checkio.org/task%5F%31") == \
        "http://www.checkio.org/task_1", "3rd rule"
    assert checkio("http://www.checkio.org:80/home/") == \
        "http://www.checkio.org/home/", "4th rule"
    assert checkio("http://www.checkio.org/task/./1/../2/././name") == \
        "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')
