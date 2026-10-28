import matplotlib.pyplot as plt
# Angela Correa NC = 0037
# dato
no_lista = [1,2,3,17,48]
califa_ml = [20,30,80,100,90]
califa_va = [70,90,60,90,100]
plt.plot(no_lista,califa_ml,label="Califa ML")
plt.plot(no_lista,califa_va,label="Califa VA")
plt.title(" calificaciones materias -------- 0037")
plt.xlabel("Numero de lista -------- 0037 ")
plt.ylabel("Calificacion -------- 0037 ")
plt.legend()
plt.show()
print("Angela Correa NC = 0037")