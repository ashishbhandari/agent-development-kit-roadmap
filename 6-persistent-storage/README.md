


seesion, State and Runner

Start to save our session to DB

save seesion tod atabase

- save all my sessiont o database file

empy list of reminders
begin tyhe process workign with existing session
start creatign new conversation
Workign with them
cerate new session

if talking iver and over athen pull the smae..



Totl context: access to all source to differnt attributes and acess to state and access to all source of information

Toolcontext get current state object and current remidner

add new ridmenr to save it to state

Session state
If you want your tool to explicitly store or read data like:
- last stock checked
- last joke topic
- reminders list
- user preferences
- saved selections
then ToolContext is the right choice.

So the key reason is not just “conversation history” in a general sense.

The stronger reason is:
I need my tool to access or update persistent/session data in a structured way.

ToolContext needed
Use ToolContext when:
- you want to save something
- you want to read something saved earlier
- you want memory across turns in structured form