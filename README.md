## Usage:

Start the application with `flask run`.

## Endpoints:

`/<platform>/<username>`:
Gets player level and rank information, including rank tier and current Ranked Points. Valid platforms are X1, PS, PC.

`/<platform>/<username>/<legend>`:
Gets available individual legend info based on equipped trackers. 

Ex: `GET /X1/iCATxMythos/Bloodhound`
```
{
    'Bloodhound':
    {
        'Damage': 328272,
        'Enemies scanned': 7942,
        'Kills': 1110
    }
}
```

`/<platform>/<username>/legends`:
Gets all available legend info based on equipped trackers. 

`/map_rotations`:
Displays the current map rotations for Battle Royale and Arenas game modes, both ranked and unranked.
* Field `remaining_mins` refers to how much time is left for the current map.
* Field `duration` refers to how much time the next map will be in rotation for.

