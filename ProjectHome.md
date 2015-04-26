'baubau' is a multithreaded backup tool written in python.

It aims to create a backup of all unrecoverable files which either don't belong to any package or have been modified.

The logic behind it is fairly simple:

  1. the main loop walks the file-system searching for files
  1. a second thread checks whether the file belongs to a package (using information from rpmdb)
  1. if the file belongs to a package, a third thread compares it against the rpm database (size and eventually md5 checksum)
  1. all modified files and new files are listed to a file (and packed into a tar archive on the fly if requested)

To avoid including unnecessary files and thus saving space, baubau uses regexp expressions to force the exclusion or inclusion of certain files (for instance media, log and lock files are excluded in /etc/baubau/exclude\_files).

Generally speaking, the resulting archive will typically contain all files which cannot be restored by simply reinstalling packages. For instance:

  * your home directory
  * all the configuration files you have modified
  * your log files

baubau will create a directory in your home directory (-d to specify the directory):

```
[root@navid-laptop ~]# ls -l /root/baubau-20070313-131511
total 1892
-rw-r--r-- 1 root root       0 Mar 13 13:15 excluded_files
-rw-r--r-- 1 root root     278 Mar 13 13:15 excluded_files_regexp
-rw-r--r-- 1 root root       0 Mar 13 13:15 excluded_pkg_files
-rw-r--r-- 1 root root 1900544 Mar 13 13:15 included_files
-rw-r--r-- 1 root root       0 Mar 13 13:15 included_files_regexp
-rw-r--r-- 1 root root   25425 Mar 13 13:15 rpm-qa
```

This directory will also be included in the tar-ball archive if you decide to let baubau create one for you (-z option).

Ideally, in order to fully restore from backup all you have to do is reinstall the rpm packages and then extract the archive produced by 'baubau' over the root file-system.