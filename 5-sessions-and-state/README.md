adk web handles eveyrthign by itself


Session, State and runner

adk web s- handle all the comlpexity
- chahting with agent - created session

State in left
- input questiosn to runner

Session: Statefull message history
- session is a state
-   Key and values

- Events
- message hsitory


Inmemory session
- savign all the conversation of hsitory in memeory
- Close all applciation, eveythign will gone

Database Session
- Eveyr time have a sesisonand will store in DB
- onr eload we can have all the session or cobevrsation agaian
- Can keep it in local computer

VertexAiSessionService
- Google cloud platfor
- Deploy your agents#
- On the cloud


Runner
- Collection of 2 peices of Info.
    - Agents
    - Session


Chattign with runner


.env file outside in root folder because we are not runnign adk web which pull out all the env variables inside of our agents.
The enviornemnt variable now need to be 


https://cloud.google.com/blog/topics/developers-practitioners/remember-this-agent-state-and-memory-with-adk

