# <h1 align="center">**`馃彞 Estancias hospitalarias 馃彞`**</h1>

<p align="center">
<img src="https://hospitecnia.com/sites/default/files/styles/node_teaser/public/2022-01/cabecera-medxat-garantizar-seguridad-paciente.jpg?itok=EmfcX-pg"   
>
</p>


La hospitalizaci贸n, o estancia hospitalaria, cuando es prolongada constituye una preocupaci贸n a nivel mundial debido a sus efectos negativos en el sistema de salud, aumentando los costos, generando deficiencia en la accesibilidad de prestaci贸n de servicios de salud, saturaci贸n de unidades de hospitalizaci贸n y urgencias, por consiguiente, mayores efectos adversos como lo son las enfermedades intrahospitalarias.

El estudio de los procesos de atenci贸n en salud, as铆 como el conocimiento de las caracter铆sticas y perfiles de los usuarios con el objetivo de predecir la ocupaci贸n hospitalaria, es uno de los aspectos al que las autoridades de salud han prestado gran inter茅s, pues permite no s贸lo garantizar los recursos necesarios para la atenci贸n del paciente, sino realizar ajustes respecto a la oferta y demanda de los servicios de salud y los implementos asociados.
鈥?
## <h2> **`Descripci贸n del problema`** </h2>

Un importante Centro de Salud lo ha contratado con el fin de poder predecir si un paciente tendr谩 una estancia hospitalaria prolongada o no, utilizando la informaci贸n contenida en el dataset asociado, la cual recaba una muestra hist贸rica de sus pacientes, para poder administrar la demanda de camas en el hospital seg煤n la condici贸n de los pacientes recientemente ingresados. 

Para esto, se define que un paciente posee estancia hospitalaria prolongada si ha estado hospitalizado m谩s de 8 d铆as. Por lo que debe generar dicha variable categ贸rica y luego categorizar los pacientes seg煤n las variables que usted considere necesarias, justificando dicha elecci贸n. 
鈥嬧?嬧??
## **`Archivos provistos`**
鈥?
Se disponen los siguientes archivos almacenados en la carpeta 'datasets':
 - 'hospitalizaciones_train.csv': Contiene 410000 registros y 15 dimensiones, el cual incluye la informaci贸n **num茅rica** de la cantidad de d铆as de estancia hospitalaria.
 - 'hospitalizaciones_test.csv': Contiene 90000 registros y 14 dimensiones, el cual no incluye la informaci贸n de la cantidad de d铆as de estancia hospitalaria.
鈥?
## **`Descripci贸n de las dimensiones`**
- Available Extra Rooms in Hospital: Habitaciones adicionales disponibles en el hospital. Una habitaci贸n no es igual a un paciente, pueden ser individuales o compartidas.
- Department: 脕rea de atenci贸n a la que ingresa el paciente. 
- Ward_Facility_Code: C贸digo de la habitaci贸n del paciente.
- doctor_name: Nombre de el/la doctor/a a cargo del paciente.
- staff_available: Cantidad de personal disponible al momento del ingreso del paciente.
- patientid: Identificador del paciente.
- Age: Edad del paciente.
- gender: G茅nero del paciente.
- Type of Admission: Tipo de ingreso registrado seg煤n la situaci贸n de ingreso del paciente.
- Severity of Illness: Gravedad de la enfermedad/condici贸n/estado del paciente al momento del ingreso.
- health_conditions: Condiciones de salud del paciente. 
- Visitors with Patient: Cantidad de visitantes registrados para el paciente.
- Insurance: Indica si la persona posee o no seguro de salud. 
- Admission_Deposit: Pago realizado a nombre del paciente, con el fin de cubrir los costos iniciales de internaci贸n. 
- Stay (in days): D铆as registrados de estancia hospitalaria. 
鈥?
## **`Lenguajes y modulos utilizados`**


<p align="center">
<img src="https://live.staticflickr.com/65535/48057247952_f9e106cb4a_b.jpg"> </img>


- Imbalanced-learn
- Matplotlib
- Numpy
- Python
- Seaborn
- Sklearn
