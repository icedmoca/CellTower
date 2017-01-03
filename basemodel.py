def Arnold(NSector=3,NPApSec=2,PTX=40,uPA=0.35,PSP=31.25,Cc=0.27,CPSBB=0.11):
    PBSMacro = NSector*NPApSec*(PTX/uPA +PSP)*(1+Cc)*(1+CPSBB)
    return(PBSMacro)
