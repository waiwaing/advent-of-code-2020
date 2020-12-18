import regex


def main():
    input = []
    with open("input.txt") as f:
        input = [x.strip() for x in f if x.strip() != ""]

    t = "^(.*) bags contain (((\\d) ([\\D]*) bags?)(, )?)*"
    parsed = [regex.match(t, x) for x in input]

    mapping = {}

    for bag in parsed:
        color = bag.group(1)
        children = bag.captures(5)
        children_count = [int(x) for x in bag.captures(4)]

        mapping[color] = []

        for i in range(0, len(children_count)):
            for j in range(0, children_count[i]):
                mapping[color].append(children[i])

    include = 0
    for key in mapping:
        queue = set(mapping[key])
        all_colors = set()
        while len(queue) > 0:
            this_color = queue.pop()
            all_colors.add(this_color)
            queue.update(mapping[this_color])

        if "shiny gold" in all_colors:
            include += 1

    print(include)

    bag_count = 0
    queue = list(mapping["shiny gold"])
    while(len(queue) > 0):
        current_bag = queue.pop()
        queue.extend(mapping[current_bag])
        bag_count += 1

    print(bag_count)


main()
