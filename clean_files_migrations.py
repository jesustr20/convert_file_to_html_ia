import os
import shutil

"""Borra los archivos temporales y los acrhivos de migraciones
Para correr nuevamente la db y generar todo de nuevo, solo es temporal"""

def delete_pycache(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for dir_name in dirs:
            if dir_name=="__pycache__":
                pycache_path = os.path.join(root, dir_name)
                print(f"Borrado carpeta: {pycache_path}")
                shutil.rmtree(pycache_path)

def delete_migrations(root_directory):
    for root, dirs, files in os.walk(root_directory):
        if 'migrations' in dirs:
            migration_path = os.path.join(root, 'migrations')
            for file_name in os.listdir(migration_path):
                if file_name != '__init__.py' and file_name.endswith('.py'):
                    file_path = os.path.join(migration_path, file_name)
                    print(f"Borrado archivo de migración: {file_path}")
                    os.remove(file_path)

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))

    delete_pycache(project_root)
    delete_migrations(project_root)

    print("Limpieza completada.")