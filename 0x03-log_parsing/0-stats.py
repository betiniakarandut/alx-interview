#!/usr/bin/python3
"""
A module for parsing HTTP request logs.
"""
import re


class LogParser:
    def __init__(self):
        self.total_file_size = 0
        self.status_codes_stats = {"200": 0, "301": 0, "400": 0,
                                   "401": 0, "403": 0, "404": 0,
                                   "405": 0, "500": 0}

    def extract_input(self, input_line):
        """
        Extracts sections of a line of an HTTP request log
        """
        log_format = (
            r'\s*(?P<ip>\S+)\s*',
            r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
            r'\s*"(?P<request>[^"]*)"\s*',
            r'\s*(?P<status_code>\S+)',
            r'\s*(?P<file_size>\d+)'
        )
        log_fmt = '{}\\-{}{}{}{}\\s*'.format(*log_format)
        resp_match = re.fullmatch(log_fmt, input_line)
        info = {
            "status_code": 0,
            "file_size": 0,
        }
        if resp_match:
            info["status_code"] = resp_match.group("status_code")
            info["file_size"] = int(resp_match.group("file_size"))
        return info

    def print_statistics(self):
        """
        Prints the build-up statistics of the HTTP request log
        """
        print("File size: {:d}".format(self.total_file_size), flush=True)
        for status_code, num in sorted(self.status_codes_stats.items()):
            if num > 0:
                print("{:s}: {:d}".format(status_code, num), flush=True)

    def update_metrics(self, line):
        """
        Updates the metrics from a given HTTP request log
        Args:
            line (str): Keyboard input from which to retrieve the metrics
        """
        line_info = self.extract_input(line)
        status_code = line_info.get("status_code", "0")
        if status_code in self.status_codes_stats:
            self.status_codes_stats[status_code] += 1
        self.total_file_size += line_info["file_size"]

    def run(self):
        """
        Testing the log parser
        """
        line_num = 0
        try:
            while True:
                line = input()
                self.update_metrics(line)
                line_num += 1
                if line_num % 10 == 0:
                    self.print_statistics()
        except (KeyboardInterrupt, EOFError):
            self.print_statistics()


if __name__ == "__main__":
    parser = LogParser()
    parser.run()
