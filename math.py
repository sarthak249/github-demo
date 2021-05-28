import re
import subprocess


def get_speaker_output_volume():
    
    process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = process.stdout.strip().decode('ascii')

    pattern = re.compile(r"output volume:(\d+), input volume:(\d+), "
                         r"alert volume:(\d+), output muted:(true|false)")
    volume, _, _, muted = pattern.match(output).groups()

    volume = int(volume)
    muted = (muted == 'true')
    print("Volume: ",volume)
    if muted==1:
        print("Volme is muted.")
    else:
        print("Volume is not muted.")
        

