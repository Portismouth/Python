SELECT*
FROM users
LEFT JOIN friendships ON USERS.ID = friendships.user_id
LEFT JOIN users AS users2 ON users2.id = friendships.friend_id