from sqlalchemy import and_

from flask import Flask, render_template, url_for, request, redirect
import db
from models import Task

app = Flask(__name__)

@app.route("/")
def home():
    # En esta función renderizamos toda la lista de tareas de nuestra base de datos
    task_list = db.session.query(Task).filter(Task.deleted_at != 1).all()
    deleted_task_list = db.session.query(Task).filter(Task.deleted_at == 1).all()

    return render_template("index.html", task_list=task_list, deleted_task_list=deleted_task_list)


@app.route("/category/<category>")
def filter_by_category(category: str):
    # Filtramos los resultados de la BBDD por la categoría que tenga la tarea
    task_list_by_category = db.session.query(Task).filter(and_(Task.category==category, Task.deleted_at == 0)).all()

    return render_template("category.html", task_list_by_category=task_list_by_category)



@app.route("/create-task", methods=['POST'])
def create_new_task():
    # Creamos un objeto o instancia de la clase Tarea, recopilando la info desde el formulario del front
    task = Task(name=request.form['name'], category=request.form['category'], description=request.form['description'], is_done=False)

    db.session.add(task)
    db.session.commit()
    db.session.close()
    return redirect(url_for('home')) # Redireccionamos a la página de home

@app.route("/is-done/<id>")
def task_is_done(id: int):
    task = db.session.query(Task).filter_by(task_id=id).first()
    if task.is_done == 0:
        task.is_done = 1
    else:
        task.is_done = 0
    db.session.commit()
    db.session.close()
    return redirect(url_for('home'))

@app.route("/delete/<id>")
def delete_task(id: int):
    task = db.session.query(Task).filter_by(task_id=int(id)).delete()
    db.session.commit()
    db.session.close()
    return redirect(url_for('home'))

@app.route("/soft-delete/<id>")
def soft_delete_task(id: int):
    task = db.session.query(Task).filter_by(task_id=id).first()
    if task == None:
        print("No hemos encontrado la tarea")
    elif task.deleted_at == 0:
        task.deleted_at = 1
        db.session.commit()
        db.session.close()
        return redirect(url_for('home'))
    else:
        task.deleted_at = 0
        db.session.commit()
        db.session.close()
        return redirect(url_for('home'))


"""FUNCIONES INICIALES
def showTasks():
    print("> MIS TAREAS:")
    result = db.session.query(Task).all()

    for task in result:
        print(task)

def addManyTasks():
    task1 = Task(name="Hacer la comida", description="", category="House")
    task2 = Task(name="Tokio School Práctica", description="Completar práctica módulo 6 - Task Manager", category="Study")
    task_list = [task1, task2]

    db.session.add_all(task_list)
    db.session.commit()
    db.session.close()
    print("> TAREAS AGREGADAS")
"""

if __name__ == "__main__":
    # 1º. RESET BD
    # db.Base.metadata.drop_all(bind=db.engine)

    # 2º. CREATE DB -- Tablas de models.py, si no existen
    db.Base.metadata.create_all(db.engine)

    # 3º. RUN THE APP
    app.run(
        debug=True, port=8000)  #### Cada vez que realicemos cambios en el código, se reiniciará el servidor === mismo que "nodemon" ####


    """PRUEBA INICIAL GESTOR TAREAS DESDE TERMINAL
    while(True):
        print("Elige una opción: 1.Ver tareas, 2. Añadir Tareas, 3. Salir")

        user_option = int(input("Elige (1-3)"))

        if user_option == 1:
            showTasks()
        elif user_option == 2:
            addManyTasks()
        elif user_option == 3:
            sys.exit(1)
        else:
            ("Opción no válida")
    """