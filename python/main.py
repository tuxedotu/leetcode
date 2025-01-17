from typing import List
import numpy as np
from numpy import fft


def romanToIn(s: str) -> int:
    s = s.upper()
    lastLiteral = None
    retVal = 0

    for literal in s:
        if literal == "I":
            retVal += 1
        elif literal == "V":
            retVal += 5 if lastLiteral != "I" else 3
        elif literal == "X":
            retVal += 10 if lastLiteral != "I" else 8
        elif literal == "L":
            retVal += 50 if lastLiteral != "X" else 30
        elif literal == "C":
            retVal += 100 if lastLiteral != "X" else 80
        elif literal == "D":
            retVal += 500 if lastLiteral != "C" else 300
        elif literal == "M":
            retVal += 1000 if lastLiteral != "C" else 800
        lastLiteral = literal
    return retVal


def twoSum(nums: List[int], target: int) -> List[int]:
    retIdx = [0, 1]

    while retIdx[0] < len(nums):
        retIdx[1] = retIdx[0] + 1
        while retIdx[1] < len(nums):
            if nums[retIdx[0]] + nums[retIdx[1]] == target:
                return retIdx
            else:
                retIdx[1] += 1
        retIdx[0] += 1

    return []


def longestCommonPrefix(strs: List[str]) -> str:
    retStr = ""
    currCharI = 0
    cmpStrI = 1

    while currCharI < len(strs[0]):
        while cmpStrI < len(strs):
            if strs[cmpStrI][currCharI] != strs[0][currCharI]:
                return retStr
            elif len(retStr) == currCharI and cmpStrI == len(strs)-1:
                retStr += strs[0][currCharI]
            cmpStrI += 1
        currCharI += 1
        cmpStrI = 0

    return retStr


def isValid(s: str) -> bool:
    openPairs = ""
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in s:
        if char in pairs.values():
            openPairs += char
        elif char in pairs.keys():
            if pairs[char] == openPairs[len(openPairs)-1]:
                openPairs = openPairs[:-1]
            else:
                return False
        else:
            return False
    return True


def findOccurrences(text: str, first: str, second: str) -> List[str]:
    text = text.split(' ')  # convert 'text' to array of words
    currOcc = -1
    retStrs = []

    if first not in text or second not in text:
        return []

    for i, word in enumerate(text):
        if word == first:
            currOcc = i
            if text[currOcc+1] and text[currOcc+1] == second:
                if text[currOcc+2]:
                    retStrs.append(text[currOcc+2])

    return retStrs


def numTilePossibilities(tiles: str) -> int:
    # TODO: could be a fun problem
    # <url> https://leetcode.com/problems/letter-tile-possibilities/
    return 0


# FUNCTION CALLS GO HERE #
print(numTilePossibilities("AAB"))
# print(findOcurrences(
#     text="we will we will rock you",
#     first="we",
#     second="will")
# )
# print(isValid("[]"))
# print(isValid("[]"))
# print(longestCommonPrefix(["a", "apple", "ar"]))
# print(twoSum([3,3], 6))
# print(f"LVIII: {romanToIn("LVIII")}")
