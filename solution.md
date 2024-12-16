#### How would you change the system if we would receive a high volume of async updates to the orders placed through a socket connection on the stock exchange, e.g. execution information? Please outline the changes in the `solution.md`.
- Data Accuracy and atomicity is the key here. Inorder to achieve both,
- The System should place the order first into the DB. Once completed, spin up a coroutine (Go routine) and assosiate them to a channel.
- this coroutine will have its own backoff and no of retries values assosiated to it.
- In event of failure through the socket, this can be retried.
- This should also be achieved only when the transaction of order is committed and placed with order_placed to be `false`.
- There can also be a Background task, that executes every minute or so, to check if there are any orders that are not placed and reporocess them based on the usecase.
- The coroutine should wait for the server socket to respond so that we can have the `order_placed` field updated.