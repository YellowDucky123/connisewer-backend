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
}
```

### toilets

```
{
    _id: ObjectId,
    title: string,
    description: string,
    location: [float, float],
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


