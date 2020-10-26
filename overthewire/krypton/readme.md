# Krypton

## 0-1

```ssh
echo S1JZUFRPTklTR1JFQVQ= | base64 -d
```

## 1-2

```sh
cd /krypton/krypton1
cat *
echo YRIRY GJB CNFFJBEQ EBGGRA | tr 'A-Z' 'N-ZA-M' # rot13.
```

## 2-3

```sh
cd /krypton/krypton2/
cat README

mkdir /tmp/ben && cd /tmp/ben
chmod 777 .
ln -s /krypton/krypton2/keyfile.dat .
echo a > t
/krypton/krypton2/encrypt t
cat ciphertext # so our a turned into an M.

# turn M back to A and continue the pattern.
cat krypton3 | tr 'M-ZA-L' 'A-Z' # it is.

# bonus:
python -c 'print( ord("a")-ord("m") )' # -12.
# this means our decryption key is -12,
# and the encryption key is 12.
```

## 3-4

```sh
cd /krypton/krypton3
cat found* | vim -
:bn # switch from scratch pad.
%s/ //g # remove spaces.

# search for repeated trigraphs.
%s/TYV//gn # 5 matches
%s/JCB//gn # 14 matches, could be the.

vim found1 # and remove spaces.
%s/JCB//gn # 10 matches, promising.

# JCB positions:
  # 133, 166, 247, 407, 530, 579, 660, 797, 1083, 1206
  # not sure, let's try a more common digraph:
# DS positions:
  # 1, 57, 201, 246, 268, 272, 276, 320, 340, 348, 359
# DS distances
  # 56, 144, 45, 22, 4, 4, 44, 20, 8
  # lots of numbers divisible by 4, might be the key length
# create a vim macro to move one char to the right, then delete 3:
qqlxxxq
# repeat it a bunch
321@q # 1285 (chars in document) / 4
# use the resulting text to perform frequency analysis.
# 38 S (11.8%)
# 28 U
# 25 B

# S in ciphertext might be an E in plaintext (very close to the 12% expected for English)
```

* I just reread the instructions and it might just *not* be a Vigenère cipher
* pretty sure I just performed a manual Kasiski test for no reason

```sh
cat found* | tr -d ' ' | fold -w1 | sort | uniq -c | sort -gr # count occurences.
# I must say, I'm pretty proud of that oneliner.
#    456 S
#    340 Q
#    301 J
#    257 U
#    246 B
#    240 N
#    227 G
#    227 C
#    210 D
#    132 Z
#    130 V
#    129 W
#     86 M
#     84 Y
#     75 T
#     71 X
#     67 K
#     64 E
#     60 L
#     55 A
#     28 F
#     19 I
#     12 O
#      4 R
#      4 H
#      2 P
```
* `S` is still the most common, and `U` and `B` are not far behind.
* reading the instructions again, it's definitely a simple substitution cipher, oh well

```sh
# S -> E
# Q -> T
# J -> A
# U -> O
# B -> I
# N -> N
# G -> S

# ETAOINS, should be easy to remember.
# let's try that
cat krypton4 | tr -d ' ' | tr 'SQJUBNG' 'etaoins'
# KeVVWiseaDeVeIeVXiMnYtooKinWCoAnMae
# not quite readable yet.

# C -> R
# D -> H
# Z -> D
# V -> L
# W -> U
# M -> C
# Y -> M
# T -> F
# X -> Y

cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTX' 'etaoinsrhdlucmfy'
# KelluiseaheleIelyicnmtooKinuroAncae
# maybe a weird spelling of Louisiana

# I'm confident about e and ll is the most common digraph with the same two chars.
# assumem K -> W to complete the first word, K -> T or K -> H would work too
# but the respective frequencies make that less likely.

cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXK' 'etaoinsrhdlucmfyw'
# welluiseaheleIelyicnmtoowinuroAncae
# trigraph: `the` and `and` are very common. `the` is perfect because we are confident about e.

cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXK' 'etaoinsrhdlucmfyw' | grep [t,h,e] --color
# we have one potential match: `ahe` is less likely than `the` let's try that:

# switch A and T:
cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXK' 'eatoinsrhdlucmfyw'
# welluisetheleIelyicnmaoowinuroAncte

# let's highlight all the letters were we are reasonably sure about in red:
cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXK' 'eatoinsrhdlucmfyw'| grep --color [w,e,l,t,h]
# instead of adding color I'll remove the uncertain characters:
# well___ethele_el________w________te

# thele_el is probably `the level`
cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXKI' 'eatoinsrhdlucmfywv'| grep --color [w,e,l,t,h,v]
#  well___ethelevel________w________te

# well done?
cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXKI' 'eatiosnrhdldcmfywv'| \
  grep --color [w,e,l,t,h,v,d,o,n]
#  welldonethelevel_o______wo_d_____te

# we are on level three, they are probably talking about level `four`:
cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXKI' 'eatiornshdldumyfwv'| \
  grep --color [w,e,l,t,h,v,d,o,n,f,u,r]
# welldonethelevelfour____word___rute

# whichever word could the message be talking about? :D
cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXKI' 'eatsornihdldupyfwv'| \
  grep --color [w,e,l,t,h,v,d,o,n,f,u,r,p,a,s,i]
# welldonethelevelfourpasswordis_rute

# so close and yet so far!

# we could start guessing but we have other text to work with:
cat found1 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXKI' 'eatsornihdldupyfwv'| grep --color [A]
  # ... thealpha_etfor ...

# that looks like a b to me :D
cat krypton4 | tr -d ' ' | tr 'SQJUBNGCDYVWMYTXKIA' 'eatsornihdldupyfwvb'
# welldonethelevelfourpasswordisbrute

# nice, now all we have to do is uppercase it.
```

* http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/
