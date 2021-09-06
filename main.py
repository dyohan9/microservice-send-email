import eventlet
from nameko.runners import ServiceRunner

from project import settings
from project.service import Mail

eventlet.monkey_patch(thread=False)  # thread=False fixed the debugger haning


def main():
    config = {'AMQP_URI': settings.AMQP_URI}

    runner = ServiceRunner(config=config)
    runner.add_service(Mail)
    runner.start()

    try:
        runner.wait()
    except KeyboardInterrupt:
        runner.stop()


if __name__ == '__main__':
    print('started')
    main()
