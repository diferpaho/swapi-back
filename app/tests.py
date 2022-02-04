import json

from graphene_django.utils.testing import GraphQLTestCase

from swapi.schema import schema


class FirstTestCase(GraphQLTestCase):
    fixtures = ['app/fixtures/unittest.json']
    GRAPHQL_SCHEMA = schema

    def test_people_query(self):
        response = self.query(
            '''
                query{
                  allPlanets {
                    edges{
                      node{
                        id
                        name
                      }
                    }
                  }
                }
            ''',
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        self.assertEqual(len(content['data']['allPlanets']['edges']), 61)

    def test_setPeople_mutation(self):
        response = self.query(
            '''
            mutation setPeopleMutation{
                setPeopleMutation(input: {
                      name: "Luke Skywalker", 
                      hairColor:"BLACK",
                      eyeColor:"BLACK",
                      gender:"MALE",
                }) {
                    people {
                        id
                        name
                        hairColor
                        eyeColor
                        gender
                    }
                }
            }
            ''',
           )

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

    def test_UpdatePeople_mutation(self):
        response = self.query(
            '''
            mutation UpdatePeopleMutation{
                UpdatePeopleMutation(input: {
                      id:"UGVvcGxlVHlwZTo5NQ==",
                      name: "Luke Skywalker", 
                      hairColor:"BLACK",
                      eyeColor:"BLACK",
                      gender:"MALE",
                }) {
                    people {
                        id
                        name
                        hairColor
                        eyeColor
                        gender
                    }
                }
            }
            ''',
           )

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
