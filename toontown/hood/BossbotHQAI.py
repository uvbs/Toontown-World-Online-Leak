from CogHoodAI import CogHoodAI
from toontown.toonbase import ToontownGlobals
from toontown.suit.DistributedBossbotBossAI import DistributedBossbotBossAI
from toontown.building.DistributedBBElevatorAI import DistributedBBElevatorAI
from toontown.coghq.DistributedCogHQDoorAI import DistributedCogHQDoorAI
from toontown.coghq.DistributedCogKartAI import DistributedCogKartAI
from toontown.building import DoorTypes
from toontown.building import FADoorCodes
from toontown.suit import DistributedSuitPlannerAI
from toontown.building import DistributedBBElevatorAI
from toontown.building import FADoorCodes
from toontown.building.DistributedBoardingPartyAI import DistributedBoardingPartyAI
from toontown.coghq import DistributedCogKartAI
from toontown.suit import DistributedBossbotBossAI
from toontown.suit import DistributedSuitPlannerAI
from toontown.toonbase import ToontownGlobals
from toontown.building import DistributedBBElevatorAI
from toontown.building import FADoorCodes
from toontown.building.DistributedBoardingPartyAI import DistributedBoardingPartyAI
from toontown.coghq import DistributedCogKartAI
from toontown.suit import DistributedBossbotBossAI
from toontown.suit import DistributedSuitPlannerAI
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil
class BossbotHQAI(CogHoodAI):
    HOOD = ToontownGlobals.BossbotHQ

    def __init__(self, air, zoneId):
        CogHoodAI.__init__(self, air)
        self.karts = []
        self.createZone()
        self.suitPlanners = []
        self.zoneId = zoneId
        self.zoneId = ToontownGlobals.BossbotHQ
        zoneId = ToontownGlobals.BossbotHQ
        
        
    def createDoor(self):
        interiorDoor = DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, self.HOOD, doorIndex=0)
        exteriorDoor = DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, ToontownGlobals.BossbotLobby, doorIndex=0, lockValue=FADoorCodes.CB_DISGUISE_INCOMPLETE)
        exteriorDoor.setOtherDoor(interiorDoor)
        exteriorDoor.zoneId = self.HOOD
        exteriorDoor.generateWithRequired(self.HOOD)
        exteriorDoor.sendUpdate('setDoorIndex', [0])
        self.doors.append(exteriorDoor)

        interiorDoor.setOtherDoor(exteriorDoor)
        interiorDoor.zoneId = ToontownGlobals.BossbotLobby
        interiorDoor.generateWithRequired(ToontownGlobals.BossbotLobby)
        interiorDoor.sendUpdate('setDoorIndex', [0])
        self.doors.append(interiorDoor)
    
    def createKart(self, index, x, y, z, h, p, r, min):
        kart = DistributedCogKartAI(self.air, index, x, y, z, h, p, r, self.air.countryClubMgr, min)
        kart.generateWithRequired(self.HOOD)
        self.karts.append(kart)
        return kart
        self.suitPlanners = []
        
 
    def createZone(self):
        CogHoodAI.createZone(self)
        
        # Create lobby manager...
        self.createLobbyManager(DistributedBossbotBossAI, ToontownGlobals.BossbotLobby)
        self.createSuitPlanners()

        # Create CEO elevator.
        self.ceoElevator = self.createElevator(DistributedBBElevatorAI, self.lobbyMgr, ToontownGlobals.BossbotLobby, ToontownGlobals.BossbotLobby, boss=True)
        
        # Make our doors.
        self.createDoor()
        
        # Create Cog Golf Courses.
        kartPos = ((154.762, 37.169, 0), (141.403, -81.887, 0), (-48.44, 15.308, 0))
        hprList = ((110.815, 0, 0), (61.231, 0, 0), (-105.481, 0, 0))

        mins = ToontownGlobals.FactoryLaffMinimums[3]
        for i in range(3):
            x, y, z = kartPos[i]
            h, p, r = hprList[i]
            self.createKart(i, x, y, z, h, p, r, mins[i])

        # Create boarding groups
        # CEO Boarding Group
        self.createBoardingGroup(self.air, [self.ceoElevator.doId], ToontownGlobals.BossbotLobby, 8)

        # Cog Golf Boarding Group's
        kartIds = [kart.getDoId() for kart in self.karts]
        self.createBoardingGroup(self.air, kartIds, ToontownGlobals.BossbotHQ)

    def createSuitPlanners(self):
        suitPlanner = DistributedSuitPlannerAI.DistributedSuitPlannerAI(self.air, self.zoneId)
        suitPlanner.generateWithRequired(self.zoneId)
        suitPlanner.d_setZoneId(self.zoneId)
        suitPlanner.initTasks()
        self.suitPlanners.append(suitPlanner)
        self.air.suitPlanners[self.zoneId] = suitPlanner
