# todo-app

Status: unfinished

## API endpoints

#### Authentication:
- `POST /auth/token`: Obtain access&refresh tokens
- `POST /auth/token/verify`: Verify access token
- `POST /auth/token/refresh`: Refresh access token
- `POST /auth/update_password`: Reset Password
- `POST /auth/register`: Register a new user
- `POST /auth/forgot_password`: Sends email with instructions to reset password
- `POST /auth/reset_password/uidb64/token`: With new password in request body, you can reset your password from here 
#### 2. Users Management:
- `GET /api/users/`: List all users.
- `POST /api/users/`: Create new user.
- `GET /api/users/<user_id>`: Retrieve the details of a specific user.
- `DELETE /api/users/<user_id>`: Delete an existing user account.
- `PUT /api/users/<user_id>`: Update an existing user account.
#### 3. Tasks Management/Actions:
- `GET /api/tasks/`: Retrieve a list of tasks. (all filters will be applied here)
- `POST /api/tasks/`: Create a new task.
- `GET /api/tasks/{task_id}/`: Retrieve details of a specific task.
- `PUT /api/tasks/{task_id}/`: Update a task.
- `DELETE /api/tasks/{task_id}/`: Delete a task.
#### 4. Categories Management:
- `GET /api/categories/`: List all categories.
- `POST /api/categories/`: Create a new category.
- `GET /api/categories/{category_id}`: Retrieve the details for a specific category.
- `PUT /api/categories/{category_id}`: Update the name for a specific category.
- `DELETE /api/categories/{category_id}`: Delete a specific category.
#### 5. Tags Management:
- `GET /api/tags/`: List all tags.
- `POST /api/tags/`: Create a new tag.
- `GET /api/tags/{tag_id}`: Retrieve the details for a specific tag.
- `PUT /api/tags/{tag_id}`: Update the details for a specific tag.
- `DELETE /api/tags/{tag_id}`: Delete a specific tag.
#### 6. Tagged Tasks Management:
- `GET /api/taggedTasks/`: List all tagged tasks.
- `POST /api/taggedTasks/`: Create a new tagged task (add a tag to a task).
- `GET /api/taggedTasks/{tagged_task_id}`: Retrieve the details for a specific tagged task.
- `PUT /api/taggedTasks/{tagged_task_id}`: Update the details for a specific tagged task (change the tag).
- `DELETE /api/taggedTasks/{tagged_task_id}`: Delete a specific tagged task (remove the tag from the task).
#### 7. Reminders Management:
- `GET /api/reminders`: List of all reminders
- `POST /api/reminders`: Create a new reminder
- `GET /api/reminders/{reminder_id}`: Retrieve the details of a specific reminder
- `PUT /api/reminders/{reminder_id}`: Update the details of a specific reminder
- `DELETE /api/reminders/{reminder_id}`: Delete a specific reminder
#### 8. Task Search:
-  `GET /api/search/`: Search tasks based on user-provided query.
