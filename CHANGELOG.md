# Changelog

## 0.2.5 (2023-06-20)

### Changed
- Changed so that the program can work in Windows that lacks SIGALRM (untested).
- The program exits with an appropriate error code depending on the error.
- Interpreting command-line arguments in own function.
- Strip whitespace from the output of the command run.
- Updated description for option shell.

### Removed
- Removed encoding declarations.
- Removed the function validate_weekday as it was not needed.

## 0.2.4 (2023-06-11)

### Added
- Option shell.
- Option no-check.
- Option timeout.

### Changed
- Error messages are printed to stderr.
- Exit with error code 1 when the user aborts with Ctrl-C.
- Updated the code to be PEP8 compliant.

## 0.1.0 (2023-06-03)

### Initial release
