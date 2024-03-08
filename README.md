# HouseLink

## Inspiration
In our **software engineering** module for university, we have been looking at creating an application for the housing market. More specifically, a platform where landlords can upload information on any properties they own and want to rent out, and viewers can find, request to view them and ultimately review them. The purpose of this piece of software is to **weed out the inadequate landlords and properties** by incorporating a rating system, making the house-searching experience more **streamlined and stress-free** for potential renters.

Whist working on this project, we started thinking about how we could make house hunting a **more enjoyable, fun experience**. Many house searching sites simply present lots of information to viewers, in the forms of lists or grids of text. We thought it would be a great idea to turn this process into a more **interactive experience**.

## What it does
Taking inspiration from apps such as Tinder and Hinge, we have turned the search for houses into a **dating app-style experience**. Viewers are presented with a house close to their location, and they are then able to swipe left or right, depending on whether they like it or not. We then take the information from these "swipes" and use them to **recommend** other houses available in the area, which we believe that the user will enjoy the most, based off of their **previous decisions**. 

For example, a user who more frequently swipes right on houses with a larger number of bedrooms is considered **more likely** to prefer larger houses, and so presented these ones before all others. Similarly, users who swipe right on more expensive properties will be shown these more expensive options **first**. On the other hand, if a user swipes left on expensive properties, the app notes that the user is more likely to be looking on a tighter budget, and so **recommends more low cost options**.

Our aim with this app is to help keep people more **engaged, diligent and motivated** throughout the house searching process, as it can be an enduring one. By having a more interactive way of searching through their available options, we want the buyers of the housing market to feel more **connected** to the experience.

## How we built it
We built our app using **Python**, utilising its built-in libraries to create a GUI for the user to interact with it. Users are able to use the **arrow keys** to "swipe" left and right to like and dislike properties, and also view information about them. Users can **view images and descriptions** of the properties - their price, number of bedrooms/bathrooms, their addresses and also the agencies/landlords who currently own them.

To store all the houses available to view along with their details, we used **SQLite** and **integrated** it into Python. This allowed us to manipulate the database by executing SQL commands **directly from the program itself**. Using SQLite, we are able to get all the relevant information for a property we need to present to a user, giving each property the **primary key** of an ID to help identify it. Using SQLite meant we were able to store and access our data far more **cleanly and effectively**, as opposed to using a file system.

Our housing **recommender system** runs through an **AI** we developed, taking users' "swipes" as primary data to inform its decisions on which properties to recommend. Using these swipes, it calculates the **means** and **scaled standard deviations** for each different aspect of the property, then takes the field with the **lowest variance** in these standard deviations as the field most desired by the user. It uses this information to then recommend properties that **most closely match** what the user likes.

## Challenges we ran into
One challenge we found was properly **animating** the frames to replicate the "swiping" motion of such apps, due to some limitations of the GUI library we have been using. We decided to work with what we have, and so decided against replicating this swiping motion and to just slide through frames instead. While this is not the usual animation, we still believe it works well with the app we have developed.

Another challenge we faced was within our recommender system, in which we found recommendations were **never being made on price**. This is because the prices for houses varied so greatly that their standard deviations were **always much larger** than those of bedrooms and bathrooms, even if the user was consistently going for the cheaper/more expensive houses. To fix this issue, we decided to use a **scaled standard deviation** instead, and so multiplied each value by a constant to **balance them out**. This weighted standard deviation proved far more effective than our previous algorithm.

## Accomplishments that we're proud of and what we learned
As our first time building a full project with both an **AI and integrated database**, we are incredibly proud of ourselves for being able to work in some very technical aspects of programming into our work, accompanied by a **fully functional UI**. We are now far more confident in using such aspects of programming, and will definitely be able to explore them further in future projects.

We have also gained a lot of insight into **coding in a team**, as we each tackled **separate aspects** of development (e.g. backend, UI and AI) and then **integrated them** all together. Having not worked with version control software such as GitHub much before, we now feel far more experienced in the world of **team development**.

## What's next for HouseLink
We would love to take the features and functionality of our app even further. One particular concept we considered working on in our free time was the idea of introducing **different types of user** to the app, for example **buyers vs. sellers**. Sellers would be able to see a more structured view of their own properties, and also be able to **add/remove** their own from the main database. We may even consider creating a **'contact'** field so that interested buyers could get in touch with the owners of the property. This would create a whole new set of functionalities to our app, and a concept that we will definitely be thinking of taking up in our free time.
