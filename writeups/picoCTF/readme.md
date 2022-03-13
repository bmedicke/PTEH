# picoCTF


<!-- vim-markdown-toc GFM -->

* [resources](#resources)
* [primer.picoctf](#primerpicoctf)

<!-- vim-markdown-toc -->

# resources

* https://explainshell.com/
* https://gchq.github.io/CyberChef/
* https://play.picoctf.org/practice
* http://docs.pwntools.com/en/stable/
* https://primer.picoctf.com/

# primer.picoctf

```sh
less README.md
vim `which usage` # nice python script.
```

* [Git Tower CLI cheatsheet](https://www.git-tower.com/blog/command-line-cheat-sheet/)
  * `ctrl-u` delete left of cursor
  * `ctrl-k` delete  right  of cursor

```sh
gdb ./a.out
break main
run
disas /r
# or:
gdb -batch -ex 'file ./a.out ' -ex 'disassemble win'
```
