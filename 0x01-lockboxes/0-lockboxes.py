#!/usr/bin/python3
"""Lockboxes."""

def canUnlockAll(boxes):
        """Check if all boxes can be opened
        Args:
                boxes (list): List which contain all the boxes with the keys
        Returns:
                bool: True if all boxes can be opened, otherwise, False
        """
        if not boxes:
                return False
        if len(boxes) == 1:
                return True
        keys = [0]
        for key in keys:
                for box in boxes[key]:
                        if box not in keys and box < len(boxes):
                                keys.append(box)
        if len(keys) == len(boxes):
                return True
        return False
