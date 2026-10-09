import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================

A = (0, 0, 0)
B = (4, 0, 0)
C = (4, 4, 0)
D = (0, 4, 0)
E = (2, 2, 4)

vertices = [A, B, C, D, E]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================
# 3. DEFINIR LAS CARAS
# ============================

caras = [
    [A, B, C, D],  # Base
    [A, B, E],     # Cara frontal
    [B, C, E],     # Cara derecha
    [C, D, E],     # Cara posterior
    [D, A, E]      # Cara izquierda
]
# ============================
# 4. DIBUJAR LA CARA
# ============================

cara = Poly3DCollection(
    caras,
    alpha=0.4,
    edgecolor="black"
)

ax.add_collection3d(cara)

# ============================
# 5. DIBUJAR LOS VÉRTICES
# ============================

for nombre, vertice in zip(["A", "B", "C", "D", "E"], vertices):

    x, y, z = vertice

    ax.scatter(x, y, z, s=80)

    ax.text(
        x,
        y,
        z + 0.1,
        nombre,
        fontsize=12
    )

# ============================
# 5. DIBUJAR LAS ARISTAS
# ============================

aristas = [
    (A, B),
    (B, C),
    (C, D),
    (D, A),
    (A, E),
    (B, E),
    (C, E),
    (D, E)
]

for inicio, fin in aristas:

    ax.plot(
        [inicio[0], fin[0]],
        [inicio[1], fin[1]],
        [inicio[2], fin[2]],
        linewidth=2
    )

# ============================
# 6. CONFIGURAR LA ESCENA
# ============================

ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_zlim(-1, 6)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_title(
    "Pirámide formada por vértices, aristas y una cara"
)

plt.show()