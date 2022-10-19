# CORE ODOO v14

Sirve para utilizar el comando scaffold sin instalar todo odoo en windows

## **Requisitos:**

- carpeta `odoo` que se encuentra en el proyecto principal
- archivo `odoo-bin`
- archivo `requirements.txt`

## **Path:**
```
    core_odoo14/
                odoo/*
                odoo-bin
                requirements.txt
```
## **Pasos:**

1. Crear un entorno virtual
2. Activar entorno virtual
3. Instalar paquetes `requirements.txt`
4. Ejecutar `python core_odoo14/odoo-bin scaffold  <module_name> <Path_to_addons_folder>`

Nota: Es similar a cuando utilizamos scaffold con odoo instalado
```
"<Path_to_python.exe in the Odoo folder>" "<Path_to_odoo-bin>" scaffold "<Path_to_addons_folder>"

"c:\Program Files (x86)\Odoo 11.0\python\python.exe" "C:\Program Files (x86)\Odoo 11.0\server\odoo-bin" scaffold <module name here> "C:\Program Files (x86)\Odoo 11.0\server\odoo\addons"
```

## Create package

1. install wheel
2. create metadata and `setup.py`
3. execute command: `python setup.py sdist`
4. execute command: `python setup.py bdist_wheel`

**Nota:** Si escribe `pip install dist/odoo_bin-0.0.1-py3-none-any.whl` se instalaria en local

### Para instalar

`pip install git+https://github.com/josenoguera-94/odoo-bin.git`
