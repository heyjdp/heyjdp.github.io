--- 
title: "\U0001f4bb CRUD Put vs Patch \U0001f4dd \u274C \U0001f9f0" 
date: 2022-08-23T16:00:00+02:00 
draft: false 
tags: ["tech", "database", "http", "development"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/http-header-functions-1200x628.jpg" # image path/url
    alt: "The http header functions list" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

Should we use the http header PUT or PATCH when updating a record in a CRUD system?

<!--more-->

## CRUD RESTful APIs

CRUD or Create, Read, Update, Delete are the basic operations required to create a RESTful interface for a database backed website. From the API point of view, the following http header methods are used for the listed operations:

| API action | http header method |
| --- | --- |
| Create | PUT |
| Read | GET |
| Update | PUT/PATCH |
| Delete | DELETE |

## POST or GET for search?

I would always choose to use GET for a data retrieval operation from the server, there are three reasons for this:

1. The URL is simple, and can be shared to another person for them to GET the same view of the data as me
2. Search engines can index requests using a GET method, so the data can be indexed
3. GET is an idempotent operation (*an operation that produces the same results no matter how many times it is performed*), whereas POST is typically used to modify data on the database

## PUT vs PATCH for update?

Well, this is a little more subtle. Basically we need to consider the data set, and how much of the data set is being changed. Let's consider that I have a record:

```json
{
    "name": "Luke",
    "home": "Tattoine",
    "alliance": "Rebel scum",
    "father": "unknown"
}
```

My basic rule would be as follows:

- If I am going to change **all** of the fields in the record, then use PUT
- If I am going to modify **only some** fields in the record, then use PATCH

So, if I want to add the following to the request body:

```json
{
    "father": "Darth Vader"
}
```

then I would use a PATCH request and only send the field that needed to be updated. Easy!

