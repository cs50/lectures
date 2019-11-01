```
favorites0.py
favorites1.py
favorites2.py
favorites3.py
favorites4.py

import0.py
import1.py
import2.py
search.py

import3.py
import4.py
```

```
CREATE INDEX "title_index" ON "shows" ("primaryTitle");

SELECT title FROM shows WHERE id IN (SELECT show_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = "Ellen DeGeneres"));

SELECT title FROM people JOIN stars ON people.id = stars.person_id JOIN shows ON stars.show_id = shows.id WHERE name = "Ellen DeGeneres";

SELECT title FROM people, stars, shows WHERE people.id = stars.person_id AND stars.show_id = shows.id AND name = "Ellen DeGeneres";

CREATE INDEX person_index ON stars (person_id);
CREATE INDEX show_index ON stars (show_id);
CREATE INDEX name_index ON people (name);
```
