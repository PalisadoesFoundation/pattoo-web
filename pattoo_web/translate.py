"""Module that does translations."""


class KeyPair(object):
    """Class to process the results of a PairXlates object."""

    def __init__(self, data):
        """Initialize the class.

        Args:
            data: PairXlates object

        Returns:
            None

        """
        if bool(data) is True:
            self._data = data
        else:
            self._data = None

    def key(self, key, idx_pair_xlate_group):
        """Translate a key.

        Args:
            key: value to translate
            idx_pair_xlate_group: idx_pair_xlate_group value in pattoo database

        Returns:
            result: Result of the translation

        """
        # Initialize the class
        result = None
        if self._data is not None:
            for item in self._data:
                if item.idx_pair_xlate_group() == idx_pair_xlate_group:
                    translations = item.translations()
                    table = translations[idx_pair_xlate_group]
                    result = table.get(key, key)
                    break
        return result


class AgentPair(object):
    """Class to process the results of a PairXlates object."""

    def __init__(self, data):
        """Initialize the class.

        Args:
            data: PairXlates object

        Returns:
            None

        """
        # Initialize key variables
        self._lookup = {}

        # Process data
        if bool(data) is True:
            for entry in data:
                translation = entry.translation()
                for key, value in translation.items():
                    self._lookup[key] = value

    def agent_program(self, agent_program):
        """Translate a key.

        Args:
            agent_program: value to translate

        Returns:
            result: Result of the translation

        """
        # Initialize the class
        result = self._lookup.get(agent_program, agent_program)
        return result
