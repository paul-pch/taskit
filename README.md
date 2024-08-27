# Taskit CLI

Taskit is a simple command-line interface for managing tasks. It allows you to add, list, edit, and clear tasks.

## Installation

To install Taskit, clone the repository and install the dependencies:

git clone https://github.com/yourusername/taskit.git cd taskit pip install -r requirements.txt


## Usage

Taskit provides the following commands:

### `add`

Add a new task with the given label and status (default: TODO).

python taskit.py add "Buy groceries"


### `list`

List all tasks in a table, grouped by status (TODO, RUN, DONE).

python taskit.py list


### `edit`

Edit the label or status of a task with the given ID.

python taskit.py edit 1234567890 --label "Buy milk" --status RUN


### `clear`

Remove all tasks with the status DONE.

python taskit.py clear


## Configuration

Taskit stores tasks in a JSON file located at `~/.tasks.json`. You can edit this file directly to modify the tasks manually.
