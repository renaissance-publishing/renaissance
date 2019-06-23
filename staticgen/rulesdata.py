from __future__ import annotations

from click import secho
from enum import Enum
from functools import total_ordering, reduce
from funcy.py3 import partial
from inflect import engine as inflect_engine
from os.path import join
from typing import Any, Dict, Iterator, List, Optional, Tuple, get_type_hints
import yaml


class NeedsInitializer(object):
    pass


__rule_types__: Dict[str, type] = {}


class Rule(object):
    def __init__(self, rule: Dict[str, Any]):
        for field, ty in get_type_hints(self.__class__).items():
            try:
                value = rule[field]

                if isinstance(NeedsInitializer, type(ty)):
                    setattr(self, field, ty(value))
                else:
                    setattr(self, field, value)
            except KeyError as e:
                if not hasattr(ty, '__args__') or not isinstance(None, ty.__args__):
                    raise e
                else:
                    setattr(self, field, None)

    # noinspection PyMethodOverriding,PyShadowingBuiltins
    def __init_subclass__(cls, type: str, **kwargs):
        super().__init_subclass__(**kwargs)
        __rule_types__[type] = cls
        cls.type = type

    @classmethod
    def load(cls,  rule: Dict[str, Any]) -> Tuple[str, Rule]:
        ty = rule['type']
        return ty, __rule_types__[ty](rule)

    def __repr__(self):
        get = partial(getattr, self)
        attrs = {field: get(field) for field in self.__annotations__.keys() if get(field) is not None}

        return '{}({})'.format(self.__class__.__name__, attrs)


class Skill(Rule, type='skill'):
    name: str
    aptitude: str
    categories: List[str]
    description: str
    fields: Optional[str]
    specializations: Optional[str]


class TraitType(NeedsInitializer, str, Enum):
    POSITIVE = 'positive'
    NEUTRAL = 'neutral'
    NEGATIVE = 'negative'


class Trait(Rule, type='trait'):
    name: str
    trait_type: TraitType
    description: str


inflect = inflect_engine()


class RulesData(object):
    def __init__(self, walk_iter: Iterator[Tuple[str, List[str], List[str]]]):
        secho('Loading rules data:', fg='yellow')

        self.rules_types = list(map(inflect.plural, __rule_types__.keys()))

        for ty in self.rules_types:
            setattr(self, ty, [])

        for root, _, files in walk_iter:
            for fn in files:
                with open(join(root, fn)) as f:
                    try:
                        rule = yaml.load(f, Loader=yaml.FullLoader)
                    except yaml.YAMLError as e:
                        secho('Error: failed loading rules file {}'.format(fn), fg='red', bold=True)
                        raise e

                    try:
                        ty, rule = Rule.load(rule)
                        rules = getattr(self, inflect.plural(ty))
                        rules += [rule]
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
                        secho('• Loaded {} file {}.'.format(rule.type, fn), fg='green')

        for ty in self.rules_types:
            getattr(self, ty).sort(key=lambda x: x.name)
