# coding=utf-8

import random

MAX_LEVEL = 4


def randomLevel():
    k = 1
    while random.randint(1, 100) % 2:
        k += 1
    k = min(k, MAX_LEVEL)
    return k


def traversal(skiplist):
    level = skiplist.level
    for current_level in range(0, level)[::-1]:
        level_str = 'header'
        current_node = skiplist.header
        while current_node:
            level_str += ' -> %s' % current_node.key
            current_node = current_node.forwards[current_level]
        print level_str


class Node(object):
    def __init__(self, level, key, value):
        self.key = key
        self.value = value
        self.forwards = [None] * level


class Skiplist(object):
    def __init__(self):
        self.level = 0
        self.header = Node(MAX_LEVEL, 0, 0)

    def insert(self, key, value):
        update = [None] * MAX_LEVEL
        current = self.header
        forward = None
        level = self.level
        for current_level in range(0, level)[::-1]:
            forward = current.forwards[current_level]
            while forward and forward.key < key:
                current = forward
                forward = current.forwards[current_level]
            update[current_level] = current
        if forward and forward.key == key:
            return False

        random_level = randomLevel()
        if random_level > self.level:
            for level in range(self.level, random_level):
                update[level] = self.header
            self.level = random_level

        forward = Node(random_level, key, value)
        for current_level in range(0, random_level):
            forward.forwards[current_level] = update[current_level].forwards[current_level]
            update[current_level].forwards[current_level] = forward

        return True

    def delete(self, key):
        update = [None] * MAX_LEVEL
        current = self.header
        forward = None
        level = self.level

        for current_level in range(0, level)[::-1]:
            forward = current.forwards[current_level]
            while forward and forward.key < key:
                current = forward
                forward = current.forwards[current_level]
            update[current_level] = current

        if forward and forward.key == key:
            for current_level in range(0, level):
                if update[current_level].forwards[current_level] == forward:
                    update[current_level].forwards[current_level] = forward.forwards[current_level]
            del forward
            for current_level in range(0, level)[::-1]:
                if not self.header.forwards[current_level]:
                    self.level -= 1
            return True
        else:
            return False

    def search(self, key):
        for current_level in range(0, self.level)[::-1]:
            forward = self.header.forwards[current_level]
            while forward and forward.key <= key:
                if forward.key == key:
                    return forward.key, forward.value, current_level
                forward = forward.forwards[current_level]
        return None

if __name__ == '__main__':
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    skiplist = Skiplist()
    for number in number_list:
        skiplist.insert(number, None)

    traversal(skiplist)
    print skiplist.search(4)
    skiplist.delete(4)
    traversal(skiplist)