# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import string
#
s = u'Tôi yêu Machine Machine Learning'

print('- string.ascii_letters = %s' % string.ascii_letters)         # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print('- string.ascii_lowercase = %s' % string.ascii_lowercase)     # abcdefghijklmnopqrstuvwxyz
print('- string.ascii_uppercase = %s' % string.ascii_uppercase)

print('- string.digits = %s' % string.digits)                       # 0123456789
print('- string.hexdigits = %s' % string.hexdigits)                 # 0123456789abcdefABCDEF
print('- string.octdigits = %s' % string.octdigits)                 # 01234567

print('- string.punctuation = %s' % string.punctuation)             # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print('- string.printable = %s' % string.printable)                 # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print('- string.whitespace = %s' % string.whitespace)               # space, tab, linefeed, return, formfeed, and vertical tab.

# print('- string.letter = %s' % string.letters)                      # 2.X - abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print('- string.lowercase = %s' % string.lowercase)                 # 2.X - abcdefghijklmnopqrstuvwxyz
# print('- string.uppercase = %s' % string.uppercase)                 # 2.X - ABCDEFGHIJKLMNOPQRSTUVWXYZ

print('- s.capitalize() = %s' % s.capitalize())
print('- s.casefold() = %s' % s.casefold())
print('- s.center() = %s' % s.center(34, '1'))
print('- s.count() = %s' % s.count('Tôi'))
print('- s.encode() = %s' % s.encode())
print('- s.endswith() = %s' % s.endswith('Machine', 0, 15))
print('- s.find() = %s' % s.find('Machine', 0, 15))
print('- s.rfind() = %s' % s.rfind('Machine'))
print('- s.index() = %s' % s.index('yêu', 0, 10))

