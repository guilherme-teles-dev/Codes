from math import copysign
loop = True
def sign(num):
    return copysign(1, num)
peak = 0
while loop:
    waveform = int(input())
    if waveform == 0:
        loop = False
    if loop == True:
        samples = [waveform]
        samples = list(map(int, input().split()))
        lastsample = ''
        lastlastsample = ''
        for sample in samples:
            if lastsample == '':
                samplelast = sample
            else:
                if lastlastsample == '':
                    lastlastsample = lastsample
                    lastsample = sample
                else:
                    rate = lastsample - lastlastsample
                    if sign(sample-lastsample) != sign(rate):
                        peak += 1
