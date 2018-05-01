#! /usr/bin/env python
# 22-read-from-file
#
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
# and count how many of each “category” of each image there are. This text file is actually a list of files
# corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for
# the images. Once you take a look at the first line or two of the file, it will be clear which part
# represents the scene category. To do this, you’re going to have to remember a bit about string
# parsing in Python 3. I talked a little bit about it in this post.
#
# /a/abbey/sun_arxtvfkkycnqhfkj.jpg


def count_categories(name_category, categories):
    # if categories is None:
    #    categories = dict()

    if name_category in categories:
        categories[name_category] += 1
    else:
        categories[name_category] = 0

    return categories


def main():
    count_mother_category = dict()
    count_sub_category = dict()

    with open("22-extra-1.txt", "r") as file:
        while True:
            actual_line = file.readline()

            if not actual_line:
                break

            splitted_line = actual_line.split("/")  # 0:empty, 1: mother category, 2: subcategory, 3: sun image

            count_mother_category = count_categories(splitted_line[1], count_mother_category)
            count_sub_category = count_categories(splitted_line[2], count_sub_category)

    print("Mother categories:")
    for category, count in count_mother_category.items():
        print(str(category) + " : " + str(count))

    print("Sub categories:")
    for subcategory, subcount in count_sub_category.items():
        print(str(subcategory) + " : " + str(subcount))


if __name__ == '__main__':
    main()


