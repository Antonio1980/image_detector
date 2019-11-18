import functools


def automation_logger(logger):

    def decorator(func):

        @functools.wraps(func)
        def log_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                err = "{0} automation_wrapper throws an exception: {1}".format(e.__class__.__name__,
                                                                                         e.__cause__)
                logger.logger.fatal(err, exc_info=True)
                raise e

        return log_wrapper

    return decorator