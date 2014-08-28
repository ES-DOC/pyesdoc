"""
.. module:: reducer.py
   :platform: Unix, Windows
   :synopsis: Performs a reduce operation over a model_component document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def _component_predicate(c):
    """Determines whether a component is in scope or not."""
    return "OTHER" not in c.type.upper()


def _property_predicate(p):
    """Determines whether a component property is in scope or not."""
    p_values = filter(_value_predicate, p.values)

    return len(p_values) > 0 or len(p.sub_properties) > 0


def _value_predicate(v):
    """Determines whether a component property value is in scope or not."""
    return v is not None and len(str(v)) > 0


def _reduce_values(memo, v_list):
    """Reduces a set of component property values."""
    memo.extend(filter(_value_predicate, v_list))

    return memo


def _reduce_properties(memo, c, p_tree, parent=None):
    """Reduces a set of component properties."""
    # Extend property attributes.
    for p in p_tree:
        p.component = c
        p.parent = parent

    # Reduce property tree.
    for p in filter(_property_predicate, p_tree):
        memo.append((p, _reduce_values([], p.values)))
        if len(p.sub_properties) > 0:
            _reduce_properties(memo, c, p.sub_properties, p)

    return memo


def _reduce_components(memo, c_tree, parent=None):
    """Reduces a set of components."""
    # Set parent hierarchy.
    for c in c_tree:
        c.parent = parent

    # Reduce component tree.
    for c in filter(_component_predicate, c_tree):
        memo.append((c, _reduce_properties([], c, c._properties)))
        if len(c.sub_components) > 0:
            _reduce_components(memo, c.sub_components, c)

    return memo


def reduce(m):
    """Performs a reduce (fold) over a model in readiness for later processing.

    :param m: A model component.
    :type m: ontologies.cim.v1.software.ModelComponent

    :returns: A tuple containing the model and it's reduced components.
    :rtype: tuple

    """
    return (m, _reduce_components([], m.sub_components))
