import graphene
from graphql_relay import from_global_id

from .models import Planet, People
from .types import PlanetType,PeopleType,FilmType
from .utils import generic_model_mutation_process


class SetPlanetMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return SetPlanetMutation(planet=planet)

class SetPeopleMutation(graphene.relay.ClientIDMutation):
    """
    Para el metodo set podemos reutilizar la misma forma de la mutacion anterior,
    en este caso el ID no se solicita para garantizar que se cree un registro.
    """
    class Input:
        name = graphene.String(required=True)
        mass = graphene.String(required=False)
        height = graphene.String(required=False)
        hair_color = graphene.String(required=True)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=True)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=True)
        home_world = graphene.GlobalID(parent_type=PlanetType, required=False)
        films = graphene.GlobalID(parent_type=FilmType, required=False)
    
    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': People, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        people = generic_model_mutation_process(**data)
        return SetPeopleMutation(people=people)

class UpdatePeopleMutation(graphene.relay.ClientIDMutation):
    """
    Para el metodo update podemos reutilizar la misma forma de la primera mutacion,
    en este caso el ID es requerido para garantizar que se actualice un registro
    ya creado
    """
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        mass = graphene.String(required=False)
        height = graphene.String(required=False)
        hair_color = graphene.String(required=True)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=True)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=True)
        home_world = graphene.GlobalID(parent_type=PlanetType, required=False)
        work_films = graphene.GlobalID(parent_type=FilmType, required=False)
    
    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': People, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        people = generic_model_mutation_process(**data)
        return UpdatePeopleMutation(people=people)
