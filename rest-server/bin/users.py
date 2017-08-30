#!/usr/bin/env python

from actionml import HttpError

from common import *

# users_client = UsersClient(url=url)

if args.action == 'user-add':
    try:
        # res = users_client.create()
        # print_success(res, 'Created new user and bearer token. Success:\n')
        print("Adding a user, returning a user-id and token")
    except HttpError as err:
        print_failure(err, 'Error creating new user\n')

elif args.action == 'user-delete':
    user_id = args.userid
    try:
        # res = users_client.delete(u)
        # print_success(res, 'Deleted user: {} Success:\n'.format(user_id))
        print("Deleting user: {}".format(user_id))
    except HttpError as err:
        print_failure(err, 'Error deleting user.')

elif args.action == 'grant':
    engine_id = args.engineid  # non-positional engine-id passed as a param
    user_id = args.userid
    role_set = args.roleset

    try:
        # res = permissions_client.create(user_id, role_set, engine_id)
        # print_success(res, 'Added permissions for user: {} Success:\n'.format(user_id))
        print('Creating permissions for user: {} to act as: {} for engine-id: {}'.format(user_id, role_set, engine_id))
    except HttpError as err:
        print_failure(err, 'Error granting permission for user: {}\n'.format(engine_id))

elif args.action == 'revoke':
    engine_id = args.engineid  # non-positional engine-id passed as a param
    user_id = args.userid

    try:
        # res = permissions_client.delete(user_id, engine_id)
        # print_success(res, 'Added permissions for user: {} Success:\n'.format(user_id))
        print('Removing permissions for user: {} for engine-id: {}'.format(user_id, engine_id))
    except HttpError as err:
        print_failure(err, 'Error deleting permission for user: {}\n'.format(engine_id))

elif args.action == 'status':
    user_id = args.userid

    try:
        if user_id is not None:
            # res = permissions_client.get(user_id)
            # print_success(res, 'Added permissions for user: {} Success:\n'.format(user_id))
            print('Getting status for user: {}'.format(user_id))
        else:
            # res = permissions_client.get(user_id)
            # print_success(res, 'Added permissions for user: {} Success:\n'.format(user_id))
            print('Getting status for all users')
    except HttpError as err:
        print_failure(err, 'Error deleting permission for user: {}\n'.format(engine_id))

else:
    print_warning("Unknown action: %{}".format(args.action))
