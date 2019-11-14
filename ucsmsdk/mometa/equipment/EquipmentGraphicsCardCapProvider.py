"""This module contains the general information for EquipmentGraphicsCardCapProvider ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentGraphicsCardCapProviderConsts:
    DELETED_FALSE = "false"
    DELETED_NO = "no"
    DELETED_TRUE = "true"
    DELETED_YES = "yes"
    DEPRECATED_FALSE = "false"
    DEPRECATED_NO = "no"
    DEPRECATED_TRUE = "true"
    DEPRECATED_YES = "yes"
    MODE_CHANGE_SUPPORTED_FALSE = "false"
    MODE_CHANGE_SUPPORTED_NO = "no"
    MODE_CHANGE_SUPPORTED_TRUE = "true"
    MODE_CHANGE_SUPPORTED_YES = "yes"


class EquipmentGraphicsCardCapProvider(ManagedObject):
    """This is EquipmentGraphicsCardCapProvider class."""

    consts = EquipmentGraphicsCardCapProviderConsts()
    naming_props = set([u'vendor', u'model', u'revision'])

    mo_meta = MoMeta("EquipmentGraphicsCardCapProvider", "equipmentGraphicsCardCapProvider", "manufacturer-[vendor]-model-[model]-revision-[revision]", VersionMeta.Version213a, "InputOutput", 0x1ff, [], [""], [u'capabilityCatalogue', u'equipmentHwCapDerivativeProvider'], [u'equipmentFruVariant', u'equipmentManufacturingDef', u'equipmentPciDef', u'equipmentPhysicalDef', u'equipmentPicture', u'equipmentServiceDef', u'equipmentSlotArrayRef', u'firmwareType', u'firmwareUpgradeConstraint'], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version213a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []),
        "deleted": MoPropertyMeta("deleted", "deleted", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "deprecated": MoPropertyMeta("deprecated", "deprecated", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []),
        "element_load_failures": MoPropertyMeta("element_load_failures", "elementLoadFailures", "uint", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "elements_loaded": MoPropertyMeta("elements_loaded", "elementsLoaded", "uint", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "gencount": MoPropertyMeta("gencount", "gencount", "uint", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], ["0-4294967295"]),
        "load_errors": MoPropertyMeta("load_errors", "loadErrors", "uint", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "load_warnings": MoPropertyMeta("load_warnings", "loadWarnings", "uint", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "mgmt_plane_ver": MoPropertyMeta("mgmt_plane_ver", "mgmtPlaneVer", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "mode_change_supported": MoPropertyMeta("mode_change_supported", "modeChangeSupported", "string", VersionMeta.Version321d, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []),
        "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version213a, MoPropertyMeta.NAMING, 0x8, 1, 510, None, [], []),
        "num_gpu": MoPropertyMeta("num_gpu", "numGpu", "uint", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
        "prom_card_type": MoPropertyMeta("prom_card_type", "promCardType", "ushort", VersionMeta.Version213a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, [], []),
        "revision": MoPropertyMeta("revision", "revision", "string", VersionMeta.Version213a, MoPropertyMeta.NAMING, 0x20, 1, 510, None, [], []),
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version213a, MoPropertyMeta.READ_ONLY, 0x40, 0, 256, None, [], []),
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []),
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version213a, MoPropertyMeta.READ_WRITE, 0x80, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []),
        "stepping": MoPropertyMeta("stepping", "stepping", "string", VersionMeta.Version224b, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
        "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version213a, MoPropertyMeta.NAMING, 0x100, 1, 510, None, [], []),
    }

    prop_map = {
        "childAction": "child_action", 
        "deleted": "deleted", 
        "deprecated": "deprecated", 
        "dn": "dn", 
        "elementLoadFailures": "element_load_failures", 
        "elementsLoaded": "elements_loaded", 
        "gencount": "gencount", 
        "loadErrors": "load_errors", 
        "loadWarnings": "load_warnings", 
        "mgmtPlaneVer": "mgmt_plane_ver", 
        "modeChangeSupported": "mode_change_supported", 
        "model": "model", 
        "numGpu": "num_gpu", 
        "promCardType": "prom_card_type", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "stepping": "stepping", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, vendor, model, revision, **kwargs):
        self._dirty_mask = 0
        self.vendor = vendor
        self.model = model
        self.revision = revision
        self.child_action = None
        self.deleted = None
        self.deprecated = None
        self.element_load_failures = None
        self.elements_loaded = None
        self.gencount = None
        self.load_errors = None
        self.load_warnings = None
        self.mgmt_plane_ver = None
        self.mode_change_supported = None
        self.num_gpu = None
        self.prom_card_type = None
        self.sacl = None
        self.status = None
        self.stepping = None

        ManagedObject.__init__(self, "EquipmentGraphicsCardCapProvider", parent_mo_or_dn, **kwargs)
