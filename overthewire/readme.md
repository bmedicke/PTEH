# OverTheWire wargames

# Bandit

## 1-2

* file named `-`, content is password
* `-` is interpreted by many programs as `stdin`/`stdout`
* `cat -` uses stdin instead of file
* [`cat ./-` works!](https://unix.stackexchange.com/questions/16357/usage-of-dash-in-place-of-a-filename)

## 4-5

* one human readable file and a bunch of binary files
* `find inhere -type f -exec file {} \;`
* `reset` to fix messed up terminal

## 5-6

* `find inhere/ -size 1033c -type f ! -executable -exec sh -c 'file {} | grep ASCII' \;`

## 6-7

* `find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null  `

## 7-8

* `grep millionth data.txt | awk '{printf $2}'`

## 8-9

* `sort data.txt | uniq -u # print only unique lines.`

## 9-10

* `strings data.txt | grep ===`

## 10-11

* `base64 -d data.txt`

## 11-12

* `cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M' # rot13.`

## 12-13

```sh
mkdir /tmp/ben && cd /tmp/ben
xxd -r ~/data.txt > zip
file zip # gzip
mv zip z.gz; gunzip z.gz; ls
file z # bzip
bunzip z; ls
file z.out # gzip
mv z.out z.gz
gunzip z.gz;ls
file z # POSIX tar
tar xf z;ls
file data5.bin # POSIX tar
tar xf data5.bin; ls
file data6.bin # bzip2
bunzip2 data6.bin; ls
file data6.bin # gzip2
bunzip2 data6.bin; ls
file data6.bin.out # POSIX tar
tar xf data6.bin.out; ls
file data8.bin # gzip
mv data8.bin d.gz; gunzip d.gz;ls
file d # ASCII, finally :D
cat d # this was hell.
```

## 13-14

* `ssh bandit14@bandit.labs.overthewire.org -p 2220 -i sshkey14`

## 14-15

* in bandit14:
* `cat /etc/bandit_pass/bandit14 | nc localhost 30000`

## 15-16
