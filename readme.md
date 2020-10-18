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
```
# kali config
