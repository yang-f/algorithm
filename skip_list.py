# coding=utf-8

import random

MAX_LEVEL = 4


def randomLevel():
    k = 1
    while random.randint(1, 100) % 2:
        k += 1
    k = k if k < MAX_LEVEL else MAX_LEVEL
    return k


def traversal(skiplist):
    level = skiplist.level
    current_level = level - 1
    while current_level >= 0:
        level_str = 'header'
        current_node = skiplist.header
        while current_node:
            level_str += ' -> %s' % current_node.key
            current_node = current_node.forwards[current_level]
        print level_str
        current_level -= 1


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
        current_level = level - 1
        while current_level >= 0:
            forward = current.forwards[current_level]
            while forward and forward.key < key:
                current = forward
                forward = current.forwards[current_level]
            update[current_level] = current
            current_level -= 1
        if forward and forward.key == key:
            return False

        random_level = randomLevel()
        if random_level > self.level:
            level = self.level
            while level < random_level:
                update[level] = self.header
                level += 1
            self.level = random_level

        forward = Node(random_level, key, value)
        current_level = 0
        while current_level < random_level:
            forward.forwards[current_level] = update[current_level].forwards[current_level]
            update[current_level].forwards[current_level] = forward
            current_level += 1

        return True

    def delete(self, key):
        update = [None] * MAX_LEVEL
        current = self.header
        forward = None
        level = self.level
        current_level = level - 1

        while current_level >= 0:
            forward = current.forwards[current_level]
            while forward and forward.key < key:
                current = forward
                forward = current.forwards[current_level]
            update[current_level] = current
            current_level -= 1
        if forward and forward.key == key:
            current_level = 0
            while current_level < self.level:
                if update[current_level].forwards[current_level] == forward:
                    update[current_level].forwards[current_level] = forward.forwards[current_level]
                current_level += 1
            del forward
            current_level = self.level - 1
            while current_level >= 0:
                if not self.header.forwards[current_level]:
                    self.level -= 1
                current_level -= 1
            return True
        else:
            return False

    def search(self, key):
        current_level = self.level - 1
        while current_level >= 0:
            forward = self.header.forwards[current_level]
            while forward and forward.key <= key:
                if forward.key == key:
                    return forward.key, forward.value, current_level
                forward = forward.forwards[current_level]
            current_level -= 1
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