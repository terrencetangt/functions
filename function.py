#Content
#A. Math Functions
#B. String Functions
#C. Date and Time Functions
#D. Operating Systems
#E. Data Functions
#F. Image Functions


#A. Math Functions
#No. of Digits
def no_digit(n):
    return len(str(n))

#palindrome number
def palindrome(n):
    s=str(n)
    l = len(s)-1
    for i in range(l):
        if s[i] != s[l-i]:
            return False
    return True

#determine if it is a prime
def isprime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#Sieve of Eratosthenes of generating primes
def SieveOfEratosthenes(n):
    primes = []
    primeb = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primeb[p] == True):
            for i in range(p * 2, n + 1, p):
                primeb[i] = False
        p += 1
    primeb[0]= False
    primeb[1]= False
    for p in range(n + 1):
        if primeb[p]:
            primes.append(p)
    return tuple(primes)

#return all prime factors list of a number
def prime_factors(n):
    factor = []
    i = 2
    while n > 1:
        while n % i == 0:
            factor.append(i)
            n = n / i
        i += 1
    return factor

#return all distinct prime factors list of a number
def distinct_prime_factors(n):
    factor = []
    i = 2
    while n > 1:
        while n % i == 0:
            if i not in factor:
                factor.append(i)
            n = n / i
        i += 1
    return factor

#Euler's totient function
def euler_totient(n):
    factor = distinct_prime_factors(n)
    p = n
    for i in range(len(factor)):
        p = int(p * (1 - 1/factor[i]))
    return p

#Factorial
def fact(n):
    import math
    return math.factorial(n)

#is permutation or not
def ispermutate(a: str, b: str):
    if len(a) != len(b):
        return False
    a_list = []
    b_list = []
    for i in range(len(a)):
        a_list.append(a[i])
        b_list.append(b[i])
    a_list.sort()
    b_list.sort()
    for i in range(len(a)):
        if a_list[i] != b_list[i]:
            return False
    return True

#Return a list of permutation
def permutations(pattern):
    from itertools import permutations
    return list(permutations(pattern))

#next permutation
def perm_next(a):
    #Step 1
    p = -1
    for k in range(len(a)-1):
        if a[k] < a[k+1]:
            p = k
    if p == -1:
        return []
    v = -1
    for l in range(p,len(a)):
        if a[p] < a[l]:
            v = l
    if v >= 0:
        t = a[p]
        a[p] = a[v]
        a[v] = t
    for i in range(int((len(a) - p - 1) / 2)):
        t = a[p +1+ i]
        a[p+1+i] = a[len(a) - i-1]
        a[len(a) - i-1] = t
    return a

#greatest common divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#B. String Functions
# replace 1 string with another string
def string_replace(string, oldvalue, newvalue):
    return string.replace(oldvalue, newvalue)
# return all splitting combination of a string
def combos(str):
  yield (str,)
  for i in range(1, len(str)):
    for c in combos(str[i:]):
      yield (str[:i],) + c

#convert txt file into string
def txt_file_to_str(path):
    file = open(path)
    s = file.read()
    file.close()
    return s

#by looping each line
def textfile_to_str(path):
    file = open(path, "r")
    s = ""
    for line in file:
        s += line
    file.close()
    return s

def textfile_to_str_list(path):
    file = open(path,"r")
    list = file.readlines()
    file.close()
    return list

#write strings to a file
def write_txt(s, path):
    file = open(path, "w")
    file.write(s)

#read text from a url
def read_url_txt(url):
    import urllib.request
    file = urllib.request.urlopen(url)
    s = ""
    for line in file:
    	s = s + line.decode()
    return s

#read csv from a path
def read_csv_file(path):
    import pandas as pd
    return pd.read_csv(path)

#sorted the dictionary by value
def dict_sorted_by_value(dictionary, decending = False):
    new_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=decending))
    return new_dict

#plot histogram
def plot_histogram(column, title):
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.distplot(column, kde = False, bins=10).set_title(title)
    plt.show()

#dictionary_count
def dict_freq_count(freq_table: dict, key):
    if key not in freq_table:
        freq_table[key] = 1
    else:
        freq_table[key] += 1

#calculate word frequency
def cal_word_freq(txt_file):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
    "for", "in", "not", "would", "there", "than", "one", "those", "on", "so", "may", "only", "must", "many", "upon", \
    "us", "could","these", "even", "much", "into", "other", "without", "should", "every", "most", "own", "cannot", \
    "while"]

    # MAIN CODE START HERE
    frequency = {}
    words = txt_file.split()
    for word in words:
        word = word.lower()
        if word.isalpha() == False:
            for p in punctuations:
                word = word.replace(p,"")
                if word.isalpha == True:
                    break
        if word.isalpha() == True:
            if word not in uninteresting_words:
                if word not in frequency:
                    frequency[word] = 1
                else:
                    frequency[word] += 1

    sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1]))
    return sorted_frequency
    #wordcloud
    # cloud = wordcloud.WordCloud()
    # cloud.generate_from_frequencies(frequency)
    # return cloud.to_array()

#Regular Expression
#https://docs.python.org/3/library/re.html
#search text by regex
def regex_search(regex, text):
    import re
    return re.search(regex,text)

#find all pattern in text by regex
def regex_findall(regex, text):
    import re
    return re.findall(regex, text)

#Split the text into list
def regex_split(regex, text):
    import re
    return re.split(regex, text)

#replace the word in the text
def regex_sub(regex, replace_word, text):
    import re
    return re.sub(regex, replace_word, text)

#C. Date and Time Functions
#ruturn current time in float
def now():
    import time
    return time.time()

#print the process time of a function (without parameters)
def time_function(function):
    from timeit import timeit
    msg = "The running time is "
    second = timeit(function, number = 1)
    if second < 60:
        print(msg + "{} seconds.".format(second))
    elif second > 60:
        minute = int((second % 60 ** 2) // 60)
        second = second % 60
        print(msg + "{} minutes and {} seconds".format(minute, second))
    elif second > 60 ** 2:
        hour = int(second // (60 ** 2))
        second = second % 60
        print(msg + "{} hours {} minutes and {} seconds".format(hour, minute, second))

#D. Operating Systems
#check harddisk usage
def check_disk_usage(disk):
    import shutil
    return shutil.disk_usage(disk)

#remove file
def remove_file(path):
    import os
    os.remove(path)

#rename file
def rename_file(pathname, new_pathname):
    import os
    os.rename(pathname, new_pathname)

#check if the path exists or not
def path_exists(path):
    import os
    return os.path.exists(path)

#return the size of the path
def getfilesize(path):
    import os
    return os.path.getsize(path)

#return the modify time value of the path
def modify_time(path):
    import os
    return os.path.getmtime(path)

#return the absolute path of the file
def abs_path(path):
    import os
    return os.path.abspath(path)

#return the current directory
def current_directory():
    import os
    return os.getcwd()

#create a new Directory
def create_directory(name_directory):
    import os
    os.mkdir(name_directory)

#change the current directory:
def change_directory(name_directory):
    import os
    os.chdir(name_directory)

#remove empty directory
def remove_directory(name_directory):
    import os
    os.rmdir(name_directory)

#determine if it is a directory
def is_directory(path):
    import os
    return os.path.isdir(path)

#return the file list of a directory
def directory_list(path):
    import os
    return os.listdir(path)
#def check_cpu_usage():

#E. Data Functions
#linear serach
def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

#binary serach
def binary_search(sorted_list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

#print the csv (List)
def print_csv(path):
    import csv
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

#return the csv file into dictionary

#F. Image Functions
#Return image
def image(path):
    from PIL import Image
    im = Image.open(path)
    return im

def image_resize(path, new_path, horizontal, vertical)
    from PIL import Image
    im = Image.open(path)
    new_im = im.resize((horizontal, vertical))
    new_im.save(new_path)
