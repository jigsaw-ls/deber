import pyshark

capture = pyshark.LiveCapture(interface='wlxc4e98407a185')
capture.sniff(timeout=10)

for packet in capture:
    print(packet)
