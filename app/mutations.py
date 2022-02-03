import graphene
from graphql_relay import from_global_id

from .models import Planet, People
from .types import PlanetType,PeopleType
from .utils import generic_model_mutation_process


class PostPlanetMutation(graphene.relay.ClientIDMutation):
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
        return PostPlanetMutation(planet=planet)

class PostPeopleMutation(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        mass = graphene.String(required=True)
        height = graphene.String(required=True)
        hair_color = graphene.String(required=True)
        skin_color = graphene.String(required=True)
        eye_color = graphene.String(required=True)
        birth_year = graphene.String(required=True)
        gender = graphene.String(required=False)
        home_world = graphene.GlobalID(parent_type=PlanetType, required=True)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': People, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        people = generic_model_mutation_process(**data)
        return PostPeopleMutation(people=people)
