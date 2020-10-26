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

* `echo BfMYroe26WYalil77FoDi9qh59eK5xNr | openssl s_client -connect localhost:30001 -ign_eof`
  * `-ign_eof` ignores end of file and keeps connection open for reply

## 16-17

```sh
# fast:
nc localhost -vvz 31000-32000 2>&1 | grep -v refused
for p in 31960 31790 31691 31518 31046; do echo test | nc -vw1 localhost $p; done

# or slower but less work:
nmap -sV localhost -p31000-32000 | grep -v echo # filter out echo servers.

# per usual:
echo cluFn7wTiGryunymYOu4RcffSxQluehd | openssl s_client -connect localhost:31790 -ign_eof

# save sshkey to sshkey17
ssh bandit17@bandit.labs.overthewire.org -p 2220 -i sshkey17
```

## 17-18

```sh
# unlike diff, git diff also shows the filenames, so we can use wildcards
# without thinking about which filename will be globbed first:
git diff --no-index passwords.*
```

## 18-19

```sh
sshpass -p 'kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd' \
  ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme 2>/dev/null
```

## 19-20

```sh
ls -Alp
./bandit20-do cat /etc/bandit_pass/bandit20
```

---

* out of interest, try to exfiltrate that binary via base64 and the tmux-clipboard:
  * run `tmux` in host and connect to bandit19
    * make sure we run tmux in vi mode: `^b`, `:setw mode-keys vi`
  * `base64 bandit20-do` to print encoded version of binary
  * `^b`+`[`, `k`, `V`, select everything with `^u` and `hjkl`
  * exit out of bandit19
  * open nvim and enter insert mode
  * paste tmux clipboard with `^b`+`]`
  * save file as `bandit20-do.b64` and decode it with `base64 -d bandit20-do.b64 > bandit20-do`
  * `file bandit*` looks like it worked
  * look at how it works with Radare2: `r2 bandit20-do`
    * `aaa;Vpp`, `g main`, `hjkl`
      * `0x080484b7      e894feffff     call sym.imp.execv`
        * `execv` syscall with `"/usr/bin/env"` string
          * https://stackoverflow.com/questions/20823371/what-is-the-difference-between-the-functions-of-the-exec-family-of-system-calls/20823401
  * `execv` honors the set-uid bit
  * `ls -lp`: `-rwsr-x--- 1 bandit20 bandit19 7296 May  7 20:14 bandit20-do`
    * `s` = `setuid + x`
    * `S` = `setuid`
* to find all binaries with the suid bit set: `find / -perm -4000 2>/dev/null`

## 20-21

* let's poke at it: `r2 suconnect`
  * it reads the password from a file, no access :(

* to background an SSH session:
  * `enter`, `~`, `^z`
  * possible escape sequences: `enter`, `~`, `?`

```sh
echo GbKksEFF4yrVs6il55v6gwY5aVje5f0j | nc -lp 5000&
./suconnect 5000
```

## 21-22

```sh
ls -Alp /etc/cron.d/
cat /etc/cron.d/cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

## 22-23

```sh
ls -Alp /etc/cron.d
cat /etc/cron.d/cronjob_bandit23 # runs as: bandit23
cat /usr/bin/cronjob_bandit23.sh
cat /tmp/$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)
```
