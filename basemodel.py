def Arnold(NSector,NPApSec,PTX,uPA,PSP,Cc,CPSBB):
    PBSMacro = NSector*NPApSec*(PTX/uPA +PSP)*(1+Cc)*(1+CPSBB)
    return(PBSMacro)
