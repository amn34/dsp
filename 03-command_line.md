# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

---

1. pushd/popd: puts paths on a stack and takes them off in reverse order for quicker moving around between directories
2. touch: makes new file
3. cp: copies first file into second file/directory, e.g. cd newfile.txt otherdir/
4. mv: move/rename files, e.g. mv newfile ~/Documents/newnamedfile (moves to new dir and renames)
5. less: shows file content one page at a time (v. cat, which shows all content w no paging; also, cat > file.txt writes input to file [then C-d])
6. rm: removes files/directories; with -rf recursively deletes contents of dir so dir w files can be rm'd
7. |, >, >>: sends output from left file/program to right file/program; writes output; appends output
8. find: "find STARTDIR -name WILDCARD -print", e.g. "find . -name "*.txt" -print
9. export: set env variable, e.g. export VAR="1"; unset removes variable
10. chmod, chown: changes permissions, owner to files and directories

---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

---

**`ls` lists contents in the currect directory. **

The -a flag lists all files, including hidden ones.
The -l flag gives the long format including the file type, permissions, owner, size, mod date, etc.
the -lh flag combines -l and -h to give the long format with size in human-readable format (e.g. 1.1K)

-h is meaningless without -l since -a does not give file sizes. Therefore `ls-al` l gives all files, including hidden ones, in long format, and `ls -alh` gives all files including hidden ones in long format with human-readable sizes.

---

What does `xargs` do? Give an example of how to use it.

---

**`xargs` executes commands over a given input. For example, you could pass the output of `find` to `xargs` and perform some action on the found files.**

    find . -name "*.txt" | xargs rm   #removes found files
    find . -name "*.txt" | xargs grep "hello" #looks for string 'hello' in found files
    
* Use -print0 and -0 options to find and run commands on files with whitespace in name
