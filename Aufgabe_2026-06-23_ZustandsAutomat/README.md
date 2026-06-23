# Order State Machine Implementation

This project implements a finite state machine for managing order status transitions in a controlled and validated manner.

## Features

- **Type Safety**: Full type hinting using Python's typing module.
- **Validation**: Ensures only valid state transitions are allowed.
- **Error Handling**: Custom exception for invalid state transitions.
- **Immutability**: The current status is exposed via a read-only property.

## Design Considerations

The implementation follows the State pattern, encapsulating state logic within a dedicated class. It enforces business rules through predefined transition mappings, ensuring process integrity.

## Usage

Initialize an `OrderStateMachine` with an initial status (defaults to "OFFEN"). Use the `transition_to()` method to change states, which will raise an `InvalidStateTransitionException` if the transition is not allowed.