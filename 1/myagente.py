from agentes import *


class RoboDog(Agent):
    def eat(selg, thing):
        print("RoboDog: recebeu comida as {}".format(self.location))

    def drink(self, thing):
        print("Robodog: bebeu agua as {}".format(self.location))


dog = RoboDog()

print(dog.alive)


class Food(Thing):
    pass

class Water(Thing):
    pass

class Park(Environment):
    def percept(self, agent):
        '''
        Imprime e retorna uma lista de coisas que estão na localização
        do nosso agente
        '''
        things = self.list_things_at(agent.location)
        print(things)
        return things

    def execute_action(self, agent, action):
        '''
        Altera o estado do ambiente com base no que o agente fez
        '''
        if action == "move down":
            agent.movedown()
        elif action == 'eat':
            items = self.list_things_at(agent.location, tclass=Food)
            if len(items) != 0:
                if agent.eat(items[0]):
                    self.delete_thing(items[0])
        elif action == 'drink':
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]):
                    self.delete_thing[items[0]]

    def is_done(self):
        no_edibles = not any(isinstance(thing, Food) or isinstance(
            thing, Water) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles






