from rest_framework import serializers
from django.db.models import Model
from django.apps import apps
from apps.courses.models import Course, Subject

'''
General-purpose serializers
Should be here to avoid possible circular imports.
'''


class GenericModelSerializer(serializers.ModelSerializer):
    '''
    Generic model serializer, recommended to serialize specific fields
    '''

    def __init__(self, *args, **kwargs):
        model = kwargs.pop('model', None)
        fields = kwargs.pop('fields', None)

        if not model or not issubclass(model, Model):
            raise ValueError("'model' argument must be a Django Model")
        self.Meta.model = model

        if fields is None:
            self.Meta.fields = ['id', 'name']
        elif isinstance(fields, (list, tuple)):
            self.Meta.fields = fields
        else:
            raise TypeError("'fields' argument should be none, list or tuple.")

        super().__init__(*args, **kwargs)

    class Meta:
        pass
