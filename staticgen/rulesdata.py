from click import secho
from functools import total_ordering, reduce
from funcy.py3 import partial
from os.path import join
from typing import Any, Dict, Iterator, List, Optional, Tuple
import yaml
gjcx

@total_ordering
class Rule(object):
    def __init__(self, rule: Dict[str, Any]):
        for field, ty in self.__annotations__.items():
            try:
                setattr(self, field, rule[field])
            except KeyError as e:
                if not hasattr(ty, '__args__') or not isinstance(None, ty.__args__):
                    raise e
                else:
                    setattr(self, field, None)

    def __lt__(self, other):
        return reduce(lambda acc, x: acc and getattr(self, x) < getattr(other, x), self.__annotations__.keys())

    def __repr__(self):
        get = partial(getattr, self)
        attrs = {field: get(field) for field in self.__annotations__.keys() if get(field) is not None}

        return '{}({})'.format(self.__class__.__name__, attrs)


class Skill(Rule):
    name: str
    aptitude: str
    categories: List[str]
    description: str
    fields: Optional[str]
    specializations: Optional[str]


class Trait(Rule):
    name: str
    trait_type: str
    description: str


class RulesData(object):
    def __init__(self, walk_iter: Iterator[Tuple[str, List[str], List[str]]]):
        secho('Loading rules data:', fg='yellow')

        self.skills: List[Skill] = []

        for root, _, files in walk_iter:
            for fn in files:
                with open(join(root, fn)) as f:
                    try:
                        rule = yaml.load(f)
                    except yaml.YAMLError as e:
                        secho('Error: failed loading rules file {}'.format(fn), fg='red', bold=True)
                        raise e

                    try:
                        if rule['type'] == 'skill':
                            self.skills.append(Skill(rule))
                    except KeyError as e:
                        if e.args[0] != 'type':
                            secho(
                                'Error: {} file {} is missing required key "{}:"'.format(rule['type'], fn, e.args[0]),
                                fg='red', bold=True
                             )
                        else:
                            secho(
                                'Error: rules file {} is missing required key "type:".'.format(fn),
                                fg='red', bold=True
                            )
                    else:
                        secho('• Loaded {} file {}.'.format(rule['type'], fn), fg='green')
        
        self.skills.sort(key=lambda x: x.name)

    def __getitem__(self, item: str):
        if item not in ['skills']:
            raise KeyError(item)

        return sorted(getattr(self, item))
