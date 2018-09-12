# Author: Franz Weidmann
# The Ryu-Controller collects flow statistics from specific ports of the OpenVSwitch
# and saves them in json format for further processing

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller import dpset
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0

import threading
import time

class reporter(threading.Thread):
   def __init__(self, threadID, reporterFunc, event, ports):
      self._reporterFunc = reporterFunc
      self._event = event
      self._ports = ports
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = "Reporter"

   def run(self):
      print("Starting " + self.name +  " thread")

      while True:
         for port in self._ports:
            self._reporterFunc(self._event.dp, port.id)

         time.sleep(5)

      print("Exiting " + self.name)

class port():
   def __init__(self, id):
      self.id = id
      self.txPacks = 0
      self.rxPacks = 0
      self.txBytes = 0
      self.rxBytes = 0
      self.txDropped = 0
      self.rxDropped = 0

class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
       super(L2Switch, self).__init__(*args, **kwargs)
       self.ports = [port(2), port(3), port(4)]


    # reply event for port stats of an VSwitch
    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def portStatsReply(self, event):
        stats = event.msg.body[0]
        self.saveStatsToPort(stats)

    # enter/leave event for a VSwitch
    @set_ev_cls(dpset.EventDP, MAIN_DISPATCHER)
    def onSwitch(self, event):
        #print("NEW SWITCH", event.enter, event.dp.id, event.ports)
        self.reporterThread = reporter(1, self.reqPortStats, event, self.ports)
        self.reporterThread.start()

    # sends a request to an VSwitch for port stats
    def reqPortStats(self, dp, portNr):
        req = dp.ofproto_parser.OFPPortStatsRequest(dp, 0, portNr)
        dp.send_msg(req)

    #  new OpenFlow message from VSwitch
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        console.log(ev.dp.id)

    # save new stats to json file
    def saveStatsToJSON(self, port):
       print("Saving to JSON")

    # extracts stats from stats message and updates port stats instance
    def saveStatsToPort(self, stats):
       port = list(filter(lambda port: port.id == stats.port_no, self.ports))[0]
       if port == None:
         print("No port instance for this port number", stats.port_no) 
         return

       print("PORT STATS", stats.port_no, stats.tx_packets-port.txPacks, stats.tx_bytes-port.txBytes, stats.tx_dropped-port.txDropped)
       port.txPacks = stats.tx_packets
       port.rxPacks = stats.rx_packets
       port.txBytes = stats.tx_bytes
       port.rxBytes = stats.rx_bytes
       port.txDropped = stats.tx_dropped
       port.rxDropped = stats.rx_dropped
       self.saveStatsToJSON(port)
