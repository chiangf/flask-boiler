class Service(object):
    """
    Base class that all service-layer classes will inherit from. This provides basic service-layer
    functionality such as CRUD.
    """
    def __init__(self, data):
        """
        Constructs the Service object.

        :param data: Data-layer object inheriting from Data, which acts as the facade to the database.
        """
        self._data = data

    def get(self, model_id):
        """
        Gets a model that matches the specified object ID.

        :param model_id: Model ID to get.
        :return: Model that matches object_id.
        """
        return self._data.get(model_id)

    def find(self, **kwargs):
        """
        Finds a list of models matching the keyword arguments.

        Usage:
            users_named_bobby = user_service.find(first_name="bobby")

        :param kwargs: Keyword arguments used to filter and retrieve a list of matching models.
        :return: List of models matching the keyword arguments.
        """
        return self._data.find(**kwargs)

    def create(self, **kwargs):
        """
        Creates a new model and saves into the database.

        Usage:
            user_service.create(first_name="bobby", last_name="tables")

        :param kwargs: Keyword arguments used for creating a new model.
        :return: Newly created (and saved) model.
        """
        new_model = self._data.create(**kwargs)
        return new_model

    def update(self, model, **kwargs):
        """
        Updates existing model and saves the updated changes into the database.

        Usage:
            user_service.update(first_name="robert")

        :param model: Model to update.
        :param kwargs: Keyword arguments to update on the model.
        :return: Updated (and saved) model.
        """
        self._data.update(model, **kwargs)
