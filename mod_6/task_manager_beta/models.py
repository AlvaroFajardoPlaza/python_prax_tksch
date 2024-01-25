import db
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

#### Configuramos las clases que se convertirán en las tablas de nuestra bbdd
class Task(db.Base):
    # Atributos globales -> especificaciones de la tabla
    __tablename__ = "tasks"
    __table_args__={ "sqlite_autoincrement" : True}
    task_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    category = Column(String, nullable=False)
    is_done = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(Boolean, nullable=False, default=False) # Manejo de soft-delete

    def __init__(self, name, description, category, is_done):
        self.name = name
        self.description = description
        self.category = category
        self.is_done = is_done

    def __repr__(self):
        return "Task {}:\n\tNombre: {}\n\tDescripción: {}\n\tCategoria: {}\n\tCreada: {}\n\tÚltima modificación: {}. Hecha: {}.".format(
                                                                                                                    self.task_id,
                                                                                                                        self.name,
                                                                                                                        self.description,
                                                                                                                        self.category,
                                                                                                                        self.created_at,
                                                                                                                        self.updated_at,
                                                                                                                        self.is_done)

    def __str__(self):
        return "Task {}:\n\tNombre: {}\n\tDescripción: {}\n\tCategoria: {}\n\tCreada: {}\n\tÚltima modificación: {}".format(self.task_id,
                                                                                                                         self.name,
                                                                                                                         self.description,
                                                                                                                         self.category,
                                                                                                                         self.created_at,
                                                                                                                         self.updated_at)

