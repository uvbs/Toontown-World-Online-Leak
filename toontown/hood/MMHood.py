from pandac.PandaModules import *
import ToonHood
from toontown.town import MMTownLoader
from toontown.safezone import MMSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *

class MMHood(ToonHood.ToonHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = MinniesMelodyland
        self.townLoaderClass = MMTownLoader.MMTownLoader
        self.safeZoneLoaderClass = MMSafeZoneLoader.MMSafeZoneLoader
        self.storageDNAFile = 'phase_6/dna/storage_MM.xml'
        self.holidayStorageDNADict = {WINTER_DECORATIONS: ['phase_6/dna/winter_storage_MM.xml'],
         WACKY_WINTER_DECORATIONS: ['phase_6/dna/winter_storage_MM.xml'],
         HALLOWEEN_PROPS: ['phase_6/dna/halloween_props_storage_MM.xml'],
         SPOOKY_PROPS: ['phase_6/dna/halloween_props_storage_MM.xml']}
        self.skyFile = 'phase_6/models/props/MM_sky'
        self.spookySkyFile = 'phase_6/models/props/MM_sky'
        self.titleColor = (1.0, 0.5, 0.5, 1.0)

    def load(self):
        ToonHood.ToonHood.load(self)
        self.parentFSM.getStateNamed('MMHood').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('MMHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload(self)

    def enter(self, *args):
        ToonHood.ToonHood.enter(self, *args)

    def exit(self):
        ToonHood.ToonHood.exit(self)
