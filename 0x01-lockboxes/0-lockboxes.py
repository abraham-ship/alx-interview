#!/usr/bin/env python3
'''method to determine if all boxes can be opened'''


def canUnlockAll(boxes):
    '''function to determine if box can be opened'''
    visited = set()

    def dfs(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited and key < len(boxes):
                dfs(key)

    dfs(0)
    return len(visited) == len(boxes)
