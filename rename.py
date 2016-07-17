#!/usr/bin/env python

import sys;
import os;
import string;

def rename(path, pattern):
    os.chdir(path);
    file_list = os.listdir(os.getcwd());
    
    dot_index = pattern.rfind('.');
    pre = pattern[:dot_index];
    suf = pattern[dot_index:];
    
    file_cnt = len(file_list);
    num_len = 3;
    if file_cnt > 100:
        num_len = 4;
    if file_cnt > 1000:
        num_len = 5;
    
    gen_num = 1;
    for file_item in file_list:
        name = pre + '-' + string.zfill(str(gen_num), num_len) + suf;
        os.rename(file_item, name);
        print (file_item + '=>' + name);
        gen_num += 1;

def prompt():
    print 'rename.py [path] newfilename';

def main():
    if (len(sys.argv) == 3):
        path = sys.argv[1];
        pattern = sys.argv[2];
    elif (len(sys.argv) == 2):
        path = os.getcwd();
        pattern = sys.argv[0];
    else:
        prompt();
        sys.exit();
    confirm = raw_input('comfirm(y|n)');
    if (confirm != 'y'):
        sys.exit();
    rename(path, pattern);

if __name__ == '__main__':
    main();
