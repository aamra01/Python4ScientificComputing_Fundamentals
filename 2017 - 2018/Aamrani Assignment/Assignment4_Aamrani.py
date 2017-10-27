import os
os.chdir("C:\Users\Rachid\Desktop\Assignment")
 
import Aamrani_Function as FC
WallComposition = {"WoodLapSiding":{"Rvalue":0.14,"length":0.013},"WoodFiberBoard":{"Rvalue":0.23,"length":0.013},
                   "GypsumWall":{"Rvalue":0.079,"length":0.013},"Inside":{"Rvalue":0.12},"Outside":{"Rvalue":0.030},
                   "GlassFiberInsulation":{"Rvalue":2.45,"length":0.090},"Brick":{"Rvalue":0.63,"length":0.100}}
 
DoorComposition = {"Outside":{"Rvalue":0.030},"Inside":{"Rvalue":0.12},"WoodComposition":{"Rvalue":0.44}}
 
RoofComposition = {"InsideTemperature":{"Rvalue":0.12},"MaltaGesso":{"Rvalue":0.069,"length":0.02},
                   "SolettaCalcestruzzo":{"Rvalue":0.1047,"length":0.20},"Outside":{"Rvalue":0.030},
                   "BarrieraBitume":{"Rvalue":0.0118,"length":0.002},"FibraVetro":{"Rvalue":1,"length":0.04},
                   "IntercapedineAria":{"Rvalue":0.16,"length":0.04},"CoperturaTegole":{"Rvalue":0.0101,"length":0.01}}
 
SerieWall = ["WoodLapSiding","WoodFiberBoard","GypsumWall","Inside","Outside","GlassFiberInsulation","Brick"]
SerieDoor = ["Outside","Inside","WoodComposition"]
SerieRoof = ["InsideTemperature","MaltaGesso","SolettaCalcestruzzo","Outside","BarrieraBitume","FibraVetro","IntercapedineAria","CoperturaTegole"]
ParallelWall = ["GlassFiberInsulation","WoodFiberBoard"]
FG = 0.70 #GlassFiberInsulation percentage
 
 
length = 20
width = 10
heigth = 2.4
 
R_series = FC.wallCalconlyInSeries(SerieWall,SerieDoor,SerieRoof,FG,WallComposition,DoorComposition,RoofComposition)
R_parallel = FC.wallCalc_onlyInParallel(ParallelWall,WallComposition)
R_Area = FC.Function(20,10,2.4)
 
 
WallComposition_1 = {"WoodLapSiding":{"Rvalue":0.14,"length":0.013},"WoodFiberSheeting":{"Rvalue":0.23,"length":0.013},
                   "GypsumWall":{"Rvalue":0.079,"length":0.013},"Inside":{"Rvalue":0.12},"Outside":{"Rvalue":0.030},
                   "GlassFiberInsulation":{"Rvalue":2.45,"length":0.025},"WoodStud":{"Rvalue":0.63,"length":0.090}}
                    
                    
SerieBetweenStud = ["WoodLapSiding","WoodFiberSheeting","GypsumWall","Inside","Outside","GlassFiberInsulation"]
SerieAtStud = ["WoodLapSiding","WoodFiberSheeting","GypsumWall","Inside","Outside","WoodStud"]
FractionGFI = 0.75 #GlassFiberInsulation percentage
 
import Aamrani_Function as FR
U_wall = FR.Results(SerieBetweenStud,SerieAtStud,FractionGFI,WallComposition_1)