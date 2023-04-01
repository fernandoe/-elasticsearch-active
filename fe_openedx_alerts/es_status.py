#!/usr/bin/env python


def get_current_status(fixed_str=None):
    if fixed_str == 'ok':
        with open("./es-status-ok.txt", "r") as result:
            return result.read()
    elif fixed_str == 'ko':
        with open("./es-status-not-ok.txt", "r") as result:
            return result.read()
    return ''


def execute():
    output = get_current_status('ko')
    print(output)
    if 'Active: active (running)' in output:
        print('BOMBOU')
    else:
        print('nao funcionou')


if __name__ == '__main__':
    execute()

