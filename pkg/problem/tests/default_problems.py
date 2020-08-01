from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint
from pkg.problem.problem import Problem


def default_variables():
    return [
        Variable([0, 1, 2, 3, 4, 5], []),
        Variable([0, 1, 2, 3, 4, 5], []),
        Variable([0, 1, 2, 3, 4, 5], []),
    ]


def default_consistent_problem():
    variables = default_variables()
    return Problem(
        variables,
        [
            Constraint((0, 1),
                       lambda variables: variables[0].get_value() != variables[1].get_value()),
            Constraint(tuple([2]), lambda variables: variables[0].get_value() > 0),
        ], [lambda variables: variables[0].get_value(), lambda variables: variables[1].get_value(), lambda variables: variables[2].get_value()])


def default_consistent_problem_set_values():
    problem = default_consistent_problem()
    problem.set_value(0, 2)
    problem.set_value(1, 1)
    problem.set_value(2, 2)
    return problem


def default_inconsistent_problem():
    variables = default_variables()
    return Problem(
        variables,
        [
            Constraint((0, 2),
                       lambda variables: False),
        ], [lambda variables: variables[0].get_value(), lambda variables: variables[1].get_value(), lambda variables: variables[2].get_value()])


def default_inconsistent_problem_set_values():
    problem = default_inconsistent_problem()
    problem.set_value(0, 2)
    problem.set_value(1, 1)
    problem.set_value(2, 2)
    return problem


def default_multi_objective_problem():
    variables = default_variables()
    return Problem(
        variables,
        [
            Constraint((0, 2),
                       lambda variables: variables[0] == variables[1]),
            Constraint(tuple([1]), lambda variables: variables[0] == 1),
            Constraint(tuple([2]), lambda variables: variables[0] > 0)
        ], [lambda variables: sum([var.get_value() for var in variables]), lambda variables: -sum(var.get_value() for var in variables)])


def default_multi_objective_problem_set_values():
    problem = default_multi_objective_problem()
    problem.set_value(0, 2)
    problem.set_value(1, 1)
    problem.set_value(2, 2)
    return problem
