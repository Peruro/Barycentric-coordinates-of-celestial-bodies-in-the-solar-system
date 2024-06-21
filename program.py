
# librerías
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric
from astropy.time import Time


# configuramos las efemérides
solar_system_ephemeris.set('builtin')
t = Time('2100-01-01')

# Función para obtener posiciones de los planetas
def get_planet_positions(t):

    planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
    positions = {}

    for planet in planets:

        positions[planet] = get_body_barycentric(planet, t).xyz.to('AU').value
        
    return positions


positions = get_planet_positions(t)


# graficamos
fig, ax = plt.subplots()

ax.set_aspect('equal')
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_title('Posiciones de los Planetas en el Sistema Solar')

# Ajustar los límites del gráfico para mejor visualización
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)


# Dibujar las posiciones
for planet, pos in positions.items():
    ax.plot(pos[0], pos[1], 'o', label=planet.capitalize())

ax.legend()
plt.show()

# graficamos en 3D
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title('Posiciones de los Planetas en el Sistema Solar')

# dibujamos tambien la posicion del sol
ax.scatter(0, 0, 0, color='yellow', label='Sun', s=100)


# Dibujar las posiciones en 3D
for planet, pos in positions.items():
    ax.scatter(pos[0], pos[1], pos[2], label=planet.capitalize())


ax.legend()
plt.show()



# posicion de neptuno
neptune_position = get_body_barycentric('neptune', t)

# convertimos a array
neptune_pos = neptune_position.xyz.to('AU').value

# distancia de neptuno al centro de masas
distance_neptune_to_barycenter = np.linalg.norm(neptune_pos)

# Mostrar la distancia
print(f"Distancia de Neptuno al baricentro del sistema solar en {t.iso}: {distance_neptune_to_barycenter:.3f} AU")