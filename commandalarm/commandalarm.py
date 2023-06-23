#!/usr/bin/env python3
# commandalarm.py
# Copyright (C) 2023 alofgren <drelofren@outlook.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
""" Set an alarm with a custom command. """

import argparse
import datetime
import errno
import subprocess
import sys
import threading
import time
from . import __version__

# pylint: disable=W0603
ALARM_FIRED = False


def alarm_handler():
    """
    Handle the alarm signal.

    Returns:
    None
    """
    global ALARM_FIRED
    ALARM_FIRED = True


def set_alarm(time_str, day):
    """
    Set an alarm for a specific time and day of the week.

    Parameters:
    time_str (str): The time in the format HH:MM:SS.
    day (int): The day of the week, where Monday is 1 and Sunday is 7.

    Returns:
    threading.Timer: A Timer object that will execute the
                    alarm_handler function after the specified time.

    Raises:
    ValueError: If the time_str is not in the format HH:MM:SS
               or if day is not an integer between 1 and 7.
    """
    try:
        time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
    except ValueError as value_err:
        raise ValueError(
            "time_str must be in the format HH:MM:SS") from value_err
    if not isinstance(day, int) or day < 1 or day > 7:
        raise ValueError("day must be an integer between 1 and 7")
    date_obj = datetime.date.today()
    days_ahead = day - date_obj.isoweekday()
    if days_ahead < 0 or (days_ahead == 0
                          and datetime.datetime.now().time() > time_obj):
        days_ahead += 7
    date_obj += datetime.timedelta(days=days_ahead)
    alarm_datetime = datetime.datetime.combine(date_obj, time_obj)
    seconds_until_alarm = int(
        round((alarm_datetime - datetime.datetime.now()).total_seconds()))
    if seconds_until_alarm <= 0:
        seconds_until_alarm = 1
    print(f"Alarm set for {alarm_datetime}")
    return threading.Timer(seconds_until_alarm, alarm_handler)


def valid_time_string(time_str):
    """
    Validates that the time string is in the correct format.

    Parameters:
    time_str (str): The time in the format HH:MM:SS.

    Returns:
    str: The time string if it is valid.

    Raises:
    argparse.ArgumentTypeError: If the time string is not in the
                               correct format.
    """
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
        return time_str
    except ValueError as value_err:
        raise argparse.ArgumentTypeError(
            f"{time_str} is not a valid time in the format HH:MM:SS"
        ) from value_err


def parse_arguments():
    """
    Parse command line arguments.

    Returns:
    argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(
        prog="commandalarm",
        description="Set an alarm with a custom command.")
    parser.add_argument("time",
                        type=valid_time_string,
                        help="the time in the format HH:MM:SS")
    parser.add_argument("command", type=str, help="the command to run")
    parser.add_argument("argument",
                        default=None,
                        type=str,
                        nargs="*",
                        help="the arguments to the command")
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument(
        "-d",
        "--day",
        default=datetime.date.today().isoweekday(),
        type=int,
        help="the day of the week as an integer from 1 to 7",
        choices=range(1, 8))
    parser.add_argument("-r",
                        "--repeat",
                        action="store_true",
                        help="repeat forever")
    parser.add_argument("-s",
                        "--shell",
                        action="store_true",
                        default=False,
                        help="run command in a shell")
    parser.add_argument("-n",
                        "--no-check",
                        action="store_false",
                        default=True,
                        help="don't check the command return code",
                        dest="check")
    parser.add_argument("-t",
                        "--timeout",
                        default=None,
                        type=int,
                        help="timeout in seconds for the command to complete")
    return parser.parse_args()


def main():
    """
    The main function that parses command-line arguments, sets the
    alarm and runs the command.
    """
    global ALARM_FIRED
    args = parse_arguments()
    try:
        timer = set_alarm(args.time, args.day)
        timer.start()
        while True:
            while not ALARM_FIRED:
                try:
                    timer.join()
                except RuntimeError:
                    print("Error: Could not join timer thread",
                          file=sys.stderr)
                    sys.exit(1)
            command_str = f"{args.command} {' '.join(args.argument)}"
            command = (command_str if args.shell else
                       [args.command] + args.argument)
            print("Time is up!")
            print("Running command:", command_str)
            try:
                result = subprocess.run(command,
                                        capture_output=True,
                                        shell=args.shell,
                                        timeout=args.timeout,
                                        check=args.check,
                                        text=True)
                print(result.stdout.strip())
            except FileNotFoundError:
                print("Command not found", file=sys.stderr)
                sys.exit(errno.ENOENT)
            except subprocess.CalledProcessError as called_process_err:
                print(f"Command returned non-zero exit status "
                      f"{called_process_err.returncode}", file=sys.stderr)
                print(f"stderr: {called_process_err.stderr}", file=sys.stderr)
                sys.exit(called_process_err.returncode)
            except PermissionError as permission_err:
                print(f"Permission error: {permission_err}", file=sys.stderr)
                sys.exit(errno.EACCES)
            except subprocess.TimeoutExpired as timeout_expired:
                print(f"Command timed out after "
                      f"{timeout_expired.timeout} seconds",
                      file=sys.stderr)
                sys.exit(errno.ETIME)
            if args.repeat:
                ALARM_FIRED = False
                time.sleep(1)
                timer = set_alarm(args.time, args.day)
                timer.start()
            else:
                break
    except KeyboardInterrupt:
        print("Alarm stopped manually.", file=sys.stderr)
        timer.cancel()
        timer.join()
        sys.exit(1)


if __name__ == "__main__":
    main()
