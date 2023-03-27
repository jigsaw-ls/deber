import tkinter as tk
from tkinter import ttk
import pyshark

class NetworkSniffer:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Sniffer")

        # Treeview for packet details
        self.tree = ttk.Treeview(self.root, columns=("time", "src", "dst", "protocol", "info"))
        self.tree.heading("#0", text="No.")
        self.tree.heading("time", text="Time")
        self.tree.heading("src", text="Source")
        self.tree.heading("dst", text="Destination")
        self.tree.heading("protocol", text="Protocol")
        self.tree.heading("info", text="Info")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Capture packets
        self.capture = pyshark.LiveCapture(interface="wlxc4e98407a185", bpf_filter="tcp")
        self.capture.apply_on_packets(self.packet_callback)

    def packet_callback(self, packet):
        # Parse packet details
        no = packet.no
        time = packet.sniff_time
        src = packet.ip.src
        dst = packet.ip.dst
        protocol = packet.transport_layer
        info = packet.info

        # Insert packet details into treeview
        self.tree.insert("", "end", text=no, values=(time, src, dst, protocol, info))

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSniffer(root)
    root.mainloop()

