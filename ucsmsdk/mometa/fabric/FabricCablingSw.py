"""This module contains the general information for FabricCablingSw ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class FabricCablingSwConsts:
    ID_A = "A"
    ID_B = "B"
    ID_NONE = "NONE"


class FabricCablingSw(ManagedObject):
    """This is FabricCablingSw class."""

    consts = FabricCablingSwConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("FabricCablingSw", "fabricCablingSw", "[id]", VersionMeta.Version311e, "InputOutput", 0x7f, [], ["admin", "ext-lan-config", "ext-lan-policy", "ext-san-config", "ext-san-policy"], [u'fabricCabling'], [u'fabricBreakout'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version311e, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version311e, MoPropertyMeta.NAMING, 0x8, None, None, None, ["A", "B", "NONE"], []),
        "locale": MoPropertyMeta("locale", "locale", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|server|chassis|internal|external),){0,5}(defaultValue|unknown|server|chassis|internal|external){0,1}""", [], []),
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version311e, MoPropertyMeta.CREATE_ONLY, 0x10, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, 0x20, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version311e, MoPropertyMeta.READ_WRITE, 0x40, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "transport": MoPropertyMeta("transport", "transport", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|ether|dce|fc),){0,4}(defaultValue|unknown|ether|dce|fc){0,1}""", [], []),
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version311e, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|unknown|lan|san|ipc),){0,4}(defaultValue|unknown|lan|san|ipc){0,1}""", [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "locale": "locale", 
        "name": "name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "transport": "transport", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.locale = None
        self.name = None
        self.sacl = None
        self.status = None
        self.transport = None
        self.type = None

        ManagedObject.__init__(self, "FabricCablingSw", parent_mo_or_dn, **kwargs)
