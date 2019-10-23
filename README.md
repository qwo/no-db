Quick
===

Datastore abstracted to primative types. We want to be the 

- ACID Compliant
- Transactional 
- No-SQL or ORM required!* (Optimizations allowed) 
- Computed Properties
- Immutable
- Binary Interfaces
- CRDT Storage per types

USAGE

=== 
# Models

User {
    name String required
    email String 
    phone Phone
    address String 
}

Phone {
    international code: number default 1
    number: validate 10
}


===
``` python

import quick
from models *


users = quick.List(Users) 



```
# From invocation to End No Abstraction 


 docker run -p 6379:6379 --name some-redis -d redis redis-server --appendonly yes                                                 


LICENSE
===
DO GOOD
