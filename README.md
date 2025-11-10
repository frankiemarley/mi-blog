```markdown
# Mi Blog Personal

Un blog moderno y responsive creado con HTML5 y CSS3 puro como proyecto académico. Diseñado con las mejores prácticas de desarrollo web frontend.

## 🌟 Características

- **Diseño Moderno**: Interface limpia y profesional con gradientes y animaciones
- **Totalmente Responsive**: Adaptado para móviles, tablets y desktop
- **3 Entradas Completas**: Tecnología, Viajes y Cocina con contenido de calidad
- **Navegación Intuitiva**: Menú fijo y navegación entre artículos
- **Performance Optimizada**: Carga rápida y código eficiente
- **Accesibilidad**: HTML semántico y contraste adecuado

## 🚀 Demo en Vivo

## 📁 Estructura del Proyecto

```
mi-blog/
├── index.html              # Página principal
├── entrada1.html           # Entrada: El Futuro de la IA
├── entrada2.html           # Entrada: Descubriendo Japón
├── entrada3.html           # Entrada: Recetas Italianas
├── styles/
│   └── main.css            # Estilos principales (CSS3)
├── images/                 # Assets visuales
└── README.md               # Este archivo
```

## 🛠 Tecnologías Utilizadas

- **HTML5**: Estructura semántica y accesible
- **CSS3**: 
  - Flexbox y Grid para layouts
  - Variables CSS para consistencia
  - Animaciones y transiciones
  - Diseño responsive con media queries
- **Git & GitHub**: Control de versiones
- **Netlify**: Deployment y hosting

## 🎨 Características de Diseño

### Paleta de Colores
```css
--primary-color: #2563eb;
--primary-dark: #1d4ed8;
--secondary-color: #7c3aed;
--text-dark: #1f2937;
--text-light: #6b7280;
```

### Tipografía
- **Fuente Principal**: Inter (Google Fonts)
- **Pesos Utilizados**: 300, 400, 500, 600, 700

### Componentes Principales
- Header con navegación sticky
- Hero section con call-to-action
- Grid de artículos con cards animadas
- Footer con enlaces organizados
- Diseño de artículos con tipografía jerárquica

## 📱 Contenido del Blog

### 🖥️ Entrada 1: Tecnología
**"El Futuro de la Inteligencia Artificial"**
- Avances recientes en IA
- Desafíos éticos
- Aplicaciones prácticas
- Futuro de la tecnología

### ✈️ Entrada 2: Viajes  
**"Descubriendo Japón: Guía Completa"**
- Planificación del viaje
- Tokio y sus distritos
- Kioto y cultura tradicional
- Consejos culturales esenciales

### 🍝 Entrada 3: Cocina
**"Recetas Italianas Auténticas"**
- Pasta fresca casera
- Salsa pomodoro tradicional
- Tiramisú clásico
- Consejos de chef profesional

## 🚀 Instalación y Uso Local

### Prerrequisitos
- Navegador web moderno
- Editor de código (VS Code recomendado)
- Git (opcional)

### Pasos para Ejecutar Localmente

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/frankiemanley/mi-blog.git
   cd mi-blog
   ```

2. **Abrir en el navegador**
   ```bash
   # Método 1: Doble clic en index.html
   # Método 2: Servidor local
   python -m http.server 8000
   # Luego visitar http://localhost:8000
   ```

## 🌐 Deployment

### Netlify
1. Conectar repositorio de GitHub
2. Configurar build settings:
   - Build command: (vacío)
   - Publish directory: ./
3. Deployment automático con cada push

### GitHub Pages
1. Ir a Settings > Pages
2. Seleccionar branch main
3. Deployment automático

## 🔧 Personalización

### Cambiar Colores
Edita las variables CSS en `styles/main.css`:
```css
:root {
    --primary-color: #tu-color;
    --secondary-color: #tu-color;
}
```

### Agregar Nuevas Entradas
1. Crear nuevo archivo HTML (ej: `entrada4.html`)
2. Seguir la estructura de entradas existentes
3. Actualizar navegación en todos los archivos
4. Agregar card en `index.html`

## 👨‍💻 Autor

- GitHub: [@frankiemanley](https://github.com/frankiemanley)

## 🙏 Agradecimientos

- [Unsplash](https://unsplash.com) por las imágenes de calidad
- [Google Fonts](https://fonts.google.com) por la tipografía Inter
- [Netlify](https://netlify.com) por el hosting gratuito

Blog en producción: https://69122f0356b7450007ea55c6--joyful-kelpie-6247e8.netlify.app/ 

Repositorio GitHub: https://github.com/frankiemarley/mi-blog 