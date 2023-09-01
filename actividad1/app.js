const express = require('express');
const axios = require('axios');
const {Client, Pool} = require('pg');
const app = express();
const main_app = express();
const PORT = 8001;
const MAIN_PORT = 8000;
app.use(express.json());
main_app.use(express.json());
const data = {
    user : "postgres",
    host : "127.0.0.1",
    database : "postgres",
    password : "Softjuandius_25",
    port : 5432
}

const client = new Client(data);

client.connect();

async function get_lyrics(req,res){
    try{
        const song = req.query.song;
        // console.log(song);
        const query = {
            text: 'SELECT text FROM spotify WHERE song = $1',
            values: [song]
        };
        const result = await client.query(query);
        // console.log(query.rows[0].text)
        res.send(result.rows[0]);
        res.end();
        
    } catch(err){
        console.log(err.message);
    }
}

async function get_duracion(req,res){
    try{
        const song = req.query.song;
        // console.log(song);
        const query = {
            text: 'SELECT duration FROM spotify2 WHERE name = $1',
            values: [song]
        };
        const result = await client.query(query);
        //console.log(query.rows[0].duration)
        res.send(result.rows[0])
        res.end();
    } catch(err){
        console.log(err.message);
    }
}

async function get_artist_lyrics(req,res){
    try{
        let artist= req.query.artist;
        artist = decodeURIComponent(artist);
        const query = await client.query(`SELECT name FROM spotify2 where artist = '[''${artist}'']'`);
        songs = query.rows.map(row => row.name);
        const resultado = {
            artista : artist,
            cancion : {}
        };
        for(const s of songs){
            //console.log(`Para la cancion ${s}:`)
            const durationResponse = await axios.get(`http://localhost:8001/getduracion?song=${s}`);
            const duration = durationResponse.data.duration;
            const lyricsResponse = await axios.get(`http://localhost:8001/getlyrics?song=${s}`);
            const lyrics = lyricsResponse.data.text;
            resultado.cancion[s] = {
                duracion : duration,
                letra : lyrics,
            };
            // console.log(lyrics);
            // console.log(`Duracion : ${duration}, Lyrics: ${lyrics}`);
        }
        // console.log(resultado);
        res.json(resultado);
        // console.log(query.rows);
        res.end();
    } catch(err){
        console.log(err.message);
    }
}

//Microservices
app.get('/getduracion',get_duracion)
app.get('/getlyrics',get_lyrics)

//API GateWay
main_app.get('/getartistlyrics',get_artist_lyrics)
main_app.get('/',(req,res)=>{
    res.send("Hola!");
})
app.listen(PORT,(req,res)=>{
    console.log("Escuchando en puerto 8001")
})

main_app.listen(MAIN_PORT,(req,res)=>{
    console.log("Escuchando en puerto 8000")
})
