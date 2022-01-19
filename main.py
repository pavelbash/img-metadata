from os.path import getmtime, isdir
import os
import re
import time

def main():
    workdir = r"D:\Паша\фото"
    regex = r".*(?P<date>\d\d[.](?P<year>\d\d\d\d)).*"
    global result
    result = []

    for directory in os.walk(workdir):
        if re.match(regex, directory[0]):
            date = re.match(regex, directory[0]).group('date')
            year = re.match(regex, directory[0]).group('year')
            pics = [i for i in directory[2] if re.match(".*(avi|mov|jpg|mp4)$", i.lower())]
            for pic in pics:
                pic = directory[0] + '\\' + pic
                t = getmtime(pic)
                timestamp = time.strftime("%d.%m.%Y", time.gmtime(t))
                if year < timestamp[6:]:
                    # print(year, timestamp[6:], sep=":")
                    date_epoch = int(time.mktime(time.strptime(date, "%m.%Y")))
                    result.append((pic, timestamp, t, date, date_epoch))

    with open("D:\Паша\анализ фото.csv", "w", encoding='utf-8') as f:
        f.write('\ufeff')
        for line in result:
            f.write(",".join([line[0].replace(',',''), line[1], str(line[2]), line[3], str(line[4])]) + "\n")
            os.utime(line[0], (line[4], line[4]))


if __name__ == '__main__':
    main()


