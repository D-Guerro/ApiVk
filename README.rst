Description
===========

An example ApiVk project.

* Documentation:
**Installation**
	* ``pip3 install ApiVk``

**Example api request**
``from api_vk.api import ApiVK``

``vk = ApiVK(token='token', group_id=0)``

``user = vk.users.get(user_ids=1)[0]``
``print("User: {} {}".format(user['first_name'], user['last_name']))``
