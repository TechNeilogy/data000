from datetime import datetime, timedelta
import math
import pytz
import numpy as np


class DataItem:

    def __init__(
        self,
        id,
        timestamp,
        bytes,
        duration
    ) -> None:

        self.id = id
        self.timestamp = timestamp
        self.bytes = bytes
        self.duration = duration

        self.sep = ','

    def __repr__(self) -> str:
        
        return f'{self.id}{self.sep}{self.timestamp}{self.sep}{self.bytes}{self.sep}{self.duration}'


class DataGenerator:

    def normal(
        self,
        mean,
        std,
        f = 1
    ): 
        for _ in range(0, 100):
            r = np.random.normal(mean, std)
            if r >= f:
                return r
        return f

    def generate_data(
        self,
        filepath,
        count
    ):
        np.random.seed()

        with open(filepath, 'w') as out:

            out.write('id,timestamp,duration,size\n')

            now = datetime.now(pytz.utc)

            delay_p = 0.0

            for id in range(count):

                size = max(100, np.random.uniform(1, 1000000))

                duration = self.normal(size / 100 + 10, size / 1000)

                if np.random.uniform(0, 1) < delay_p:
                    delay =  self.normal(10000 * delay_p, 2)                  
                    duration = max(1,  duration + delay)
                    delay_p = 0.0
                else:
                    delay_p += np.random.uniform(0.05, 0.08)

                now += timedelta(
                    seconds=duration/1000
                )

                data_item = DataItem(
                    id, 
                    now, 
                    duration, 
                    size
                )

                out.write(str(data_item))
                out.write('\n')
          
