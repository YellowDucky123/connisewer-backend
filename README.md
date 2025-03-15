This is the backend repo for the Connisewer project 

## Database

The database contain the following collecions:

### users

```
{
    _id: ObjectId,
    name: string,
    email: string,
    // profile_picture: string,
}
```

### toilets

```
{
    _id: ObjectId,
    location_id: int,
    title: string,
    description: string,
    location: [float, float], // lat, long
}
```

### reviews

```
{
    _id: ObjectId,
    text: string,
    rating: int,
    user_id: ObjectId,
    toilet_id: ObjectId,
}
```
