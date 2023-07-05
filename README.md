# CommandAlarm

CommandAlarm is a simple command line program that allows users to set an alarm with a custom command. 

## Installation

To install CommandAlarm, you can use [pip](https://pip.pypa.io/en/stable/):

```bash
pip install commandalarm
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/alofgren/commandalarm.git
cd commandalarm
pip install .
```

## Usage Output

```
usage: commandalarm [-h] [-v] [-d {1,2,3,4,5,6,7}] [-r] [-s] [-n] [-t TIMEOUT] time command [argument ...]

Set an alarm with a custom command.

positional arguments:
  time                  the time in the format HH:MM:SS
  command               the command to run
  argument              the arguments to the command

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d {1,2,3,4,5,6,7}, --day {1,2,3,4,5,6,7}
                        the day of the week as an integer from 1 to 7
  -r, --repeat          repeat forever
  -s, --shell           run command in a shell
  -n, --no-check        don't check the command return code
  -t TIMEOUT, --timeout TIMEOUT
                        timeout in seconds for the command to complete
```

## Examples

To set an alarm for 2:00 PM and play a sound when the alarm goes off:
```bash
commandalarm 14:00:00 aplay alarm_sound.wav
```

To set an alarm for 9:15 AM on Wednesday to run a Python script with a timeout of 30 seconds: 
```bash
commandalarm 09:15:00 --day 3 --timeout 30 python3 script.py
```

To run a command in a shell, use the -s or --shell option:
```bash
commandalarm 16:00:00 --shell 'ENV_VAR="I am running in a shell"; echo $ENV_VAR'
```

To disable further option processing, use two hyphens ("--") before the command:
```bash
commandalarm 16:00:00 -- ls -l
```

## Contributing

If you would like to contribute to CommandAlarm, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/alofgren/commandalarm).

## License

CommandAlarm is licensed under the [GPL License](https://github.com/alofgren/commandalarm/blob/main/LICENSE).
