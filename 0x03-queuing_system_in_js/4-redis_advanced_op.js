import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', function() {
    console.log('Redis client connected to the server');
});

redisClient.on('error', function (err) {
    console.log(`Redis client not connected to the server: ${err}`);
});

//set key-value list
redisClient.hset('HolbertonSchools', 'Portland', '50', print);
redisClient.hset('HolbertonSchools', 'Seattle', '80', print);
redisClient.hset('HolbertonSchools', 'New York', '20', print);
redisClient.hset('HolbertonSchools', 'Bogota', '20', print);
redisClient.hset('HolbertonSchools', 'Cali', '40', print);
redisClient.hset('HolbertonSchools', 'Paris', '2', print);

// retrieve all elements stored in HolbertonSchools list
redisClient.hgetall('HolbertonSchools', function(error, result) {
    if (error) {
        console.log(error);
        throw error;
    }
    console.log(result);
});
