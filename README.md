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

## API

### Login

```
POST /user/register
register(username, email, password)

POST /user/login
login(email, password)

POST /user/logout
logout()

DELETE /user/delete
delete()
```

### Search

```
GET /toilets/search
search(query) => [Toilet]
```

### Reviews

```
POST /user/review/post
post_review(toilet_id, text, rating)  

PUT /user/review/edit
edit_review(review_id, text, rating)

DELETE /user/review/delete
delete_review(review_id)
```


