import { redis } from 'kue';
import { createClient, print, RedisClient } from 'redis';

const client = createClient();

RedisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
    RedisClient.quit();
});
RedisClient.on('connect', () => console.log('Redis client connected to the server'));

console.log(RedisClient.connected);

function setNewSchool(schoolName, value) {
    RedisClient.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    redisClient.get(schoolName, (_error, value) => {
        if (value) console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
