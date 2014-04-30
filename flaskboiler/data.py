from flask.ext.sqlalchemy import SQLAlchemy


# Setup SQLAlchemy database stub, which will be initialized inside create_app() factory.
db = SQLAlchemy()


class Data(object):
    """
    Base class that all service-layer classes will inherit from. This provides basic service-layer
    functionality such as CRUD.
    """

    def __init__(self, model_class):
        # Defines the data model that the service defines.
        self._model_class = model_class

    def get(self, model_id):
        """
        Gets a model that matches the specified object ID.

        :param model_id: Model ID to get.
        :return: Model that matches object_id.
        """
        return self._model_class.query.get(model_id)

    def find(self, **kwargs):
        """
        Finds a list of models matching the keyword arguments.

        Usage:
            users_named_bobby = user_service.find(first_name="bobby")

        :param kwargs: Keyword arguments used to filter and retrieve a list of matching models.
        :return: List of models matching the keyword arguments.
        """
        return self._model_class.query.filter_by(**kwargs)

    def create(self, **kwargs):
        """
        Creates a new model and saves into the database.

        Usage:
            bobby = user_service.create(username="little_bobby_tables", first_name="bobby", last_name="tables")

        :param kwargs: Keyword arguments used for creating a new model.
        :return: Newly created (and saved) model.
        """
        new_model = self._model_class(**kwargs)
        self._save(new_model)

        return new_model

    def update(self, model, **kwargs):
        """
        Updates existing model and saves the updated changes into the database.

        Usage:
            bobby = user_service.get(username="little_bobby_tables")
            user_service.update(bobby, first_name="robert")

        :param model: Model to update.
        :param kwargs: Keyword arguments to update on the model.
        :return: Updated (and saved) model.
        """
        for k, v in kwargs.iteritems():
            setattr(model, k, v)

        self._save(model)

    def _save(self, model):
        """
        Saves the model into the database.

        If the model does not exist yet, a new row will be inserted. Otherwise if the model already
        exists, then the existing row will be updated.

        :param model: Model to save in the database.
        """
        db.session.add(model)
        db.session.commit()
