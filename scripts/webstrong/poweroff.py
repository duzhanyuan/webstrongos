import os
import sys

before_sd = 'echo WebStrongOS 1.3 && echo'
sd_params = ''
time = 'now'


def shutdown(params):
    def find_param(i):
        global before_sd
        global sd_params
        global time

        if params[i] == '-u':
            before_sd += ' && apt update && apt upgrade -y && apt autoremove -y'
        elif params[i] == '-r':
            sd_params += ' -r'
        elif params[i] == '-t':
            custom_time = i + 1
            time = params[custom_time]
        elif params[i] == '-h':
            help()

    for i in range(len(params)):
        find_param(i)

    # print 'sudo -- su -c "'"{} && shutdown{} -h {}"'"'.format(before_sd, sd_params, time)
    os.system('sudo -- su -c "'"{} && shutdown{} {}"'"'.format(before_sd, sd_params, time))
    exit(0)


def help():
    help_info = '\n\e[1mList of available params:\e[0m\n\n' \
                '  -u --> Run apt update and upgrade before shutdown\n' \
                '  -r --> Reboot system before shutdown\n' \
                '  -t [TIME] --> Set time to shutdown\n\n' \
                'Created by WebStrong'
    os.system('echo "{}"'.format(help_info))
    exit(0)


shutdown(sys.argv)
