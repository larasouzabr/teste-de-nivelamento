import axios from 'axios';
import { operadora } from '../interfaces/operadora';

const url = "http://localhost:5000/api"
export async function fetchData(query: string): Promise<operadora[]> {
    try {
        const response = await axios.get(`${url}/busca/${query}`);
        return response.data as operadora[];
    } catch (error) {
        console.error('Erro ao buscar dados:', error);
        throw error;
    }
}

export async function getDados(): Promise<operadora[]> {
    try {
        const response = await axios.get(`${url}/dados`);
        return response.data as operadora[];
    } catch (error) {
        console.error('Erro ao buscar dados:', error);
        throw error;
    }
}

