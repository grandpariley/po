from pkg.problem.variable import Variable
from pkg.problem.constraint import Constraint
from pkg.problem.problem import Problem

def defaultVariables():
    return [
        Variable([0, 1, 2, 3, 4, 5]),
        Variable([0, 1, 2, 3, 4, 5]),
        Variable([0, 1, 2, 3, 4, 5]),
    ]

def defaultConsistentProblem():
    variables = defaultVariables()
    variables[0].set_value(2)
    variables[1].set_value(1)
    variables[2].set_value(2)
    return Problem(
        variables,
        [
            Constraint((0, 1),
                        lambda variables: variables[0] != variables[1]),
            Constraint(tuple([1]), lambda variables: variables[0] == 1),
            Constraint(tuple([2]), lambda variables: variables[0] > 0)
        ], [lambda variables: variables[0].get_value(), lambda variables: variables[1].get_value(), lambda variables: variables[2].get_value()])

def defaultInconsistentProblem():
    variables = defaultVariables()
    return Problem(
        variables,
        [
            Constraint((0, 2),
                        lambda variables: False),
        ], None)

def defaultMultiObjectiveProblem():
    variables = defaultVariables()
    variables[0].set_value(2)
    variables[1].set_value(1)
    variables[2].set_value(2)
    return Problem(
        variables,
        [
            Constraint((0, 2),
                        lambda variables: variables[0] == variables[1]),
            Constraint(tuple([1]), lambda variables: variables[0] == 1),
            Constraint(tuple([2]), lambda variables: variables[0] > 0)
        ], [lambda variables: sum([var.get_value() for var in variables]), lambda variables: -sum(var.get_value() for var in variables)])
