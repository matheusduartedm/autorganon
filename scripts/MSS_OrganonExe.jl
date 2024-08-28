function OrganonExe(PATH_ORGANON)
    cd(PATH_ORGANON)
    comando1 = string(PATH_ORGANON,"ORGANONB.exe")
    comando2 = string(PATH_ORGANON,  "script.spt" )
    run(`$comando1 -1 $comando2`)
    println("Rodadas Dinâmicas executadas com sucesso")
end

OrganonExe(PATH_ORGANON)