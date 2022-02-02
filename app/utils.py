def generic_model_mutation_process(model, data, id=None, commit=True):
    """Función que recibe un modelo, una información(data) y un id (opcional),
    la función permite crear o editar un registro.
    Si se obtuvo un id, se busca el registro con esa identificación para realizar
    la actualización de los campos.
    En caso de que no se tenga un id, se crea el registro con la información suministrada(data).
    """
    if id:
        
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
