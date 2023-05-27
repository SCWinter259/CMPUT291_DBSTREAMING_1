## The Pattern

The pattern we use is Model View Controller. Basically: 
- The Models are base classes. Almost all subjects mentioned in the description are Model objects.
- The Contorllers are Classes used to control and moderate the activity of the app
- The Views are what the user sees.

# Other notes

When we run this project, we a running the main file. Here is my idea:
- All SQL queries will be written into functions, and stored in `QueryFunctions.py`
- Those query functions will be called by the Model classes and the LoginView (because this is the starting view)
- Each view will return the name of the next view to be executed. To make going back possible, we have `SysStack.py` being a Controller class. It is basically a stack.
- We need SysStack because many views can lead to one view. When the user wants to go back, stack is needed to know which one to go back.
- We will then look up the view we need in `all_views.py`. Then we call the view (which is a function).
- `cache.py` and `config.py` are to cache informations that will be used throughout the app. The second caches connection and cursor, which are variables need for SQLite. The first file caches everything else.