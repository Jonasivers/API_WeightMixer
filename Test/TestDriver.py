import logging
from Driver import *


def test_driver():
    # set up logging to file and console
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


    try:
        # Call functions and log their outputs
        logging.info('Getting name...')
        print(get_Name())


        logging.info('Setting speed to 200...')
        print(set_Speed(200))


        logging.info('Getting speed...')
        speed = get_Speed()
        print(speed)
        logging.info(f'Speed: {speed}')

        logging.info('Getting speed set point...')
        speed_set_point = get_Speed_Set_Point()
        logging.info(f'Speed set point: {speed_set_point}')

        logging.info('Getting viscosity trend...')
        viscosity_trend = get_Viscosity_Trend()
        logging.info(f'Viscosity trend: {viscosity_trend}')

        logging.info('Starting mixer...')
        start_Mixer()

        logging.info('Stopping mixer...')
        stop_Mixer()

        logging.info('Resetting mixer...')
        reset()

        logging.info('Stopping mixer...')
        stop_Mixer()

        logging.info('Starting weight...')
        start_Weight()

        logging.info('Stopping weight...')
        stop_Weight()

        logging.info('Getting weight value...')
        weight_value = get_Weight_Value()
        logging.info(f'Weight value: {weight_value}')

        logging.info('Getting weight status...')
        time.sleep(5)
        weight_status = get_Weight_Status()
        logging.info(f'Weight status: {weight_status}')


    except Exception as e:
        # If an error occurs, log it
        logging.error(f'An error occurred: {e}')


if __name__ == '__main__':
    test_driver()
