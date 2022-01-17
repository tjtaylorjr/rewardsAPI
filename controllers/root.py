from flask import Blueprint, Response

root = Blueprint('root', __name__)


@root.get('/')
def get_root():
    return Response(
        '''
            <h1>Rewards API</h1>

            <p>A prototype for a consumer rewards web service</p>

            <a href="https://github.com/tjtaylorjr/rewardsAPI">Documentation</a>
        ''',
        status=200
    )
