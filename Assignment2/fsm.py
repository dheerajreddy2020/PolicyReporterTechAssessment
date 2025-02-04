from typing import List

class FSM:
    """
    A generic Finite State Machine class.
    """

    def __init__(self, states: List[str], alphabet: List[str], initial_state: str, final_states: List[str], transitions: dict):
        """
        Initializes the FSM.

        Args:
          states: A list of states.
          alphabet: A list of input symbols.
          initial_state: The initial state.
          final_states: A list of final states.
          transitions: A dictionary of transitions, where the key is a tuple of (state, symbol)
                       and the value is the next state.
        """
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = initial_state

    def transition(self, symbol: str):
        """
        Transitions to the next state based on the current state and input symbol.

        Args:
          symbol: The input symbol.
        """
        self.current_state = self.transitions.get((self.current_state, symbol), None)
        if self.current_state is None:
            raise ValueError(f"Invalid transition for symbol: {symbol} in state: {self.current_state}")

    def process_input(self, input_string: str):
        """
        Processes the input string and returns the final state.

        Args:
          input_string: The input string.

        Returns:
          The final state.
        """
        self.current_state = self.initial_state
        for symbol in input_string:
            self.transition(symbol)
        return self.current_state

    def is_final_state(self) -> bool:
        """
        Checks if the current state is a final state.

        Returns:
          True if the current state is a final state, False otherwise.
        """
        return self.current_state in self.final_states

def mod_three_fsm(input_string: str) -> int:
    """
    Calculates the remainder when the binary number represented by the input string
    is divided by 3 using an FSM.

    Args:
      input_string: The input string representing the binary number.

    Returns:
      The remainder.
    """
    states = ['S0', 'S1', 'S2']
    alphabet = ['0', '1']
    initial_state = 'S0'
    final_states = ['S0', 'S1', 'S2']
    transitions = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2'
    }
    fsm = FSM(states, alphabet, initial_state, final_states, transitions)
    final_state = fsm.process_input(input_string)
    return states.index(final_state)

