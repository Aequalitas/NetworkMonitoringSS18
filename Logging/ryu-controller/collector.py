# Author: Franz Weidmann
# The Ryu-Controller collects flow statistics from specific ports of the OpenVSwitch
# and saves them in json format for further processing

from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller import dpset
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0

class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)

        self.reqPortStats(event.dp, 2)
        self.reqPortStats(event.dp, 3)
        self.reqPortStats(event.dp, 4)

    # reply event for port stats of an VSwitch
    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def portStatsReply(self, event):
        stats = event.msg.body[0]
        print("NEW PORT STATS")
        print(stats.port_no, stats.tx_packets)

    # enter/leave event for a VSwitch
    @set_ev_cls(dpset.EventDP, MAIN_DISPATCHER)
    def onSwitch(self, event):
        print(event.enter, event.dp.id, event.ports)

    # sends a request to an VSwitch for port stats
    def reqPortStats(self, dp, portNr):
        req = dp.ofproto_parser.OFPPortStatsRequest(dp, 0, portNr)
        dp.send_msg(req)

    #  new OpenFlow message from VSwitch
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):