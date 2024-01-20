#!/usr/bin/python
# -*- coding: utf8 -*-


import requstProcessing
import hashingDelete


def count_test():

    right_answers = [75, 356, 55, 28]
    input_data = [
        "https://ru.pinterest.com/AllChai_/dreamcore/",
        "https://ru.pinterest.com/AllChai_/%D0%B1%D0%B0%D0%BB%D1%8C%D0%B7%D0%B0%D0%BC-%D0%BD%D0%B0-%D0%B4%D1%83%D1%88%D1%83/",
        "https://ru.pinterest.com/AllChai_/%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD/",
        "https://ru.pinterest.com/AllChai_/%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%D1%8B-%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B5%D0%B9%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0/"
    ]
    program_answers = []
    for data in input_data:
        response = requstProcessing.get_request(url=data)
        answer = requstProcessing.pinCount(response=response[0])
        program_answers.append(answer[0])
    score = 0
    for index, value in enumerate(program_answers):
        if int(value) == int(right_answers[index]):
            score += 1

    return score, len(right_answers)

def boardId_test():
    right_answers = ["629659660342228024", "629659660342230758", "629659660342228048", "629659660342228029"]
    input_data = [
        "https://ru.pinterest.com/AllChai_/dreamcore/",
        "https://ru.pinterest.com/AllChai_/%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD/",
        "https://ru.pinterest.com/AllChai_/%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%D1%8B-%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B5%D0%B9%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0/",
        "https://ru.pinterest.com/AllChai_/%D0%B1%D0%B0%D0%BB%D1%8C%D0%B7%D0%B0%D0%BC-%D0%BD%D0%B0-%D0%B4%D1%83%D1%88%D1%83/"
    ]
    program_answers = []
    for data in input_data:
        response = requstProcessing.get_request(url=data)
        answer = requstProcessing.boardID(response=response[0])
        program_answers.append(answer[0])
    score = 0
    for index, value in enumerate(program_answers):
        if int(value) == int(right_answers[index]):
            score += 1

    return score, len(right_answers)


def hash_test():
    input_data = "D:/all/all packs/Code/Python/Для коледжа/Pinloader/New realization/for hashtest"
    right_answers = [
        'a910d9b0e989ef664b8f8f101b5c0946', '235d9ff1b00e45710dfb99ad99557d35',
        '0c6818c5ed6e88b7c4f8bb2ebb163164', 'c20d1f89f2819490d6bf7aa7020d10f8'
    ]

    hash_list = hashingDelete.create_hash(path=input_data)
    score = 0
    for index, value in enumerate(hash_list[0]):
        if value == right_answers[index]:
            score += 1

    return score, len(right_answers)

def testing():
    total_score = 0
    total_length = 0
    score, length = count_test()
    total_score += score
    total_length += length
    print(f"COUNT TEST: {score}/{length}")
    score, length = boardId_test()
    total_score += score
    total_length += length
    print(f"BOARDID TEST: {score}/{length}")
    score, length = hash_test()
    total_score += score
    total_length += length
    print(f"HASH TEST: {score}/{length}")
    print(f"TOTAL SCORE: {total_score}/{total_length}")

testing()
