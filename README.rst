========================
A Drupal file mover tool
========================

Synopsis
--------
Move uploaded files between Drupal ``sites/*/files`` (sub)directories,
updating all references in database.
This actually doesn't do any operations itself, but generates a bunch of
``mv`` commands and ``sql`` statements which can be applied to the filesystem
and the database.

Similar solutions
-----------------
- https://drupal.org/sandbox/aasarava/1712322
- https://drupal.org/project/media_mover
- https://drupal.org/project/uploadedfilesmover
- https://drupal.org/project/file_maintenance
- http://www.midwesternmac.com/blogs/geerlingguy/moving-your-drupal-files-folder-dev-live-sites
