import streamlit as st
st.title('El Ayudante de  la Pala , ¡Palosa!')
st.header('¡Tan amigable con el ecosistema como contigo!')
option = st.selectbox('¿QUE ESTAS BUSCANDO?',
                     ('Busca aquí :)', 'Insecticidas', 'Fertilizante', 'Desinfectante RBM-Q', 'Abono/Composta/Lumus', 'Sistemas de riego', 'Compuestos químicos', 'Ropa/Vestimenta', 'Herramienta y maquinaria', 'Semillas', ' '))
st.sidebar.title('¿Quiénes somos?')
st.sidebar.write('Somos una empresa socialmente responsable que busca la eficacia y seguridad de productos químicos en materia de agricultura por medio de nuestra página web, garantizando productos de alta calidad y seguridad en transporte.') 
st.sidebar.balloons()
st.sidebar.image('https://encolombia.com/wp-content/uploads/2021/01/Agricultura-moderna.jpg')
st.sidebar.header('Misión')
st.sidebar.write('Proveer y satisfacer las necesidades de nuestros clientes de una forma mas eficaz, sencilla y segura en materia de agricultura por medio de nuestra página de internet. ')
st.sidebar.header('Visión')
st.sidebar.write('Ser lideres de mercado en materia de agricultura asi como el tener un sector de clientes específicos  asi como clientes fecuentes y confiables.')
st.sidebar.header('Valores')
st.sidebar.markdown("""
* Responsabilidad social
* Calidad
* Honestidad
* Compromiso
* Eficacia  
            """)
st.sidebar.subheader('Autores')
st.sidebar.write('Adrian Wright Olivas')
st.sidebar.write('Gilberto Domínguez Avilés')
st.sidebar.subheader('Dirección')
st.sidebar.write('Facultad de Ciencias Químicas UACH, Universitario, Campus Uach, Chihuahua, Lealtad II, 31125 Chihuahua, Chih., México')
st.image('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.telesurtv.net%2Fopinion%2F-Semillas-cuando-germino-la-agricultura-y-florecio-la-humanidad-20170821-0024.html&psig=AOvVaw3aLbriIdot6Q1v2LhnqJYo&ust=1653057463294000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLDg4Inl6_cCFQAAAAAdAAAAABAJ')
st.sidebar.subheader('¿Cómo utilizar la página?')

video_file = open('star.mp4', 'rb')
video_bytes = video_file.read()

st.sidebar.video(video_bytes)


if option =='Insecticidas':
  st.subheader('Insecticida Urbano Cipermetrina ')
  st.image('https://www.productoslimpiaya.com/wp-content/uploads/2021/01/cipermetrina.jpg')
  st.write('Es un insecticida con acción de contacto e ingestión, con excelente efecto de derribe y persistencia. Está compuesto por cipermetrina un eficiente insecticida convencional eficiente para cultivos de Algodonero, Maíz, Soya, Frijol y Cebolla')
  st.write('Especificaciones: 80% de concentración en cada 100ml. Contenido neto 2.8lt')
  st.write('Precio:$129.39')
  st.write('Lugar de procedencia: Ojinaga, CHIH.')

  st.subheader('JABÓN POTÁSICO ')
  st.image('https://cdn.shopify.com/s/files/1/0246/3147/6308/products/JabonNuevo2.png?v=1641578067')
  st.write('El jabón potásico (también conocido como potasa) es un potente pesticida naturalque se usa para mantener a raya la proliferación de plagas como pulgones o negrilla.')
  st.write('Especificaciones: 78% de concentración en cada 100 ml. Contenido neto 165 gr.')
  st.write('Precio: $ 179.00 Oferta')
  st.write('Lugar de procedencia: Delicias, CHIH.')


  
if option =='Fertilizantes':
  st.subheader('Insecticida Urbano Cipermetrina ')
  st.image('https://www.productoslimpiaya.com/wp-content/uploads/2021/01/cipermetrina.jpg')
  st.write('Es un insecticida con acción de contacto e ingestión, con excelente efecto de derribe y persistencia. Está compuesto por cipermetrina un eficiente insecticida convencional eficiente para cultivos de Algodonero, Maíz, Soya, Frijol y Cebolla')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')

  st.subheader('JABÓN POTÁSICO ')
  st.image('https://cdn.shopify.com/s/files/1/0246/3147/6308/products/JabonNuevo2.png?v=1641578067')
  st.write('El jabón potásico (también conocido como potasa) es un potente pesticida naturalque se usa para mantener a raya la proliferación de plagas como pulgones o negrilla.')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')


if option =='Desinfectante RBM-Q':
  st.subheader('Insecticida Urbano Cipermetrina ')
  st.image('https://www.productoslimpiaya.com/wp-content/uploads/2021/01/cipermetrina.jpg')
  st.write('Es un insecticida con acción de contacto e ingestión, con excelente efecto de derribe y persistencia. Está compuesto por cipermetrina un eficiente insecticida convencional eficiente para cultivos de Algodonero, Maíz, Soya, Frijol y Cebolla')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')
  st.image('')
  st.write('El jabón potásico (también conocido como potasa) es un potente pesticida naturalque se usa para mantener a raya la proliferación de plagas como pulgones o negrilla.')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')

if option =='Abono/Composta/Lumus':
  st.subheader('Humus de lombriz ')
  st.image('https://th.bing.com/th/id/R.ea5345e69eef3ec6dd2c7bf6f2951db5?rik=LFV1mIjpyTWL9w&pid=ImgRaw&r=0')
  st.write('En Plásticos y Papeles Viedma disponemos de bolsas para humus, abonos y forraje. Este tipo de embalaje permite transportar grandes cargas pesadas sin riesgo a rotura. El humus de lombriz es uno de los abonos orgánicos más populares del mercado.')
  st.write('Especificaciones: 5 kg por costal')
  st.write('Precio: $359')
  st.write('Lugar de procedencia: Ojinaga, CHIH.')

  st.subheader('ABONO VERMILITA')
  st.image('https://th.bing.com/th/id/R.3d0dfc258a737512bc9395233e902490?rik=2HenEF5d0i8RdA&riu=http%3a%2f%2fcdn.shopify.com%2fs%2ffiles%2f1%2f1457%2f1446%2fproducts%2fVermiculita_Sustrato_grande.jpg%3fv%3d1484349473&ehk=dxwCDNldE92ff6%2bVGQ%2fFRjfVt66XifzpBylKsnyJuh4%3d&risl=&pid=ImgRaw&r=0')
  st.write('Abono Orgánico Fermentado tipo Bocashi Costal con 19 litros.')
  st.write('Modo de Empleo: mezclar con la tierra ó sustrato evitando aplicar directamente en la zona de raíces, regar abundantemente después de la aplicación.')
  st.write('Especificaciones:Aplicar cada 15 días en hortalizas, hierbas, plantas ornamentales y cada 4 meses en árboles. ')
  st.write('Precio: $149.99')
  st.write('Lugar de procedencia: Fabrica las huertas Michoacan, Méxcio.')

if option =='Sistemas de riego':
  st.subheader('Insecticida Urbano Cipermetrina ')
  st.image('https://www.productoslimpiaya.com/wp-content/uploads/2021/01/cipermetrina.jpg')
  st.write('Es un insecticida con acción de contacto e ingestión, con excelente efecto de derribe y persistencia. Está compuesto por cipermetrina un eficiente insecticida convencional eficiente para cultivos de Algodonero, Maíz, Soya, Frijol y Cebolla')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')

  st.subheader('JABÓN POTÁSICO ')
  st.image('https://cdn.shopify.com/s/files/1/0246/3147/6308/products/JabonNuevo2.png?v=1641578067')
  st.write('El jabón potásico (también conocido como potasa) es un potente pesticida naturalque se usa para mantener a raya la proliferación de plagas como pulgones o negrilla.')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')

if option =='Compuestos químicos':
  st.subheader('Insecticida Urbano Cipermetrina ')
  st.image('https://www.productoslimpiaya.com/wp-content/uploads/2021/01/cipermetrina.jpg')
  st.write('Es un insecticida con acción de contacto e ingestión, con excelente efecto de derribe y persistencia. Está compuesto por cipermetrina un eficiente insecticida convencional eficiente para cultivos de Algodonero, Maíz, Soya, Frijol y Cebolla')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')

  st.subheader('JABÓN POTÁSICO ')
  st.image('https://cdn.shopify.com/s/files/1/0246/3147/6308/products/JabonNuevo2.png?v=1641578067')
  st.write('El jabón potásico (también conocido como potasa) es un potente pesticida naturalque se usa para mantener a raya la proliferación de plagas como pulgones o negrilla.')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')

if option =='Ropa/Vestimenta':
  st.subheader(' Oberol de carga ')
  st.image('https://th.bing.com/th/id/R.d068d3b4ea081c5631edd13ee02db6fd?rik=CdVPXQlgWe%2fyOQ&pid=ImgRaw&r=0')
  st.write(' Oberol de color rojo para trabajos pesados, riesgosamente quimicos, biológicos y químico-biológicos.')
  st.write('Especificaciones: todas las tallas disponibles')
  st.write('Precio: mayoreo: $299    menudeo: $199')
  st.write('Lugar de procedencia: Leon, Guanajuato.')

  st.subheader('Masacaras KN95 ')
  st.image('https://th.bing.com/th/id/OIP.aBmOE_-xmwm5wl6ACDfdngHaHa?pid=ImgDet&rs=1')
  st.write('Mascarilla KN95 tipo quirurgica de color blanco, todos modelos disponibles.')
  st.write('Especificaciones: color blanco')
  st.write('Precio: precio por unidad $300')
  st.write('Lugar de procedencia: Guadalajara, México.')

if option =='Herramienta/Maquinaria':
  st.subheader('Tractor agrícola 4850 John Deer ')
  st.image('https://th.bing.com/th/id/R.3f3bac58ac083b717fdcc2fd1f428177?rik=nbYvRJWYvwKJWA&pid=ImgRaw&r=0')
  st.write(' Tractor agrícola John Deer 4850, año 1998, procedencia Dallas, Tx.')
  st.write('Especificaciones: Fallas de bateria')
  st.write('Precio: negociable +$600,000.00')
  st.write('Lugar de procedencia: Cd. Juarez, Chihuahua.')

  st.subheader('Pala Frontal Para Tractores Agricolas Massey Ferguson ')
  st.image('https://th.bing.com/th/id/R.9e52705b7aa59a0d9e7bb561288a0bee?rik=%2fpuvzLQs%2bHsF%2fA&pid=ImgRaw&r=0')
  st.write('PALA FRONTAL PARA TRACTORES MASSEY FERGUSON ( 255, 265, 275, 285, 355, 365, 375, 385 ) o QUE TENGA BASE PARA ATORNILLAR EN LA PARTE DE ENFRENTE ARRIBA DEL EJE EN CUADRO CON 4 PERFORACIONES, PARA TRACTORES DE 60 A 100 HP.ver las ultimas fotos se muestra como son las bases y las perforaciones necesarias en el tractor para atornillas.')
  st.write('Especificaciones: Color rojo')
  st.write('Precio: $180,000')
  st.write('Lugar de procedencia: Hermosillo, Sonora.')

if option =='Semillas':
  st.subheader('Insecticida Urbano Cipermetrina ')
  st.image('https://www.productoslimpiaya.com/wp-content/uploads/2021/01/cipermetrina.jpg')
  st.write('Es un insecticida con acción de contacto e ingestión, con excelente efecto de derribe y persistencia. Está compuesto por cipermetrina un eficiente insecticida convencional eficiente para cultivos de Algodonero, Maíz, Soya, Frijol y Cebolla')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')

  st.subheader('JABÓN POTÁSICO ')
  st.image('https://cdn.shopify.com/s/files/1/0246/3147/6308/products/JabonNuevo2.png?v=1641578067')
  st.write('El jabón potásico (también conocido como potasa) es un potente pesticida naturalque se usa para mantener a raya la proliferación de plagas como pulgones o negrilla.')
  st.write('Especificaciones:')
  st.write('Precio:')
  st.write('Lugar de procedencia:')
