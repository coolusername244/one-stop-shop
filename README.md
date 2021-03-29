# One Stop Shop!

Welcome to One Stop Shop! The online high street shopping outlet. 

This multi-functional web application has been made with the use of Django Full-Stack Frameworks. 
Its high powered libraries and compatability with databases allow for strong and scalable web applications. 

The site allows users to browse items throughout the store, add items to and edit the contents of their shopping cart, 
purchase items through [Stripe](https://stripe.com) and view their order history on their profile page!

Admin users are also able to add or remove items from the store while also having the ability to edit current products! 
Its also really easy for all user to view whats been happening recently with the new buliten board, superusers also have the 
functionality to add, remove or edit entries here too.

Finally, we understand that feedback and communication are important so we have our own contact page for users to get in touch!

---

While this site is not real, the best efforts have gone in to making sure that it is as functional as possible.

The live link for the [app](https://coolusername244-one-stop-shop.herokuapp.com/)

The link for the [GitHub Repo](https://github.com/coolusername244/MS4)

---
## UX

One Stop Shop was designed to have an easy, natural and familiar. In this section you will find the wireframes and User Stories. I have also included "A Typical User Journey" describing the path to build off of and relate to user stories.


### Wireframes
All of the wireframes for this project are included below, click the arrow to reveal

 - <details open>
    <summary>Base HTML</summary>
    <img src="wireframes/base-html.png">
    </details>

 - <details open>
    <summary>Home Page</summary>
    <img src="wireframes/home-page.png">
    </details>

 - <details open>
    <summary>All Products</summary>
    <img src="wireframes/all-products.png">
    </details>

 - <details open>
    <summary>Single Product</summary>
    <img src="wireframes/single-product.png">
    </details>

 - <details open>
    <summary>Shopping Bag</summary>
    <img src="wireframes/shopping-bag.png">
    </details>

 - <details open>
    <summary>Login</summary>
    <img src="wireframes/login.png">
    </details>

 - <details open>
    <summary>Register</summary>
    <img src="wireframes/register.png">
    </details>

---


### User Stories


- ### Viewing and Navigation

| USER STORY ID | AS A/AN... | I WANT TO BE ABLE TO... | SO THAT I CAN... | AS A DEVELOPER, I HAVE...
| - | - | - | - | - |
| 1 | USER | View all products that the store has to offer | Quickly see if there are any products id like to purchase | As soon as the user lands on the home page, they are greeted with some text and a button that will take them to the list of allavailable products
| 2 | USER | View individual products and their details | See all info regarding a specific item | When the user clicks on the image of a product they like the looks of, they will be redirected to the single-product-detail page
| 3 | USER | Easily see the total of all products in the basket for purchase | To avoid spending too much! | Each time the user updates the bag items, the price is automatically calculated and displayed to the user as well as their shopping bag item total

- ### Registration and Accounts

| USER STORY ID | AS A/AN... | I WANT TO BE ABLE TO... | SO THAT I CAN... | AS A DEVELOPER, I HAVE...
| - | - | - | - | - |
| 4 | NEW USER | Easily be able to register for an account | View my account details and info | Added a button labelled 'Account', when the user clicks, they will be shown 2 options, Register or Login. Clicking Register will take the user to the profile registration form.
| 5 | RETURNING USER | Easily be able to log in and out of my account | Access my personalised account | The 'Account' button will allow users to also log in and out.
| 6 | RETURNING USER | Easily recover my password if I have forgottten it | Regain access to my account | Enabled (through Django AllAuth) for the user to click the 'Forgot Password' link on the Sign In page. Clicking this will mean that the user will have to enter their email address connected to their profile and will recieve an email with instructions to reset the password
| 7 | NEW USER | Receive an email confirmation after successful registration | To ensure that the process has been successful | Once the user has filled out the registration form correctly, the user will be sent a verification email with a link to follow to activate the account. This has been achieved with Django AllAuth.
| 8 | RETURNING USER | Have a personalised account profile | Centralise all of my order history, delivery info and card info | Customer order histories are located on their profile page. They are shown a smaller version of this and are able to click the link for a full view of a particular order.

- ### Sorting and Searhing

| USER STORY ID | AS A/AN... | I WANT TO BE ABLE TO... | SO THAT I CAN... | AS A DEVELOPER, I HAVE...
| - | - | - | - | - |
| 9 | USER | Sort the list of products | By highest rated, price etc | Installed a filter located at the top of the products view. Users are able to organise by - Price, Category, Rating or Name
| 10 | USER | Easily filter products by category | So I can find the best products in the category I wish to view | Made it so the category of each item is visible and clickable. Users can click on the category name and the products will be filtered to that specific one.
| 11 | USER | Search for a product by name or description | So I can view a product I know the name of | Included a search bar that is located at the top of each page. Once users have entered a search term, the function will search all of the product info for the users query. The user is also shown the number of results and their search term, just incase they have made a typo, its easily seen. 
| 12 | USER | Be presented with the results of what I have searched for | So I can see if the product I wish to purchase is available | All of the results that have been given from the search are listed on the page, the same way they are on the products page.

- ### Purchasing and Checkout

| USER STORY ID | AS A/AN... | I WANT TO BE ABLE TO... | SO THAT I CAN... | AS A DEVELOPER, I HAVE...
| - | - | - | - | - |
| 13 | USER | Easily select the quantity and/or size of item | To ensure that I know what size/quantity I am buying | When looking at individual items, users have the option to chose how many units they want (1-90) and if the item has a size i.e. clothing, they can pick from a dropdown menu. They are also able to change the unit quantity while reviewing the bag before checkout. 
| 14 | USER | View items that are in my bag | So I can see if I am missing anything | Each time an item is added they will be shown a small window with shopping bag contents and also users are able to click the shopping cart link to review products before payment and adjust if needed. 
| 15 | USER | Adjust the item quantity in the bag | In case I feel the amount isnt right | As above
| 16 | USER | Recieve an email confirming order and successful paymenet | To ensure that everything has worked and I now sit back until delivery | Ensured that users recieve an email order confirmation once [Stripe](https://stripe.com) has recieved payment. 
| 17 | USER | Have an option to save delivery info to profile | To make future checkouts faster | On the users profile page, they will be presented with a form for their delivery information to be filled out. Once the user updates and clicks save, they can go to the checkout an their info will be prefilled.
| 18 | USER | view order confirmation after checkout | To ensure that everything has worked and I now sit back until delivery | Upon successful payment, the user will be shown a confirmation of their order as well as seeing a mesage displayed re email confirmation. 
| 19 | USER | Feel like the store has a robust checkout process | Feel safe spending money online | Using [Stripes](https://stripe.com) elements, the user will be given a secure feeling as it is filled out and reacting as needed

- ### Admin 

| USER STORY ID | AS A/AN... | I WANT TO BE ABLE TO... | SO THAT I CAN... | AS A DEVELOPER, I HAVE...
| - | - | - | - | - |
| 20 | Administrator | Add a product | Keep the store up to date | Installed a button which is located within the account dropdown menu - The button will only be visible to superuser
| 21 | Administrator | Edit a product | Keep the store up to date | Added an edit button next to items that is only visible to superusers
| 22 | Administrator | Delete a product | Keep the store up to date | Added a delete button next to items that is only visible to superusers
| 23 | Administrator | Add News Article | Keep users up to date with the latest news | Installed blog style news post to the site where only superusers have the authority to update, edit and delete. All users can view
| 24 | User and Admin | Contact the admin | Send praise or complain | I have added a contact form that once completed will notify the user that an email has been sent and will send an email to the admin (me)

- ## A typical user journey 

  - User lands on to the home page and clicks 'SHOP NOW'
  
  - User is shown all products and clicks on and likes the look of an item in the  'Womens Jeans & Trousers' category

  - User decides to look at only 'Womens Jeans & Trousers' by clicking the grey link under the price

  - User selects an item to buy, inspects the details, selects quantity and size of item

  - User is sure they would like to buy so they click 'ADD TO BAG'

  - User is show a success message containing their order and a button that will guide them towards the checkout page

  - User will have an oppertunity to review their order, change the quantity of items or remove them completely

    - Should the user remove all items from the bag, they are informed that the bag is empty and have a button back to the products page

  - Once the user is satisfied with their order they will click the 'CONTINUE TO SECURE CHECKOUT" button

  - The user will then proceed to fill out the required delivery information and at the bottom of the form, they are prompted that they will be able to save the info and create order histories by creating a profile

  - User will click to register a profile and fill out the form for verification

  - Once form is satisfied and submitted, user will recieve an email requesting to confirm their email

  - Once following the link, they are redirected to the confirm email page where they click a button to verify

  - Then required to log in

  - Then redirect to the checkout

  - Fill out the form with their details and have the checkbox ticked (this is done automatically)

  - Upon order confirmation, they are taken to the success page and will also recieve an email confirming their order

  - User can now go to their profile page and they will see their delivery info and order history

  - Once order has been placed, customer is likely to browse the rest of the site, thus seeing the news and contact

  - User clicks on the news button to see all of the latest information 

  - User then clicks on contact, sending the admin a nice thank you email

---

## Features
### Existing Features

Home Page and Base HTML - ' / '
-

- Search Bar 
  - The search bar allows users to search the site for desired products
  - If the user searches for something that is in the store such as jeans, they will be presented with all of the results and how many
  - if search bar is empty when clicked, user will be shown all products and also shown a message that the box was empty

- 'Shop Now' landing screen button
  - Designed to get the user shopping as quickly as possible
  - Once clicked, the user will be shown all the products in the store 

- Navabr
  - The navbar on desktop spans the top of the page and is home to all of the category and section buttons
  - Contains shopping cart button which adjusts the price and item quantity each time bag is updated
  - Contains Account button which, if you are not authenticated, will only have the options to login or register, once the user is logged in then they will change to 'My Profile' and 'Logout'
  - Superusers will also have the button to add a prroduct to the store
  - While not logged in, button only reads 'Account', when user is logged in, this changes to 'My Account'
  - Categories are hidden on smaller devices and are shown by a burger icon in the top left of screen

Products - ' /products '
-

 - Category Sorter 
   - This will allow users to sort the sort the products from highest to lowest in terms of:
     - Price (low to high)
     - Rating (low to high)
     - Name (A-Z)
     - Category (A-Z)
    - Once the category has been selected, javascript will refresh the page having adjusted for the conditions

- Products 
  - The user is shown all of the products in their respective category and they are all within their own package courtesy of the for loop!
  - The image is the largest part of the Product section, and once clicked will take you to the details for that product
  - Superusers are shown an edit and delete button
  - all users are shown the rating and category of the products
  - clicking on the category will show you all products that share the same category

- Single Product Detail 
  - Users are presented with a description of the item they are looking at
  - Users are able to select the quantity by pressing '+' or '-' buttons either side of the number or they can type the amount
  - If the item has a size, they are also able to select the size through a dropdown menu


- Back to Top Button 
  - As the page gets rather long, I have added a button to take the user back to the top of the page

News - ' /news ' + ' /news/add_news ' 
-

- News Blog
  - News page for users of the site to keep up to date with whats happening
  - When user is not a superuser, the News section of the navbar is just a button whereas for a superuser it is a dropdown and has the option to add an entry
  - Superusers have a form to fill and if they have no image to upload, a default image will be present instead
  - News is presented in blog post form with most recent posts at the top of the page 
  - Time of publish and author is also visable to all users

Contact - ' /contact ' 
-

- Contact Form 
  - Should the user wish to get in contact with the management for any reason, they are able to do so
  - Once the form has been submitted, the user will see a message appear on their screen explaining that it was successful and the emil was sent
  - As the store is not real, the email it gets sent to is mine

Profile - ' /profile ' 
-

- Delivery information
  - When the user first makes a profile, the form will be empty
  - The user can fill oout their profile info here and click update and it will be remembered and recalled during the checkout process
  - The user can also populate this field by filling it out within the checkuot app and having the 'remember' box checked

- Order History 
  - Users are able to view their order history here
  - When users click on the numbers that are highlighted blue they will be taken to the order confirmation for their previous order (Note - the blue numbers are the first few numbers of the order number)

Add a Product - ' /products/add ' 
-

- Add Product Form 
  - Only accessable to superusers
  - This form will add a new product to the store for all to see
  - If the form is submitted with no image, a default image will apply instead 

Shopping Cart - ' /bag ' 
- 

- Shopping Cart 
  - User is able to review their order 
  - The user is able to adjust the quantity of an item by pressing the '+' or '-' button and then clicking'Update qty'
  - The user is also able to remove the item from the bag entirely by clicking the small grey x located on right of the table
  - User is told how many items there are in total in the bag. With the use of if statements, the shopping bag will say item or items depending on value
  - User is given the button "Continue to checkout' buttton to click once they have reviewed their order 

Checkout - ' /checkout ' 
- 

- Delivery Form
  - The user has a form to fill here for their delivery info
  - The form can be filled out by updating the delivery details in the profile app
  - After ensuring that the checkbox is checked to save your info, when you submit the form, the data will also be saved to the users profile page

- Stripe 
  - Stripe has been used here to handle payments from users
  - Stripe can handle user authentication and handles responses which can be presented to the user in a UI friendly manner


- Order Summary 
  - To ensure that the customer really is sure on what they are buying, there is an order summary containing everything the user will be purchasing

---
## Testing

- Test 1 - User can add product to shopping cart - Test Passed 
  - Step 1 - click shop now
  - Step 2 - click any product
  - Step 3 - click add to bag
  - Step 4 - see success message
  - Step 5 - click shopping cart icon 
  - Step 6 - review item is in shopping bag


- Test 2 - User can remove product from cart - Test Passed 
  - Step 1 - click add to bag on a product
  - Step 2 - click shopping cart icon 
  - Step 3 - click x icon on product you wish to delete
  - Step 4 - see info message - "item removed from bag"

- Test 3 - Signing up for profile - Test Passed 
  - Step 1 - click the account button
  - Step 2 - fill in the required forms (The forms will not submit without the required forms filled correctly. Relevent error messages are displayed thanks for allauth)
  - Step 3 - go to your email 
  - Step 4 - open verification email
  - Step 5 - follow link
  - Step 6 - press confirm
  - Step 7 - sign in with your chosen username and password


- Test 4 - Adding delivery info from checkout - Test Passed 
  - Step 1 - from the shopping bag, click 'continue to secure checkout'
  - Step 2 - add all details to form
  - Step 3 - make sure that checkbox for saving info is checked (should happen automatically)
  - Step 4 - using stripes test checkout number, proceed to checkout as planned
  - Step 5 - once order is complete, navigate to My Profile
  - Step 6 - Observe that delivery info is populated


- Test 5 - Editing delivery info in profile app - Test Passed 
  - Step 1 - While in My Profile, edit the delivery info
  - Step 2 - click update information
  - Step 3 - see success message
  - Step 4 - add a product to the bag and proceed to the checkout and observe address change


- Test 6 - Review previous orders - Test Passed 
  - Step 1 - make sure you are logged in
  - Step 2 - make an order
  - Step 3 - click My Profile
  - Step 4 - On the right hand side will be a list of previous orders
  - Step 5 - click the order number
  - Step 6 - review previous order


- Test 7 - Signing in to profile - Test Passed 
  - Step 1 - ensure you are logged out
  - Step 2 - click Account button
  - Step 3 - click log in 
  - Step 4 - enter credentials
  - Step 5 - click sign in
  - Step 6 - be redirected to home page and see success message


- Test 8 - Signing out to profile - Test Passed 
  - Step 1 - Ensure you are logged in
  - Step 2 - click Account button
  - Step 3 - click logout
  - Step 4 - click sign out


- Test 9 - Getting a new password - Test Passed 
  - Step 1 - While you are logged out, click Login
  - Step 2 - click Forgot Password
  - Step 3 - enter email address
  - Step 4 - click reset my password
  - Step 5 - check your email
  - Step 6 - open email titled 'Password Reset Email'
  - Step 7 - open the link
  - Step 8 - enter new password
  - Step 9 - click change password
  - Step 10- Observe screen which says 'Your password has now been changed'

- Test 10 - Adding a news article - Test Passed 
  - Step 1 - ensure you are logged in as a superuser
  - Step 2 - click News in the navbar
  - Step 3 - click Add Entry
  - Step 4 - fill out required fields
  - Step 5 - click Add News Article
  - Step 6 - observe redirection to news page and new entry is at top
  - Step 7 - observe info message stating that news has been added successfully 


- Test 11 - Deleting a news article - Test Passed 
  - Step 1 - ensure you are logged in as a superuser
  - Step 2 - click News in the navbar
  - Step 3 - click View All
  - Step 4 - click delete on the entry you wish to discard
  - Step 5 - observe that news article has been deleted
  - Step 6 - observe info message stating that news has been deleted successfully


- Test 12 - Editing a news article - Test Passed 
  - Step 1 - ensure you are logged in as a superuser
  - Step 2 - click News in the navbar
  - Step 3 - click View All
  - Step 4 - click edit on the entry you wish to change
  - Step 5 - you will see the same form as adding but with the fields populated with the current contents
  - Step 6 - make changes and click edit article
  - Step 7 - be redirected to news page and see that blog has been changed and info message advising so


- Test 13 - Sending email to superuser - Test Passed 
  - Step 1 - click Contact Us on the navbar
  - Step 2 - fill out required fields
  - Step 3 - click send
  - Step 4 - observe redirection to home page and message confirming tha temail was sent


- Test 14 - Adding a product to the store - Test Passed 
  - Step 1 - ensure you are logged in as a superuser
  - Step 2 - click My Account
  - Step 3 - click Add A Product 
  - Step 4 - fill out required fields
  - Step 5 - click add product button
  - Step 6 - observe redirect to new product
    - Step 7 - if product has sizes, show drop down
    - Step 8 - if product has no image, show default image
    - Step 9 - if product has no rating, show 'no rating'


- Test 15 - Editing a product within the store - Test Passed 
  - Step 1 - ensure you are logged in as a superuser
  - Step 2 - you will be able to see the edit button on both the view for all products and the single product view
  - Step 3 - once clicked, you will be shown the form with all the data prefilled out
  - Step 4 - once you have made your changes click 'Update this Product'
  - Step 5 - observe redirect to product detail page and see data edited
  - Step 6 - observe info message saying update successful

- Test 16 - Deleting a product from the store - Test Passed 
  - Step 1 - ensure you are logged in as superuser
  - Step 2 - you will be able to see the delete button on both the view for all products and the single product view
  - Step 3 - when the button has been clicked, you will be redirected to the products page and see a success message



---
## Tech Used 
---
## Deployment
---
## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
---
### Media
- The photos used in this site were obtained from ...
---
### Acknowledgements

- I received inspiration for this project from X