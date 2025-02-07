# Generated by Django 4.1 on 2022-09-08 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0003_rolesdesistema_defecto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rolesdesistema',
            options={'permissions': [('_crear_usuario', 'Crear usuario'), ('_eliminar_usuario', 'Eliminar usuario'), ('_acceder_al_sistema', 'Acceder al sistema'), ('_crear_roles', 'Crear roles'), ('_asignar_roles', 'Asignar roles a usuario'), ('_visualizar_roles', 'Visualizar roles a usuario'), ('_eliminar_roles', 'Eliminar roles a usuario'), ('_visualizar_usuario', 'Visualizar usuario del Sistema'), ('_crear_proyecto', 'Crear Proyecto'), ('_editar_proyecto', 'Editar Proyecto'), ('_visualizar_proyecto', 'Visualizar Proyecto'), ('_cancelar_proyecto', 'Cancelar Proyecto'), ('_eliminar_miembros', 'Eliminar miembros de un proyecto'), ('_visualizar_historial_proyecto', 'Visualizar historial del proyecto'), ('_modificar_fecha', 'Modificar fecha de inicio y fin del proyecto'), ('_modificar_estado_proyecto', 'Modificar estado del proyecto'), ('_crear_sprint', 'Crear sprint'), ('_modificar_sprint', 'Modificar sprint'), ('_modificar_estado_sprint', 'Modificar estado de un sprint'), ('_crear_us', 'Crear US'), ('_modificar_us', 'Modificar US'), ('_modificar_estado_us', 'Modificar estado de US'), ('_cancelar_us', 'Cancelar US'), ('_consultar_historial_us', 'Consultar historial de un US'), ('_modificar_backlog', 'Modificar Product Backlog'), ('_modificar_sprint_backlog', 'Modificar Sprint Backlog'), ('_crear_tipos_us', 'Crear tipos de US'), ('_modificar_tipos_us', 'Modificar tipos de US'), ('_visualizar_burndown_chart', 'Visualizar Burndown Chart'), ('_visualizar_kanban', 'Visualizar Tabla Kamban')]},
        ),
    ]
