# Percepto Home Assignment

## Screenshot:
# Screenshots

![django_admin](./screenshots/forumAdmin.png)
![forum](./screenshots/forumPage.png)

## Comments:
- For the frontend authintication I used JWT tokens which was mostly boilerplate (but I totally regret it!)
- If a user is deleted all their posts will be as well (this can be changenged easily)
- UI Design was not addressed as asked in the assnment
- Added Admin UI to see data in DB
- Django user password has lots of validations required by default - I removed all of them for easier tests
- Did not add pagination but that can easily be added through DRF Pagination
- I did not use validators for forms
- Some functions here break the DRY principles - can fix if needed using mixins..
- Settings secrets SHOULD be env vars and not hardcoded - but hardcoded is more simple...

## What can be added?
- Sockets/messeges
- Signals
- Email notifications
- Model indexing and primary keys for faster quering
- Batch fetching
- More docstrings
- Tests with API mock on frontend and unit tests on backend
- Better UI/Design
- Better scurity
- 1-2 hours more will get you containers as well with docker-compose

# Backend

- Create a virtual env with `python3.9`
- Run `pip install -r requirements.txt`
- Install postgres DB and add table with name `percepto`
- Run migrtions
- Load data from fixtures folder using `./manage.py loaddata fixtures/data.json`
- Data dumped includes some threads and superuser (username/password) - admin/amin123 and site user theman/123
- to use admin site run `./manage.py  createsuperuser` and follow directions


# Frontend

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
