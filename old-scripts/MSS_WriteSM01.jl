PATH = "D:\\GoogleDrive\\ufrj\\TCC\\02-Base_Dados\\99-Dados_Colombia\\"
file = "maquinas_2030_damping_v2.csv"

header1="!   No  GOV GID  BName"
header2="!(--Xld-) (--Ra--) (-Sbase) (--Xt--) (---H--) (---D--)"
maquina1=readdlm(PATH*file,',', comments=false,skipstart=1)
(l,c) = size(maquina1)
c1    = 4
c2    = 6
newDyn  = ""

for i in 1:l
    newDyn = newDyn*"SM01\n"
    newDyn = newDyn*header1*"\n"
    for j in 1:c1
        newDyn = newDyn*string(maquina1[i,j])*" "
    end
    newDyn = newDyn*"\n"
    newDyn = newDyn*header2*"\n"
    for j in 1+c1:c2+c1
        newDyn = newDyn*string(maquina1[i,j])*" "
    end
    newDyn = newDyn*"\n"
    newDyn = newDyn*"/\n"
end
newDyn = newDyn*"-999/\n"
newDyn = newDyn*"-999/\n"
newDyn = newDyn*"-999/\n"
arq  = PATH*"maquinas_2030_damping_v2.dyn"
narq = open(arq,"w")
write(narq,newDyn)
close(narq)
println("Arquivo Dinâmico Finalizado")
