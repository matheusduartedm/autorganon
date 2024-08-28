#=
Esse código irá ler os cenários de geração/demanda do SDDP e escrever o arquivo .scd a ser lido pelo Organon. Essa leitura do SDDP será feita via PsrClasses
=#
#Pacotes

#Entradas PC Pessoal
PSRClasses = "D:\\psrclassesinterfacejulia\\"
PATH_CASE  = "D:\\Google Drive\\ufrj\\TCC\\02-Base_Dados\\02-Base_SDDP\\"

#Entradas PC PSR=#
#=Path       = "D:\\Google Drive\\ufrj\\TCC\\04-Repositorio\\data\\"
PSRClasses = "D:\\psrclassesinterfacejulia\\"
PATH_CASE  = "D:\\Google Drive\\ufrj\\TCC\\02-Base_Dados\\02-Base_SDDP\\"
PATH_CASE  = "D:\\BASES\\DRef_WPescadero_GD\\"=#

# ------Parte 1 - Inicialização padrão SDDP------------------------------------
        #PATH_CASE = Path

        PATH_PSRCLASSES = PSRClasses #caminho com o PSR_Classes
        include(string(PATH_PSRCLASSES,"psrclasses.jl")) #Inclui as definicoes do modulo PSRClasses
        PSRClasses_init(PATH_PSRCLASSES) #Inicializa a DLL do PSRClasses

        ilog = PSRManagerLog_getInstance(0) #Configura Gerenciador de Log
        PSRManagerLog_initPortuguese(ilog) #Inicializa idioma portugues para log
        ilogcons = PSRLogSimpleConsole_create(0) #Acrescenta Log do Tipo Console Simples ao Gerenciador (log na tela)
        PSRManagerLog_addLog(ilog, ilogcons)
        igmsk  = PSRManagerIOMask_getInstance(0)#Configura Gerenciador de Mascaras e carrega Mascaras
        iret = PSRManagerIOMask_importFile(igmsk, string(PATH_PSRCLASSES,"Masks_SDDP_V10.2.pmk"))
        iret = PSRManagerIOMask_importFile(igmsk, string(PATH_PSRCLASSES,"Masks_SDDP_V10.3.pmk"))
        iret = PSRManagerIOMask_importFile(igmsk, string(PATH_PSRCLASSES,"Masks_SDDP_Blocks.pmk"))
        igmdl = PSRManagerModels_getInstance(0)#Configura Gerenciador de Modelos e carrega Modelos
        iret = PSRManagerModels_importFile(igmdl, string(PATH_PSRCLASSES,"Models_SDDP_V10.2.pmd"))
        iret = PSRManagerModels_importFile(igmdl, string(PATH_PSRCLASSES,"Models_SDDP_V10.3.pmd"))

#-------Parte 2 - Carrega estudo da base SDDP-----------------------------------
        istdy = PSRStudy_create(0)#Cria Estudo
        iosddp = PSRIOSDDP_create(0)#Cria Objeto Leitor de Estudo SDDP e carrega dados
        iret = PSRIOSDDP_load(iosddp, istdy, PATH_CASE, PATH_CASE, PSR_SDDP_VERSION_14)

#-------Parte 3 - Obtem lista de entidades desejadas----------------------------
#       Obtem lista de usinas do estudo
        lstsys = PSRStudy_getCollectionSystems(istdy)
        lsthyd = PSRStudy_getCollectionPlants(istdy, PSR_PLANTTYPE_HYDRO)
        lstter = PSRStudy_getCollectionPlants(istdy, PSR_PLANTTYPE_THERMAL)
        lstgnd = PSRStudy_getCollectionPlants(istdy, PSR_PLANTTYPE_GND)
        lstdem = PSRStudy_getCollectionDemands(istdy)
        #lstbus = PSRStudy_getCollectionBuses(istdy)

#       Obtem total de sistemas e usinas associadas
        nsys     = PSRCollectionElement_maxElements(lstsys)
        nhydro   = PSRCollectionElement_maxElements(lsthyd)
        nthermal = PSRCollectionElement_maxElements(lstter)
        ngnd     = PSRCollectionElement_maxElements(lstgnd)
        #nbus     = PSRCollectionElement_maxElements(lstbus)
        ndem     = PSRCollectionElement_maxElements(lstdem)

#       Obtem informações do estudo
        stages = PSRStudy_getNumberStages(istdy)
        blocks = PSRStudy_getNumberBlocks(istdy)
        scenarios=PSRStudy_getNumberSimulations(istdy)

        systemNameAux = allocstring(nsys,12)
        thermNameAux  = allocstring(nthermal, 12)
        hydroNameAux  = allocstring(nhydro, 12)
        gndNameAux    = allocstring(ngnd, 12)
        #busNameAux    = allocstring(nbus,12)
        demNameAux    = allocstring(ndem,12)

        ipthermsys = Array(Int32, nthermal)
        PSRCollectionElement_mapRelationShip(lstter, lstsys, ipthermsys, PSR_RELATIONSHIP_1TO1, false )

        iphydrosys = Array(Int32, nhydro)
        PSRCollectionElement_mapRelationShip(lsthyd, lstsys, iphydrosys, PSR_RELATIONSHIP_1TO1, false )

        ipgndsys = Array(Int32, ngnd)
        PSRCollectionElement_mapRelationShip(lstgnd, lstsys, ipgndsys, PSR_RELATIONSHIP_1TO1, false )

        ipdemsys = Array(Int32, ndem)
        PSRCollectionElement_mapRelationShip(lstdem, lstsys, ipdemsys, PSR_RELATIONSHIP_1TO1, false )

        #ipbusger = Array(Int32, nthermal)
        #PSRCollectionElement_mapRelationShip(lstter, lstbus, ipbusger, PSR_RELATIONSHIP_1TO1, false )

        imapsys = PSRMapData_create(0)
        PSRMapData_addElements(imapsys, lstsys)
        PSRMapData_mapParm(imapsys, "name", systemNameAux, 12)

        imapter = PSRMapData_create(0)
        PSRMapData_addElements(imapter, lstter)
        PSRMapData_mapParm(imapter, "name", thermNameAux, 12)

        imaphydro = PSRMapData_create(0)
        PSRMapData_addElements(imaphydro, lsthyd)
        PSRMapData_mapParm(imaphydro, "name", hydroNameAux, 12)

        imapgnd = PSRMapData_create(0)
        PSRMapData_addElements(imapgnd, lstgnd)
        PSRMapData_mapParm(imapgnd, "name", gndNameAux, 12)

        imapdem = PSRMapData_create(0)
        PSRMapData_addElements(imapdem, lstdem)
        PSRMapData_mapParm(imapdem, "name", demNameAux, 12)

        #imapbus = PSRMapData_create(0)
        #PSRMapData_addElements(imapbus, lstbus)
        #PSRMapData_mapParm(imapbus, "name", busNameAux, 12)


        PSRMapData_pullToMemory(imapsys)
        systemName = splitstring(systemNameAux,12)

        PSRMapData_pullToMemory(imapter)
        thermName = splitstring(thermNameAux,12)

        PSRMapData_pullToMemory(imaphydro)
        hydroName = splitstring(hydroNameAux,12)

        PSRMapData_pullToMemory(imapgnd)
        gndName = splitstring(gndNameAux,12)

        PSRMapData_pullToMemory(imapdem)
        demName = splitstring(demNameAux,12)

        #PSRMapData_pullToMemory(imapbus)
        #busName = splitstring(busNameAux,12)

#-------Parte 4 - Obtem informacoes dos arquivos binarios de geracao-------------------------------
#       Usinas Termicas
        dimthermal = stages*blocks*scenarios*nthermal
        gerthermal = read(PATH_CASE*"gerterMW.bin",Float32, dimthermal)

#       Usinas Hidros
        dimhydro = stages*blocks*scenarios*nhydro
        gerhydro = read(PATH_CASE*"gerhid.bin",Float32, dimhydro)

#       Usinas GNDs
        dimgnd = stages*blocks*scenarios*ngnd
        gergnd = read(PATH_CASE*"gergnd.bin",Float32, dimgnd)

#       Demanda
        dimdem = stages*blocks*scenarios*nsys
        totdem = read(PATH_CASE*"demamw.bin",Float32, dimdem)

#       Duracao dos Blocos
        dimdur = stages*blocks*scenarios
        duracao = read(PATH_CASE*"duraci.bin",Float32, dimdur)
scd = """REF 00:00, 24:00, "9bus.ntw" """

#--------------Num estudo, puramente térmico-------------------------------------------
vtherm = collect(1:nthermal)
dictThermName = Dict(thermName[i] => vtherm[i] for i=1:nthermal)
a = DictGerBus[thermName[t]]
DictBusTherm = Dict("1"=>["Ger1        "],"3"=>["Ger2        ","Ger3        "])

#cenário de 1 a 6
for c in 1:6
        print("Cenario: ")
        println(c)
        println("Geração")
        for i in keys(DictBusTherm)
                print(i)
                print("->")
                total = 0
                for j in DictBusTherm[i]
                        p=dictThermName[j]
                        print(p)
                        print(": ")
                        step = nthermal*(c-1)
                        print(gerthermal[step+p])
                        print("; ")
                        total = gerthermal[step+p] + total
                end
                print("TOTAL: ")
                print(total)
                println("")
        end
        println("Demanda")
        for i in 1:ndem
                print(demName[i])
                print("-> ")
                step = ndem*(c-1)
                print(totdem[step+i])
                print("; ")
        end
        println("")
        println("-------------------------")
end


#--------------Num estudo, com mais de um tipo de usina, é necessário identificar os tipos de usinas em cada barra para fazer a soma correta da geração na barra---------------------------------
DictBusGer = Dict("1"=>["T","Ger1        "],"3"=>["T","Ger2        ","T","Ger3        "])
c=1
for i in keys(DictBusGer)
        print(i)
        print("->")
        total = 0
        j=DictBusGer[i]
        for x in 1:Int32(size(j)[1]/2)
                if j[2*x-1]=="T"
                        println(j[Int32(2*x)])
                        p=dictThermName[j[2*x]]
                        print(p)
                        print(": ")
                        step = nthermal*(c-1)
                        print(gerthermal[step+p])
                        print("; ")
                        total = gerthermal[step+p] + total
                end
        end
        print("TOTAL: ")
        print(total)
        println("")
end

#--------------Num estudo, onde as usinas precisam ser dividdas em barras, é necessário identificar a participação da usina em cada barra para fazer a soma correta da geração na barra---------------------------------
DictBusGer = Dict("1"=>["T", 1,"Ger1        ","T", 0.2,"Ger2        "],"3"=>["T",0.8,"Ger2        ","T",1,"Ger3        "])
c=1
for i in keys(DictBusGer)
        print(i)
        print("->")
        total = 0
        j=DictBusGer[i]
        for x in 1:Int32(size(j)[1]/3)
                if j[3*x-2]=="T"
                        println(j[Int32(3*x)])
                        p=dictThermName[j[3*x]]
                        print(p)
                        print(": ")
                        step = nthermal*(c-1)
                        part = j[3*x-1]
                        print(gerthermal[step+p]*part)
                        print("; ")
                        total = part*gerthermal[step+p] + total
                end
        end
        print("TOTAL: ")
        print(total)
        println("")
end



for s in 1:stages*scenarios*blocks
    for t in 1:nthermal
        a= DictGerBus[thermName[t]]
        println(a)
    end
    for g in 1:ngnd
        println("gnd")
    end
    for h in 1:nhydro
    end
    for d in 1:ndem
    end
end
