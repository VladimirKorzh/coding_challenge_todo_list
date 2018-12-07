import redis as redis


def redis_init(application):
    application.extensions['redis'] = redis.StrictRedis(host=application.config.get('REDIS_HOST'),
                                                  port=application.config.get('REDIS_PORT'),
                                                  db=application.config.get('REDIS_DB'),
                                                  decode_responses=True)
