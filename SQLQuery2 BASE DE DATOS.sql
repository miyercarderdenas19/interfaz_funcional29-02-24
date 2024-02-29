-- SABER LAS TABLAS QUE HAY EN LA BASE DE DATOS
SELECT TABLE_SCHEMA, TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE'

-- VER ESTRUCTURA DE TABLA
GO 
EXEC sp_help 'Descripcion'  
GO
-- INSERTAR DATOS DE PRUEBA



SELECT * FROM [dbo].[Mantenimiento] -- Esta tabla no tiene datos
SELECT * FROM [dbo].[Descripcion] -- Esta tabla no tiene datos
SELECT * FROM [dbo].[Responsable] -- Esta tabla no tiene datos

SELECT * FROM [dbo].[InformacionProducto]



INSERT INTO InformacionProducto (idProducto, Nombre, Descripcion )
VALUES
       (4, 'PRISMA', 'valvulas del PRISMA'),
       (5, 'RCM', 'medidor de flujo del RCM' ),
       (6, 'TLV','trampa de valor del TLV'),
	   (7, 'SAMSON', 'valvulas del SAMSON' ),
       (8, 'GAST', 'bombas de vacio del GAST'), 
	   (9, 'BURKERT', 'medidor flujos del BURKERT'),
       (10, 'WILKERSON', 'valvulas de aire comprimido del WILKERSON'),
	   (11, 'SUDMO', 'valvulas del SUDMO');
	

DELETE FROM InformacionProducto WHERE Nombre = 'piedras';


INSERT INTO  GG