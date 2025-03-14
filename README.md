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
    reviews: [ObjectId],
    ratings: [ObjectId]
}
```

### toilets

```
{
    _id: ObjectId,
    title: string,
    description: string,
    location: [float, float],
    rating: float,
    reviews: [ObjectId]
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

### ratings

```
{
    _id: ObjectId,
    value: int,
    user_id: ObjectId,
    toilet_id: ObjectId,
}
```
