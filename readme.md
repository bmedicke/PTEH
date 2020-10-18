# PT𓀮EH

# toc


## enumeration

## foothold

## priviledge escalation

```sh
id
ps -p $$
ip a # ifconfig
lsblk
netstat -tulpen
```

```sh
cd /opt
python3 -m http.server 80
```

```sh
./linpeas.sh -a
```

## oneliners

```sh
# upgrade shell:
python -c 'import pyt;pty.spawn("bash")'

# fix environment:
export TERM=linux

# listen for incoming connection:
nc -nvlp 1234

# logging a reverse shell locally:
script # stop with ^D. breaks in vi.

# get a temp dir:
cd $(mktemp -d)

# get local connections:
netstat -tulpen
```

# kali config

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

* ranger disables previews for root (enable them on a by case basis with `zp`)
